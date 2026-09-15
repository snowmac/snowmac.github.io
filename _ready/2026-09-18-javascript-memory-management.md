---
layout: post
title: "JavaScript Doesn't Have Memory Leaks. Your References Do."
date: 2026-09-18
categories: JavaScript Node.js Engineering Performance
---

"JavaScript is garbage collected, so I don't have to think about memory" is one of the more expensive lies engineers tell themselves. I've been writing JavaScript since I was a teenager, and the apps that fall over aren't falling over because the garbage collector is broken. They're falling over because someone, often me, on a bad day, kept a reference alive that should have died.

This is the deep-dive I've wanted to write for years: how V8's garbage collector actually works, why "leaks" happen anyway, and how to find and fix them, in the browser and in Node.js, because the two environments leak in genuinely different ways for one structural reason that's easy to miss.

---

## The Garbage Collector's Actual Job

**What is a memory leak in JavaScript?** It's memory that's no longer needed but never gets freed, because something in your code still holds a reference to it, even unintentionally. JavaScript doesn't have leaks the way C does (forgetting to call `free()`); it has *unintended reachability*, which is a different bug with a different fix.

A garbage collector doesn't free memory you're "done with." It frees memory nothing can reach anymore. Those sound similar. They aren't. The GC only knows what's *reachable*: walkable from a root (global scope, the current call stack, active closures) through a chain of references. If your code still holds a reference to something, no matter how unintentionally, the GC considers it alive and will never touch it.

That's the whole story of a JavaScript memory leak, in either environment: not a bug in garbage collection, but an object staying reachable longer than you meant it to. Reachable, in the detached-DOM-node example further down, looks like this:

```
Root (global scope)
  └── cachedRows array
        └── <tr> element  ← still reachable, so still alive,
                             even though it's not in the DOM anymore
```

Once nothing in that chain points to the `<tr>` anymore, it looks like this instead:

```
Root (global scope)
  └── cachedRows array
        └── (nothing)      ← no path to the <tr> at all, GC collects it
```

Everything in this post comes down to that picture. Find the chain, and you've found the leak.

---

## How V8 Actually Collects Garbage

This part is identical whether you're in Chrome or Node: both run on V8. V8 splits the heap into generations, based on the generational hypothesis: most objects die young.

**Young generation.** New allocations land here first, in a small, fast space. V8's young-generation collector (nicknamed Scavenger) has traditionally used semi-space copying: the space split in two halves, everything still reachable copied from the active half to the other on each collection. Copying is fast because you're only touching live objects, which is why short-lived objects are nearly free in JavaScript. More recent V8 versions have been shifting this toward a project called Minor Mark-Sweep (Minor MS), which collects the young generation with mark-sweep instead of copying, cutting the memory overhead of maintaining two semi-spaces, while the collection itself stays parallelized across worker threads. The mental model (short-lived objects are cheap to collect) holds either way; the exact mechanism underneath it is still actively evolving.

**Old generation.** Objects that survive a couple of young-generation collections get promoted here. This space uses mark-sweep-compact instead of copying, because copying the whole old generation on every pass would be far too slow. V8 marks every reachable object from the roots, sweeps the unreachable ones, and periodically compacts to reduce fragmentation, mostly incrementally and concurrently on background threads, specifically so a full stop-the-world pause doesn't freeze whatever's running.

The engine is doing real, sophisticated work to keep collection cheap. It cannot save you from an object your own code is still pointing to, and that's where the browser and Node genuinely diverge.

### Why Doesn't Memory Drop Right After I Set Something to `null`?

Because most GC work in V8 is incremental, concurrent, and lazy on purpose, not run to completion the instant something becomes unreachable. A few things to hold in mind before you mistake normal behavior for a leak:

- **A sawtooth `heapUsed` graph is healthy, not a bug.** Memory climbs as you allocate, drops sharply when a collection runs, climbs again. That's the shape of a normal, working garbage collector. The thing to actually watch for is whether the *bottom* of each sawtooth trends upward over time, not whether the line ever goes up at all.
- **The OS doesn't always get memory back either.** Even after V8 frees a chunk of heap, the process's reserved memory (what the OS reports as RSS) doesn't necessarily shrink right away. Returning pages to the OS has its own cost, so both V8 and the underlying allocator often hold onto freed space for reuse instead of giving it back immediately. A tool reporting high memory usage isn't proof anything is still reachable that shouldn't be.
- **Heap size is not the same number as live objects.** `heapTotal` reflects how much space V8 has reserved for the heap, which can be well above what's actually in use at any given moment. `heapUsed` is the number worth watching; `heapTotal` mostly just tells you how much headroom V8 decided to keep on hand.

