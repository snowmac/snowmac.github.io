---
layout: post
title: "I Mined 12 Months of My Own Google Voice History to Sell Leads. The First Version of My Report Would Have Cost Me the Deal."
date: 2026-10-17
categories: AI Data-Analysis Small-Business
permalink: /preview.html
---

I'm a Principal Engineer, and I run a junk removal and scrap metal business, Go Green Scrap Pros, on the side. Every lead comes in through a Google Voice number tied to the website. After a year of real volume, I wanted to sell overflow leads to another local business, but "trust me, I get a lot of calls" isn't a pitch. I needed real numbers. So I pulled a Google Takeout export covering 12 months of that number's history and built a pipeline to turn 2,200+ raw files into a report. The first version showed 423 leads. Handing that number to a buyer unvetted would have blown up the pitch the moment they asked me to walk through it.

---

## What Google Takeout Actually Gives You

A Google Voice Takeout export isn't a spreadsheet. It's one HTML file per call or text, named by phone number, call type, and timestamp (`+13035551234 - Voicemail - 2026-06-08T21_12_10Z.html`), each one a full standalone page with inline CSS, a machine-generated transcript with per-word confidence scores, and an embedded audio player pointing at the matching MP3. Across 12 months on that number, that's 2,214 files in the main call log alone, plus another 239 already sorted into a spam folder.

Buried in there was the actual signal: personal calls mixed with a steady, growing stream of "I have a mattress I need picked up" texts once the number went live as a business line.

I used an agentic workflow for one specific part of this: pulling structured fields (phone number, timestamp, transcript text) out of 2,200+ inconsistently formatted HTML files, which is exactly the kind of messy extraction task that's tedious to hand-code file by file. The actual analysis, the classification, the deduplication, the priority logic, was plain deterministic code that I wrote and checked by hand. That distinction matters for this post specifically: the thing that almost shipped a bad number wasn't the AI making something up. It was me trusting a clean-looking chart before I'd tried to break it.

---

## First Pass: Fast, Clean-Looking, and Wrong

The obvious approach is a regex classifier. Read each file, pull the transcript or text body, keyword-match it into a category (scrap metal, junk removal, mattress removal, spam, everything else), and count. That produced a report in about twenty minutes: 423 "qualified leads," a clean monthly bar chart, a category breakdown. It looked like exactly the kind of thing you'd hand a buyer.

It was also wrong, in a way that only surfaced when someone asked a simple question about it: is your catch-all "Other Inquiry" category even a real lead bucket? Going back through it, no. It was three different things jammed together. Some were genuine leads my keywords had missed (a broken TV, a treadmill, a downspout, nothing in my regex for those). A lot more were just the back half of a conversation I'd already counted somewhere else: "Where are you located?" "Cash or Venmo?" "Ok." A few were pure noise, a relative's text, a marketing cold-pitch, an automated Google Business verification code, that never should have been classified as a lead attempt at all.

---

## The Real Bug Was Structural, Not Just a Bad Bucket

Chasing that one bad category exposed the actual problem: I was counting per *file*, not per *person*. A single customer texting back and forth over three days about the same mattress pickup produced three separate text files, three separate "leads" in the tally. Checking the numbers directly: 90 phone-number-and-category combinations had more than one message counted against them, adding roughly 150 phantom leads, and 79 phone numbers were getting split across multiple categories because different messages in the same conversation happened to trip different keywords.

That's the kind of error that survives a casual read of a chart. The totals look plausible, the monthly trend looks plausible, and it only breaks when someone downstream (a buyer doing their own spot-check, or just a skeptical question) tries to reconcile the count against reality.

The real lesson was about what unit I was counting in the first place:

| Counting unit | What you actually get |
| --- | --- |
| File | Every HTML export artifact, duplicated per message |
| Message | Every inbound text, still splits one conversation into many |
| Conversation | Closer, but doesn't resolve across categories |
| Phone number | The real-world entity a lead actually maps to |

Every row above "phone number" looks like data. Only the last one is.

---

## The Fix: Dedupe to the Real-World Entity First

The fix was to stop classifying files and start classifying *people*. For every phone number, I combined all of its messages across the full time window into one blob, ran the category match against that combined text exactly once, and used the earliest contact date as the lead's month. Priority order mattered too: mattress before scrap metal before junk removal before a general catch-all, so a conversation that happened to mention both a mattress and some spare metal didn't get counted twice. That ordering reflects a real business priority call I made, not an arbitrary if/else chain. Anything that was pure scheduling chatter with no identifiable item, or a personal/vendor message with no request in it at all, got pulled out and reported separately instead of inflating the lead count.

Phone number is the best entity key available in this data, but it's not a perfect one, and it's worth saying so instead of pretending otherwise. A shared household phone, a number that changes hands, or a business line reused by a different owner years later could all violate the one-number-one-lead assumption. There's a second gap in the same spirit: collapsing a full 12-month window into a single earliest-contact date treats someone who messages in March and comes back with an unrelated job in October as one lead instead of two. A tighter version of this would sessionize by a gap in contact, not just dedupe by number. I didn't build that yet. Phone number, even with these caveats, was dramatically closer to the real business question than individual files ever were, and that's the bar it needed to clear.

The corrected numbers were smaller, and that was the point:

```
Initial classifier:      423 leads
After entity resolution: 161 leads
Inflation removed:       262 leads (62% of the original count)
```

62 real spam numbers instead of 89, and categories that held up when I actually read the transcripts behind them. A report that survives someone checking your work is worth more than one that looks better and doesn't.

---

## The Business Outcome

That corrected report became the actual pitch. I'm now working out an exclusive lead-routing deal (all categories, all leads from the website, tracked through a third-party call-tracking tool instead of the personal Google Voice number) at a flat monthly rate, benchmarked against what exclusive local-service leads actually go for. Junk removal leads run $30-80 through Google Local Services Ads, for comparison. None of that pricing conversation happens without a lead count a buyer can trust, and a buyer can't trust a count until you've tried to break it yourself first.

---

## The Takeaway

Raw exports like a Google Takeout dump aren't data. They're evidence, and the first classifier you write against them will produce a number that looks clean and isn't. The failure mode isn't usually the keyword logic; it's the counting unit. The hardest part of analytics is rarely extracting the data. It's deciding what a single row is actually supposed to represent, and checking your own answer before someone else does.
