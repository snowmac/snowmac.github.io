---
layout: post
title: "Local Seo Rebuild"
date: 2026-03-08
categories: SEO Automation Software 3.0 Small Business
---

---
title: "I Rebuilt My Entire Local SEO Strategy in One Session. Here's What That Looks Like."
date: 2026-03-08
author: Adam Bourg
tags: [SEO, Automation, Software 3.0, Small Business]
---

Let me be direct. I'm a Principal Engineer. I run a junk removal and scrap metal business on the side. And until recently, my website was a single HTML file that called itself a scrap metal company when it should have been leading with junk removal.

That's friction. That's money on the table. Let's talk about how I fixed it.

---

## The Problem: A Single Page Is Not a Strategy

The old gogreenscrappros.com was a one-page site with an emoji in the H1, schema that said "Denver" instead of "Thornton," and mattress pricing that didn't match my yard signs. Classic manual-build tech debt. The kind of thing you let slide because it "works" — until you realize it's working against you.

Google doesn't rank businesses. It ranks pages. Specific pages, for specific searches, in specific cities. If you're serving seven cities and you have one page, you're essentially asking one employee to answer seven phones simultaneously. That's not a system. That's a grind.

---

## The Software 3.0 Fix: Agentic, Not Manual

Here's how I approached it. Instead of grinding through eleven HTML files by hand, I ran an agentic session with Claude Code and treated the entire site as a single refactor problem.

What got built in one session:

- **7 city landing pages** — Thornton, Arvada, Westminster, Golden, Wheat Ridge, Broomfield, Northglenn. Each with 700+ words of unique content, LocalBusiness schema, FAQPage schema, BreadcrumbList schema, city-specific neighborhoods and zip codes.
- **Dedicated service pages** — `/mattress-removal/`, `/scrap-metal-pickup/`, `/about/`, `/contact/`.
- **A proper 404** — because Netlify serves it automatically and "page not found" is still a brand touchpoint.
- **Nav updated across all 11 pages simultaneously** — Mattress Removal, Scrap Metal, About, Contact, plus a SMS "Text Us" link.
- **og:image on every page** — logo.png, consistent social sharing card.
- **sameAs schema** — Facebook and Nextdoor URLs wired into the LocalBusiness JSON-LD.
- **Sitemap updated, robots.txt clean, Google Fonts render-blocking fixed.**
- **serve.sh** — one command hot-reload dev server, auto-installs browser-sync, no config.

That's not a weekend project. That's an afternoon.

---

## Pricing Is a Source of Truth Problem

Here's a thing nobody talks about: your pricing copy is a source of truth, and when it drifts, trust erodes.

My yard signs said $80 for mattress removal. My website said "starting at $80." Those are not the same sentence. "Starting at" implies negotiation, hidden fees, upsell at the door — exactly what I built this business not to be.

The fix was surgical. Every instance of "starting at $80" and "from $80" across the entire codebase, replaced with "$80 flat." No wiggle room in the language because there's no wiggle room in the price.

And the multi-mattress structure — $80 for the first, $60 for each additional, call for a custom quote at 6+ — that's actual pricing logic, not marketing fluff. Put the real number on the page. People respect it.

---

## Schema Is the Hidden Leverage

Most local business sites treat schema as an afterthought. That's leaving ranking signals on the floor.

Every page on this site now has:

- **LocalBusiness** with geo, hasOfferCatalog, openingHours, sameAs.
- **FAQPage** — five questions per city page, each a real search query someone types at 11pm trying to figure out how much junk removal costs.
- **BreadcrumbList** — both the JSON-LD and the visible UI nav.
- **AggregateRating placeholder** — the code comment is already in index.html, ready to uncomment when the review count hits 10+.

The sameAs array with Facebook and Nextdoor URLs is underrated. It's telling Google: this entity exists in the real world, here's the proof. That's E-E-A-T in two lines of JSON.

---

## The Off-Site Work Is Still Manual. For Now.

Here's the honest part. The site is solid. The on-page SEO is tight. But local ranking is a three-legged stool: your site, your Google Business Profile, and your citations.

The GBP verification is in progress — video verification, no postcard wait. The citations (Yelp, Bing Places, Apple Maps, Angi, BBB) are on a checklist in Apple Notes, generated in the same session.

The reviews? That's a human problem. Nobody's automated genuine customer trust. Yet.

---

## The Takeaway

You don't need a $5,000 SEO agency and a six-month roadmap to compete in local search. You need a clear mental model, a willingness to treat your website like a codebase, and enough agentic leverage to execute without grinding.

One session. Eleven pages. Fully structured, schema-validated, pricing-accurate, and deployed to Netlify via a single git push.

That's the slick, vanilla version of local SEO.

---
*Go Green Scrap Pros serves Thornton, Arvada, Westminster, Golden, Wheat Ridge, Broomfield, and Northglenn. Mattress removal $80 flat. Scrap metal pickup free. Call or text Adam: 720-675-7693.*