If you take one thing from this: don't diagnose a leak off a single high number. Diagnose it off a trend that doesn't come back down.

---

## Why the Same Engine Leaks Differently in Each Environment

A browser tab has a natural reset button: the user navigates away or closes it, and the whole heap, leaks included, goes with it. A leak in a frontend app is bounded by how long someone keeps that tab open, which is often minutes to hours.

A Node process has no such reset. It's meant to run for days or weeks between deploys, serving thousands of requests from the same long-lived heap. A leak that adds a few kilobytes per request is invisible in a five-minute test and a guaranteed out-of-memory crash three days into production. This is the single biggest reason Node memory leaks deserve more paranoia than frontend ones: the failure mode isn't a sluggish tab, it's your whole service going down.

---

## Frontend Leak Patterns

### 1. Detached DOM nodes

```javascript
let cachedRows = [];

function refreshTable(rows) {
  const table = document.getElementById('table');
  table.innerHTML = ''; // old rows removed from the DOM

  rows.forEach(row => {
    const tr = document.createElement('tr');
    tr.textContent = row.label;
    table.appendChild(tr);
    cachedRows.push(tr); // ...but a reference to every old one lives on here
  });
}
```

The old `<tr>` elements are gone from the visible DOM, but `cachedRows` still holds a reference to every one ever created. Each is "detached": removed from the tree, still reachable from JS, and the GC will never reclaim them. Run `refreshTable` a thousand times and you've got a thousand ghost tables sitting in memory.

### 2. Event listeners that outlive their element

```javascript
function attachTracking(el) {
  const onScroll = () => trackPosition(el);
  window.addEventListener('scroll', onScroll);
  // el gets removed from the DOM later, but window still holds onScroll,
  // and onScroll's closure still holds el
}
```

`window` isn't going anywhere, which means anything it holds a listener reference to isn't going anywhere either. Removing `el` from the DOM does nothing: the listener, and everything the listener closes over, stays alive for the life of the page. Always pair `addEventListener` with a matching `removeEventListener` at the point the associated element or component is torn down, or use `AbortController` to remove a whole batch of listeners in one call (the fix for this is in the last section, further down).

If you're working in React specifically, this is the exact failure mode a `useEffect` cleanup function exists to prevent: any subscription, timer, or listener set up inside an effect needs to be torn down in the function that effect returns, or it outlives the component that created it.

### 3. Sibling closures sharing a context

```javascript
function setupHandler(largeDataset) {
  const summary = summarize(largeDataset); // small, this is all we actually need

  // this closure is never called, but it references largeDataset,
  // which is enough to force largeDataset into the shared Context
  function debugDump() {
    if (largeDataset) console.log('dataset present');
  }

  document.getElementById('btn').addEventListener('click', () => {
    console.log(summary); // this closure never touches largeDataset directly
  });
}
```

This one is subtle, and it's the closure leak that actually bites people in production, not the vague "closures keep everything alive" version. V8 doesn't retain a variable just because it exists in an enclosing function; it only gets heap-allocated into a Context object if *some* closure in that scope actually references it. The catch is that sibling closures created in the same scope can end up sharing one Context object rather than each getting its own trimmed-down copy. Here, `debugDump` referencing `largeDataset` is enough to pull it into the shared Context, and because the click handler is a sibling closure over that same Context, it keeps `largeDataset` alive too, even though it never reads it. This is the mechanism behind the well-known "Meteor leak" from a few years back, and it still shows up today any time an unused or debug-only closure sits next to the one that actually matters. Delete dead closures, and split unrelated closures into genuinely separate scopes rather than leaving them next to each other "for convenience."

---

## Common Node.js Memory Leaks

### 1. EventEmitter listeners piling up per-request

