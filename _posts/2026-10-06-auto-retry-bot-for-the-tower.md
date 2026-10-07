---
layout: post
title: "Building an auto-retry bot for The Tower in Python"
date: 2026-10-06
categories: Python Automation macOS
---

The Tower is an idle tower-defense game. A run takes roughly 19 to 30 minutes at the tier I play, then a GAME STATS dialog appears and waits for a click on RETRY. If I'm away, the game sits idle and earns nothing. So I wrote a script to click for me.

The whole thing is one Python file, about 150 lines, plus a small PNG template.

## What it does

- Finds the "The Tower" window, wherever it is on screen.
- Every 60 seconds, looks for the RETRY button and clicks it.
- 60 seconds after a retry, taps the Defense tab and the Health upgrade.
- Taps Health again at a random interval between 90 and 300 seconds.
- Every 5 seconds, looks for the gem CLAIM button and clicks it.
- Writes every action to a log file, with a heartbeat every 30 minutes.

## How it works

### Finding the window

macOS exposes the window list through Quartz. Each entry carries a title, an owner name and its bounds on screen:

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

The script reads the bounds on every loop. That is why the window can sit on the left, middle or right of the screen and nothing changes.

### Seeing the screen

`screencapture -l <window id>` captures one window by id. It works even when part of the window is covered. The script loads the PNG with OpenCV.

This needs Screen Recording permission for your terminal app. Without it, the capture fails and the error message does not say why.

### Recognizing buttons

Buttons are found with template matching. I saved a crop of the RETRY button as `retry.png`, and `cv2.matchTemplate` slides it over the live frame:

```python
res = cv2.matchTemplate(img, tpl, cv2.TM_CCOEFF_NORMED)
_, score, _, loc = cv2.minMaxLoc(res)
if score >= 0.85:
    ...  # click the centre of the match
```

A score of 0.85 or higher counts as a match. In practice the real button scores 1.00, so there is a lot of room.

The template is created by the script itself. With the dialog showing, run `autoclick.py --learn` and it crops the button from a live capture, so the template always matches the real pixels and scale of your screen.

The CLAIM button holds a gem count that changes, so its template is only the "CLAIM" text row. The first attempt at detecting that button was too loose. A magenta game effect passed through the area and was saved as the template. I tightened the check to require the cyan border on both sides plus white text, and removed the bad file.

### Clicking

Click points are the match position converted from image pixels to screen coordinates, using the current window bounds. The fixed targets, the Defense tab and the Health upgrade box, are stored as fractions of the window, for example `(0.374, 0.975)`.

My first version did nothing. The match score was 1.00 and the script logged a click, but the game ignored it. The fix was to send a mouse-move event first, then a mouse-down and mouse-up with longer pauses:

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

Clicking needs Accessibility permission as well.

### The loop

One loop ticks once a second. Separate timestamps decide what is due: the next RETRY check, the next claim check, the shield tap, the next Health tap. A RETRY click resets the shield and Health schedule, because a new run starts from scratch.

Before any timed tap, the script checks for the RETRY dialog again. If it is up, it clicks RETRY instead. That stops a stray tap from landing on the dialog.

## Limits

- It moves your real mouse. You cannot use the Mac while it clicks.
- The game window must be on screen, uncovered, and on the active Space. Clicks are global, so they land on whatever is on top.
- The fixed tap positions fit this window layout. A different layout needs new fractions.
- It only knows about RETRY, CLAIM and the timed taps. Any other popup would leave it stuck. I have ads turned off in the game and see no other popups, so I am not worried, but the log makes a stall easy to spot: if the last line is old, it stopped.
- I tested the full flow with short timers. I have not yet watched the real 60 and 300 second timings run for hours.

I keep the Mac awake with `caffeinate -d -i`. Display sleep or a screen lock would block both capture and clicks.

## Is it worth it?

For a single-player idle game, I think so. At about 20 to 30 runs in a 10-hour night and about 30 million coins per run, that is several hundred million coins I would not otherwise collect. I did not check the game's terms of service, so if you play online or on leaderboards, read them first.

## Running it

```bash
python3 -m venv .venv
.venv/bin/pip install opencv-python-headless numpy pyobjc-framework-Quartz

# with the GAME STATS dialog on screen
.venv/bin/python autoclick.py --learn

# with the CLAIM button on screen (optional)
.venv/bin/python autoclick.py --learn-claim

# run it
caffeinate -d -i .venv/bin/python autoclick.py
```

The log is written to `autoclick.log` next to the script. Check it with `tail autoclick.log`.
