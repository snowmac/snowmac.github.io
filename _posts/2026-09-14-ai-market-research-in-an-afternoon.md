---
layout: post
title: "I Pressure-Tested Six Local Business Verticals With AI Market Research in One Afternoon"
date: 2026-09-14
categories: AI Agentic-Workflows Strategy Small-Business
---

I'm a Principal Engineer, and I was about to build an AI-powered service business for local businesses in the Denver metro. Before writing a line of code, I wanted to know something basic: does anyone actually want this?

So instead of guessing, I connected Claude Code to a live SEO data source and spent an afternoon interrogating the market. Here's what that looked like, and why "just ask an AI" is the wrong way to describe what actually happened.

---

## The Setup

I connected the Semrush MCP server to Claude Code — one command, one authentication step — and started asking questions the way you'd interrogate a colleague who happened to have a Bloomberg terminal for search data: *What's the search volume for "med spa Denver"? Who's already ranking? Are they running ads? What do the actual business owners search for when they need help?*

No dashboards. No exporting CSVs into a spreadsheet and pivot-tabling my way to an insight three days later. Just a conversation that got sharper with every answer.

---

## Casting a Wide Net, On Purpose

The instinct when you have an idea is to validate *that* idea. I did the opposite — I asked the model to be curious across roughly fifty different local business categories before narrowing anything. Dentists, med spas, chiropractors, massage therapists, personal injury lawyers, dog boarders, auto shops, fab shops. Anything plausible in a Denver-metro small business economy.

That matters more than it sounds like it should. The category I *thought* made sense going in (trades — plumbers, electricians) turned out to have a much better analog once the data pushed back on my assumptions. Casting wide first is what let the numbers actually change my mind instead of just confirming what I already believed.

---

## The Pattern That Mattered Most

Across every vertical, one distinction kept showing up and kept being the actual decision-maker: **the volume of people searching for a service is a completely different number from the volume of business owners searching for help running that service** — and you have to check both, separately, before you know anything.

A few concrete examples from the actual research:

- "med spa denver" pulls 1,000 searches a month. "med spa marketing agency" *also* pulls 1,000/mo — real, provable demand from the business-owner side, not just the consumer side.
- "chiropractic answering service" pulls decent volume too, but the search results are already dominated by half a dozen national AI-answering competitors with dedicated chiropractic landing pages. Same category, wildly different competitive reality.
- One vertical had search volume in the tens of thousands for the consumer-facing term, and functionally zero for anything an owner would search when looking for marketing help. Great top-of-funnel, terrible business to sell into — nobody there thinks of themselves as running a business that needs an agency.

None of that is visible if you only check the term you already had in mind. It only shows up when you make the AI check its own assumptions against real, adjacent queries — the equivalent of a good analyst refusing to stop at the first plausible-sounding number.

---

## Checking Who's Already There, Not Just Who's Searching

Volume without competition context is just a vanity metric. For every serious candidate, I had Claude Code pull the actual organic rankings and check who was running paid ads on the term.

That single check ruled things in and out fast. One vertical looked perfect on volume and turned out to have a mature, decades-deep national industry already fighting over it — down to state bar associations listing official vendor partnerships. Another had massive dollar-value search terms, but every top result was an enterprise B2B agency built for companies with actual marketing departments, not the small owner-operators I was trying to reach. Both would have looked like wins if I'd stopped at search volume.

Conversely, the category I ended up prioritizing had real, provable demand and **zero competitors running any paid search at all** — a genuine gap, not a hunch.

---

## The Real Leverage: Turning Research Into Structure

The part that would have taken me a week with a spreadsheet took an afternoon, and not because the AI "did the thinking." It's because Claude Code could hold six parallel investigation threads, execute the actual API calls to pull live data, and — critically — write structured findings to disk as it went, so nothing got lost between the twentieth query and the fortieth.

By the end of the session I had a real, cited comparison across six verticals, ranked on the dimensions that actually mattered (local demand, owner search behavior, competitive saturation, ability to pay), sitting in version-controlled files instead of my head. That's the difference between "I asked an AI about my business idea" and doing actual market research — the second one is checkable, the first one isn't.

---

## The Takeaway

You don't need a market research firm and a six-week engagement to know whether an idea is worth building. You need a live data source, a willingness to let the data override your first instinct, and enough agentic leverage to ask the second and third question instead of stopping at the first plausible-looking number.

One afternoon. Six verticals. Fully cited, fully comparable, and sitting in a repo instead of a slide deck.

That's what "AI market research" actually looks like when it's done right.
