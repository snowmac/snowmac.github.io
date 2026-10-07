---
layout: post
title: "I Wrote a 150-Line Python Bot So My Idle Game Earns Coins While I Sleep"
date: 2026-10-06
categories: Python Automation macOS Engineering
---

I play an idle tower-defense game called The Tower. A run at my tier takes 19 to 30 minutes and pays out about 30 million coins. Then a GAME STATS dialog pops up and waits for me to click RETRY.

If I'm asleep, the game sits on that dialog and earns nothing. Ten hours of that is somewhere between 20 and 30 runs, or 600 to 900 million coins, left on the table.

**So I wrote a bot to click the button.** One Python file, about 150 lines, one small PNG.

## The Bet

Auto-upgrade and auto-perks are already turned on in the game, and I have ads off, so a run needs no decisions from me. The only human step is the click. If a script can see the dialog and click RETRY, the game plays itself overnight.

## Problem One: Find the Window Wherever It Is

macOS lists every window through Quartz, with its title and its bounds on screen. The script reads the bounds on every loop and works out every click as a fraction of the window.

```python
def find_window(title):
    for w in Quartz.CGWindowListCopyWindowInfo(
            Quartz.kCGWindowListOptionOnScreenOnly, Quartz.kCGNullWindowID):
        if title.lower() in (w.get("kCGWindowName") or "").lower() \
                or title.lower() in (w.get("kCGWindowOwnerName") or "").lower():
            b = w["kCGWindowBounds"]
            if b["Width"] > 200:
                return w["kCGWindowNumber"], b
    return None, None
```

That means the window can sit on the left, the middle or the right of the screen and nothing changes. The only rule is that nothing can cover it, because clicks are global and land on whatever is on top.

## Problem Two: Teach It What RETRY Looks Like

The script captures the window with `screencapture -l` and slides a saved picture of the RETRY button over it with OpenCV template matching:

```python
res = cv2.matchTemplate(img, tpl, cv2.TM_CCOEFF_NORMED)
_, score, _, loc = cv2.minMaxLoc(res)
if score >= 0.85:
    ...  # click the centre of the match
```

The real button scores 1.00, so 0.85 leaves a lot of room. I didn't want to hand-crop the template, so `autoclick.py --learn` crops it from a live capture while the dialog is up. The template always matches the exact pixels on my screen.

**One gotcha:** without Screen Recording permission for your terminal, `screencapture` just fails, and the error doesn't say why.

## Problem Three: The Click That Did Nothing

First real test. The match score was 1.00. The script logged `retry found -> click`. The dialog stayed exactly where it was.

My click was a mouse-down and a mouse-up fired back to back. The game ignored it. The fix was to move the mouse first, then press and release with real pauses:

```python
def click(x, y):
    pos = (x, y)
    for t, d in ((Quartz.kCGEventMouseMoved, 0.15),
                 (Quartz.kCGEventLeftMouseDown, 0.1),
                 (Quartz.kCGEventLeftMouseUp, 0.05)):
        Quartz.CGEventPost(Quartz.kCGHIDEventTap,
                           Quartz.CGEventCreateMouseEvent(None, t, pos, Quartz.kCGMouseButtonLeft))
        time.sleep(d)
```

Same position, same button, but now the game sees something that looks like a person. The very next run restarted on its own.

## Problem Four: Retry Wasn't Enough

Once RETRY worked, I added the rest of what I'd do by hand:

- 60 seconds after a retry, tap the Defense tab, then the Health upgrade.
- Tap Health again at a random interval between 90 and 300 seconds.
- Every 5 seconds, look for the gem CLAIM button and tap it.

Those taps use fixed positions stored as window fractions. The CLAIM button holds a gem count that changes, so its template is only the word "CLAIM".

**My first CLAIM capture saved the wrong thing.** The watcher fired on a bright magenta game effect that drifted through the spot, and I got a template of a purple arrow. I tightened the check to require a cyan border on both sides plus white text, and threw the bad file away. A blank or wrong template is worse than none, because it matches everywhere.

Before any timed tap, the script checks for the RETRY dialog again. If the dialog is up, it clicks RETRY instead of tapping a game button underneath it.

## Problem Five: Trust, but Check the Log

I'm going to leave this running while I'm asleep, so I need to see what it did. Every action goes to `autoclick.log` with a date and time, and there's an `alive` line every 30 minutes. In the morning:

```
tail autoclick.log
```

If the last line is hours old, it stopped. If it ends with `alive`, it ran all night. The count of `retry found` lines tells me how many runs it finished.

## The Verdict

**It works.** I watched it click RETRY, the next run started, then the shield tab and Health taps fired on schedule. The CLAIM tap matched at 1.00 on a live button.

Honest caveats:

- **I tested with short timers.** The real 60 and 300 second timings haven't run for hours yet. The log will tell me.
- **It moves my real mouse.** I can't use the Mac while it clicks.
- **It only knows RETRY, CLAIM and the timed taps.** Any other popup would leave it stuck. I have ads off and see no other popups.
- **I run it under `caffeinate -d -i`.** A sleeping display or a screen lock blocks both capture and clicks.
- **I didn't read the game's terms of service.** It's single-player and I'm only clicking buttons I'd click anyway, but check yours before pointing a bot at anything with leaderboards.

For a script this small, the trade is hard to argue with: one short script, and a game that earns instead of idling.

---
*Ramblings from an ADHD brain that would rather write a bot than set an alarm for 3 a.m.*
