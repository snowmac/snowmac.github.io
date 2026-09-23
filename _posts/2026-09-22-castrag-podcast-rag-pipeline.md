---
layout: post
title: "I Turned 230 Podcast Episodes Into a $33 RAG Pipeline Instead of Paying $600/Month for Coaching"
date: 2026-09-22
categories: AI RAG Automation Engineering
---

There's a personal finance podcast I like — a married couple talking through debt, budgeting, and money management for ADHD brains like mine. They also sell coaching. $600 a month.

Here's the thing: they've been podcasting for years. If they have a real framework, they've probably already said the whole thing out loud, for free, across a couple hundred episodes. I just needed a way to actually get at it.

**So instead of paying for coaching, I built a pipeline.**

## The Bet

Download every episode. Transcribe it. Make it searchable. Ask it questions the way I'd ask a coach. If the framework is real, it should hold up under direct interrogation — not just vibes-based skimming of show notes.

Total cost to test that bet against 230 episodes and ~145 hours of audio: **about $33.**

## Problem One: Your Files Are Too Big

The mp3s ran up to 150MB each — full episodes at a decent bitrate. Every transcription API has a file-size ceiling well below that, and there's no server-side workaround. You shrink the audio before it leaves your machine, or you don't get to play.

The fix is ffmpeg, chopping each file into ~15-minute mono chunks at 64kbps:

```python
cmd = [
    "ffmpeg", "-y", "-v", "error", "-i", str(src),
    "-ac", "1", "-ar", "16000", "-b:a", "64k",
    "-f", "segment", "-segment_time", str(CHUNK_SECONDS),
    pattern,
]
subprocess.run(cmd, check=True)
```

Speech doesn't need stereo or a high bitrate. Mono and 64kbps loses nothing a transcription model cares about, and it turns a 150MB upload problem into a non-problem.

## Problem Two: Sequential Is Slow, Unlimited Is Worse

First pass ran file-by-file. It worked, but it was slow enough that I restructured for two-level concurrency — multiple files at once, each with its own small thread pool for its own chunks.

**The multiplier matters.** 8 files × 3 chunk-workers each is 24 concurrent API calls, not 8, not 3. Go wider than your rate limit tier and you don't get a clean error — you get opaque connection failures that look like bugs in your code. Better to under-provision concurrency and let a retry-with-backoff loop eat the occasional transient failure than to chase a race condition that isn't one.

## Problem Three: The Secret That Shadowed Itself

This one cost me the most confused minutes of the whole project. Fresh OpenAI key, dropped into a local `.env` file. First test call: 401, quoting back a completely different, invalid key.

Something else was setting `OPENAI_API_KEY` first — a stale export sitting in my shell profile from months ago. `python-dotenv`'s `load_dotenv()` doesn't override existing environment variables by default. The shell wins, silently, with no warning that it's even happening.

```python
load_dotenv(ROOT / ".env", override=True)
```

One keyword. If an API call ever fails auth with a key that looks unfamiliar, `echo $VAR_NAME` before you start doubting your own code.

## Problem Four: Optimize Cost Mid-Flight

Batch one (52 files, 33 hours of audio) ran on `whisper-1` at $0.006/minute — about $12. Before committing to batch two (178 more files, an estimated 113 hours), I checked for something cheaper. `gpt-4o-mini-transcribe` runs at roughly half the per-minute cost with comparable quality for this use case.

```python
resp = client.audio.transcriptions.create(
    model="gpt-4o-mini-transcribe",  # was "whisper-1"
    file=f,
    response_format="text",
)
```

Same call shape. Same downstream pipeline. Because every stage skips work it's already done, swapping models mid-project didn't cost a rewrite — just a changed string and a rerun.

## Turning Text Into Something Queryable

1.29 million words of transcript is useless dumped into a single prompt. Two representations actually solved it:

**Structured summaries** — every transcript, independently, reduced to a fixed JSON shape (topics, quotes, takeaways, tone) via `response_format={"type": "json_object"}`. 230 of these ran concurrently in under 4 minutes for about 30 cents total.

**Embeddings** — each transcript chunked (1000 words, 100-word overlap) and embedded with `text-embedding-3-small`. Vectors landed in one numpy array with parallel JSON metadata:

```python
norms = np.linalg.norm(vectors, axis=1) * np.linalg.norm(query_vec)
sims = (vectors @ query_vec) / np.where(norms == 0, 1, norms)
top_idx = np.argsort(-sims)[:top_k]
```

No vector database. Cosine similarity over a few thousand 1536-dimension vectors is fast enough in plain numpy that Pinecone or Chroma would have been solving a problem I didn't have.

**Then RAG for actual answers** — embed the question, retrieve the top-k chunks, hand them to `gpt-4o-mini` with one hard rule: answer only from what's retrieved, cite the source file per claim, and say so plainly if the evidence isn't there. Grounded answers instead of the model's memory means it doesn't hallucinate advice the podcast never actually gave.

## The Verdict

**~$33 in API calls.** A pipeline that transcribes, summarizes, indexes, and answers grounded questions over any podcast archive — not just this one. And a working answer to whether that $600/month coaching framework holds up: mostly yes, with real specifics I could pull out and cite, not just marketing copy.

What I can't replicate for $33: the accountability of an actual recurring coaching call. An AI pipeline extracts a framework. It doesn't check in on you biweekly and notice you didn't stick to it.

Still — for the price of extracting the framework itself, this beat a month of the subscription by about 18x.

I open-sourced the pipeline as **castrag**: chunk it, transcribe it, summarize it, index it, ask it questions. Point it at your own audio.

---
*Ramblings from an ADHD brain that finally has a coach it can actually afford.*