```javascript
const emitter = require('./shared-emitter');

app.get('/status', (req, res) => {
  emitter.on('update', (data) => res.write(data)); // never removed
  // every request to this route adds one more permanent listener
});
```

Node's `EventEmitter` will warn you about this specifically: `MaxListenersExceededWarning: Possible EventEmitter memory leak detected. 11 listeners added.` If you've seen that warning and dismissed it, that was the leak, not a false alarm. A listener attached in a request handler and never removed accumulates one per request, forever, for the life of the process. Use `.once()` where it fits, explicitly `.removeListener()` when the request completes, or the `{ signal }` option in the last section, further down, which ties the listener's removal to a single `AbortController`.

### 2. Module-level caches with no bound

```javascript
const sessionCache = new Map(); // lives at module scope, for the process's entire life

function trackSession(id, data) {
  sessionCache.set(id, data);
}
```

This is the same unbounded-cache mistake as in the browser, but the consequence is worse: a browser tab's cache resets on reload. A Node module's top-level state persists for the entire uptime of the server. Every cache at module scope needs an eviction policy: max size, TTL, or an LRU implementation, or it's a slow-motion OOM crash with a delay timer on it.

### 3. Timers and intervals outliving their purpose

```javascript
function startPolling(connection) {
  setInterval(() => {
    connection.ping();
  }, 5000);
  // if `connection` closes, this interval, and its closure over `connection`,
  // keeps running and keeps the connection object alive indefinitely
}
```

An uncleared `setInterval` is a classic Node leak because the callback's closure keeps everything it references alive for as long as the timer runs, which, without an explicit `clearInterval`, is the life of the process. Always keep the return value of `setInterval`/`setTimeout` and clear it when the resource it depends on goes away.

---

## Catching a Leak Before It Becomes an Outage

You want a signal that fires long before a snapshot is even necessary.

- **In the browser**, the Performance Monitor tab (separate from the Memory panel) gives a live, scrubbable graph of JS heap size, DOM node count, and listener count over time. Leave it running while you use the app normally. A heap that saws up and down with GC but trends flat is healthy; one that trends up and to the right, forever, is not.
- **In Node**, log `process.memoryUsage()` on an interval in any long-running service and ship it to whatever metrics system you already use (even just stdout in a staging environment is enough to start). Watch `heapUsed` specifically. A heap that climbs in a straight line under steady traffic and never comes back down after GC is your leak, plotted for you, days before it becomes a crash.
- **RSS vs. `heapUsed`** matters here too: RSS (resident set size) includes memory outside V8's managed heap entirely. If RSS grows but `heapUsed` stays flat, look at three places before assuming a native module: `Buffer`/`ArrayBuffer` allocations, which live in the `external` field of `process.memoryUsage()` rather than `heapUsed`; an unclosed resource (a database connection, an open file handle, an un-destroyed stream); and allocator fragmentation. That third one surprises people. Under high concurrency, Linux's default glibc allocator is genuinely bad about handing freed memory back to the OS, so V8 can have correctly freed something at the JS level while RSS still looks high. Swapping in `jemalloc` or `tcmalloc` (via `LD_PRELOAD`) is a standard production fix for exactly this "phantom leak," not a JavaScript-level bug at all.
- **`--max-old-space-size`** is worth setting explicitly rather than relying on V8's default, so a real leak produces a clean, early, debuggable crash with a heap dump instead of the process silently consuming the entire host's memory first.

## How to Actually Find Memory Leaks in JavaScript (Chrome and Node)

Once you know something's leaking, the goal is the exact chain of references keeping it alive, not a guess.

**In the browser**, Chrome DevTools' Memory panel has a specific, reliable workflow for finding JavaScript memory leaks:

1. Take a heap snapshot.
2. Perform the suspect action (open/close a modal, navigate to a view and back).
3. Take a second heap snapshot.
4. Force garbage collection (the trash-can icon), then take a third snapshot.
5. Use the "Comparison" view between snapshots two and three. Anything that grew and didn't shrink after a forced GC is either a real leak or something that legitimately needs to stay alive, and DevTools shows you the retaining path directly.

The **Allocation instrumentation on timeline** recorder (also in the Memory panel) is the other half of this: it shows you *where in your code* allocations that survive are coming from, which is faster than diffing snapshots by hand when the leak is subtle.

**In Node**, the same underlying tooling works, because it's the same engine:

- Start Node with `--inspect` and open `chrome://inspect` in Chrome for the identical Memory panel and comparison workflow against a live server process.
- **`v8.writeHeapSnapshot()`** is built directly into Node core: zero dependencies, no native compilation, safe to wire up behind a signal in a running service:

  ```javascript
  const v8 = require('v8');
  process.on('SIGUSR2', () => {
    const fileName = v8.writeHeapSnapshot();
    console.log(`Heap snapshot written to ${fileName}`);
  });
  ```

  Trigger it against a live production process (`kill -USR2 <pid>`) and load the resulting `.heapsnapshot` file in Chrome DevTools exactly like a browser snapshot. This is the tool I'd reach for first now, precisely because it ships with Node itself.
- **Clinic.js** (`clinic doctor`, `clinic heapprofiler`) is still a genuinely useful next step when the built-in snapshot isn't enough. Doctor tells you *what kind* of problem you have (GC pressure, event loop blocking, I/O) before you dig further, and HeapProfiler gives you a flamegraph of allocations if it points to memory.
- **`0x`** generates a CPU flamegraph from a single command (`0x server.js`) and is useful for allocation-heavy investigations, though `node --prof` + `--prof-process`, or a CPU profile taken directly through the inspector, cover the same ground with nothing to install.
- **`why-is-node-running`** answers a narrower, very practical question: why hasn't my process exited? An open handle (a timer, a socket, a file descriptor) keeping the event loop alive is often the exact same reference that's leaking memory.

## What Actually Fixes a Leak Once You've Found It

Finding the retaining path is most of the work. The fix is usually one of a small number of moves:

- **`WeakMap` / `WeakSet`**: the fix for the detached-DOM-node cache pattern, *specifically when your keys are objects* (a DOM node, a component instance) that should be collectible the moment nothing else references them. A `WeakMap` never keeps its keys alive; a plain `Map` always does. This does **not** apply to the `sessionCache` example from the Node section above; those keys are session ID strings, and `WeakMap` only accepts object keys. For a primitive-keyed cache, you need explicit bounds instead (next bullet), not `WeakMap`.
- **`WeakRef` / `FinalizationRegistry`**: narrower tools, useful when you genuinely need to hold a reference to something without preventing its collection, and want to be notified after the fact when it's gone. Reach for these rarely and deliberately. `FinalizationRegistry` callbacks aren't guaranteed to run promptly, or at all, so they're not a substitute for actually cleaning up in the normal control flow.
- **`AbortController`**: the modern, clean way to tie a listener's lifetime to something else's, and it's not just a browser API. In the browser, pass the same `signal` to every `addEventListener` call for a component's lifetime and call `.abort()` once instead of pairing up individual `removeEventListener` calls. In Node, `EventEmitter.on()` accepts the same `{ signal }` option natively:

  ```javascript
  app.get('/status', (req, res) => {
    const ac = new AbortController();
    res.on('close', () => ac.abort()); // client disconnects, everything below is cleaned up

    emitter.on('update', (data) => res.write(data), { signal: ac.signal });
  });
  ```

  This is the direct fix for the per-request `EventEmitter` leak from earlier: one `.abort()` call on disconnect instead of remembering to `.removeListener()` on every exit path.
- **Explicit bounds on every cache**: a max size (evict oldest or least-recently-used past a limit) or a TTL. This is what actually fixes the `sessionCache` example above. There is no such thing as an unbounded cache that's actually safe; there's only one that hasn't leaked yet.
- **Regression prevention**: for anything that bit you once, add a heap-size assertion to a test: perform the suspect action N times in a headless run, force GC, assert heap growth stays under a threshold. It's a cheap test that catches the exact class of bug that's otherwise invisible until day six of uptime.

---

## The Takeaway

Same engine, same generational garbage collector, same underlying rule: nothing gets freed while something still points to it. What changes between a frontend app and a Node service is the blast radius. A browser leak degrades one person's tab until they close it. A Node leak degrades your entire service until it crashes, because there's no reload button on a server that's supposed to stay up for weeks. Find the retaining path, not the symptom, and treat every module-level cache, every event listener, and every timer as something that needs an explicit exit plan, not just a start.
