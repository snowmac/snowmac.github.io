# AI Consulting SEO / Positioning Strategy — Working Notes

Status: research phase. Not for publishing — working doc to drive keyword research and content planning for adambourg.com relaunch.

## Business model under consideration

**Primary idea:** Retainer-based managed AI services for local Denver-area small businesses,
starting with trades/field-service businesses (plumbers, electricians, contractors).

- Target: 10-20 retainer clients @ $200-$500/mo = ~$2,000-$10,000/mo recurring
- Lead offer: AI receptionist / call-answering (build on Vapi or Retell dev API, not a
  white-label resale product — need to own the product/margin/content story)
- Upsell path once trust is established: SEO, web, scheduling/dispatch, review management,
  marketing automation
- Secondary/parallel track: enterprise/compliance-focused AI consulting (RAG, HIPAA/PII/PCI-SOX),
  leveraging existing `rag-saas-pitchdeck.html` and HIPAA/security background — different funnel,
  different buyer, likely needs separate positioning or site section, not the same SEO target
  as the local-trades content.

## Why AI receptionist as the lead product (not SEO/web/marketing bundle)

- Missed call = missed job — easy, visceral ROI story for a non-technical owner
- Trades workers can't answer the phone while working (hands dirty, on a roof, driving) —
  solving a known pain, not creating a new concept to explain
- Trivially demoable live in a sales conversation (call the number)
- Weaker fit for offices w/ existing front desk staff (dental, legal, medical) — there it's
  an overflow/after-hours pitch, less dramatic, but compliance angle (HIPAA) plays to existing
  strength for that vertical specifically

## Content pillars (from earlier discussion)

1. **Local problem/solution posts** — "AI phone answering for plumbers: what it costs and does,"
   "How Denver [trade] businesses stop missing after-hours calls," etc. Long-tail, low
   competition vs. big AI content mills.
2. **Case studies / proof-of-work** — highest-converting content type. Already have
   `2026-03-08-local-seo-rebuild.md` and the vector-search post as a template. Need 2-3 more
   real before/after examples, even small ones.
3. **Local-intent landing pages** (not blog posts) — one per vertical: "AI Answering Service
   for Plumbers in Denver," "AI Automation for Contractors," etc. Structured for local SEO
   (NAP consistency, service area, embedded map, testimonials).
4. **Plain-English AI explainer content** — "What AI can actually do for your small business
   (no jargon)," objection-handling before a sales call.
5. **Local presence / community** — Google Business Profile, chamber of commerce, contractor
   trade groups, referral network (leverages the scrapping-hobby blue-collar network).

## Tools / SEO research setup

- **Semrush** — already has an account for another project; add the Semrush MCP server to pull
  keyword volume/difficulty/questions directly into Claude Code sessions. Needs API key from
  Semrush account (Account Info → API).
- **Ahrefs** — alternative/supplement, official MCP server since July 2025, strong for
  backlink/competitive gap analysis.
- **DataForSEO** — pay-per-call alternative if avoiding a flat subscription, 79 tools across
  SERP/keyword/backlink/on-page.
- **Google Search Console (MCP: mcp-server-gsc)** — free, first-party, but only useful once
  the site is live and indexed. Set up + submit sitemap now regardless, so data starts
  accumulating during the content build-out.

### Keyword validation to-do (once Semrush MCP is connected)
- [ ] Volume/difficulty for "AI answering service [trade] Denver" per vertical (plumber,
      electrician, HVAC, general contractor)
- [ ] Check how saturated the space already is locally — is a national player (ServiceTitan,
      Smith.ai, Podium) already ranking for Denver-local trades + AI answering terms?
- [ ] Volume for enterprise/compliance track terms — "HIPAA compliant RAG consultant,"
      "AI consultant [industry] compliance," etc., to gauge whether that's worth a dedicated
      site section
- [ ] "Questions" / People Also Ask data for FAQ-style content targeting voice/AI search

## Case study to-dos (time-sensitive)

- [x] **Fab shop WordPress → static/Keystatic migration — "before" data captured.**
      Full site audit of the old silverengineeringworks.com, dated Aug 4, 2026 (pre-crash).
      Site is now down, so this was the only surviving record of the "before" state — copied
      into `notes/case-studies/silver-engineering-works-audit-before.pdf` in this repo.

      **Old-site findings (the actual case-study material):**
      - 97 unique pages, avg load 0.77s, slowest pages (/equipment, /industries) 1.7–2.16s
      - Homepage alone loaded 46 scripts / 63 stylesheets — "typical of a heavily
        plugin-driven WordPress/page-builder setup," per the audit
      - 75% of pages (73/97) missing meta descriptions, including the homepage, About,
        Contact, Services
      - 73% of all 674 images sitewide missing alt text (ADA/WCAG exposure + lost
        image-search SEO)
      - **Headline hook: 31 of 97 pages (a third of the site) were unmodified WooCommerce
        demo-store content — still live and purchasable.** A visitor could add a fake
        "Space Helmet" ($220) to a cart on a metal fabrication company's site. Real
        liability, not just clutter — this is the strongest, most concrete story beat.
      - 52 duplicate URL variants (www/non-www/http/trailing-slash) all returning 200
        instead of redirecting
      - 2 dead outbound links pointing to a competitor's site (pendarvismanufacturing.com)

      **To do once the new static/Keystatic site is live:**
      - [ ] Run the same audit (or PageSpeed/Lighthouse) against the new site for a direct
            before/after comparison
      - [ ] Write the case study post — lead with the demo-shop/fake-purchase finding, then
            the performance and SEO-hygiene improvements
      - [ ] Confirm none of the fab-shop's real business content/copy was lost in migration
            (the audit's word counts per page, Sheet 01, are a checklist for that)

## Vertical ideas — one file per vertical

Each candidate vertical gets its own working file once explored in depth, to keep this doc from
becoming unwieldy as more get added:

- [[med-spa-idea1]] — Med Spa / Aesthetics (Denver metro). Selected over massage/wellness,
  personal injury law intake, dog boarding, dental, and real estate after a broad curiosity pass
  across ~50 Denver-metro business types. Decision: dedicated brand (not adambourg.com),
  agentic-delivery retainer model, inbound-only distribution (no cold calling).
- [[chiropractor-idea2]] — Chiropractic (Denver metro). Runner-up to med spa: bigger,
  suburb-durable local demand and a warm first-client lead (Dr. Joshua Fern), but the
  AI-answering-service angle is already contested by 3+ national AI-native competitors, unlike
  med spa's open field.
- [[auto-repair-idea3]] — Auto repair (Denver metro), plus why fab shops/machine shops/welding/
  CNC don't work as a repeatable search-driven vertical (referral/RFQ-driven, not searched —
  keep Silver Engineering Works as a one-off case study only, not a vertical). Auto repair is a
  real open-field candidate like med spa, but lower ticket size/CPC than med spa or chiro.
- [[other-verticals-idea4]] — Personal injury law, dermatology, property management. Biggest
  dollar signals of the whole project (PI law CPC up to $235), but all three are heavily
  contested by entrenched national players (property management's top results even include the
  AI voice platform vendor itself marketing into that niche) — passed on for now in favor of
  med spa/chiro/auto repair's open fields. Full six-vertical comparison table at the bottom.

## Open questions / other things to consider

Not yet decided — flagged for discussion:

- **Vertical focus vs. broad "small business."** Sharper positioning (e.g. plumbers +
  electricians only, to start) may out-convert generic "AI for small business Denver."
- **Legal/liability.** An AI system answering calls and booking jobs on a client's behalf
  probably needs E&O / tech liability insurance and clear contract terms (what happens if the
  AI misquotes a job or mishandles an emergency call).
- **Business entity/structure.** LLC formation, contracts/MSA template for retainer clients,
  before signing paying customers.
- **Pricing tiers.** Flat retainer vs. usage-based (per-minute overages like the RAG SaaS
  pitch deck already models) — may want tiering (Starter/Pro/Enterprise) similar to that deck.
- **Onboarding repeatability.** The "low effort by client #10" assumption only holds if
  onboarding is templated (standard call-flow config, standard integrations) — worth
  designing the onboarding process before selling client #1, not after.
- **Competitive landscape check.** Local competitors already offering AI answering/automation
  to Denver trades — direct competitors, not just national platforms.
- **Distribution beyond SEO.** Existing YouTube channel (RobotGuide - AI) — could double as a
  content/lead channel; trade associations, local Chamber of Commerce, contractor referral
  networks (potentially higher-leverage than organic search for this buyer).
- **Vapi vs. Retell decision.** Still need a head-to-head on pricing/latency/integration ease
  before committing the build.
- **Site architecture.** Whether local-trades content and enterprise/compliance content live
  on the same site/nav or need separating to avoid diluting SEO signal (raised earlier,
  unresolved).
- **"Built with Claude, deployed on Cloudflare" as its own angle.** Currently rebuilding
  adambourg.com this way. Two distinct opportunities here, don't conflate them:
  - **Content asset:** document the build itself as a live case study/proof-of-work post —
    "I rebuilt my site with Claude Code and deployed it to Cloudflare in [X hours]." Same
    Tier-1 proof-of-work category as the local-seo-rebuild and vector-search posts.
  - **Possible service line:** Squarespace/Wix dissatisfaction is a well-known, common pain
    (slow editors, generic templates, recurring fees, poor SEO/performance control) —
    "AI-built custom website migration off Squarespace" could be a real wedge offer for the
    same small-business audience: fast turnaround, custom (not templated), hosted on
    Cloudflare (cheap/fast/good Core Web Vitals). Could work as a one-time build fee that
    feeds into the AI-receptionist retainer relationship, or as its own lead-gen angle
    ("Squarespace alternative Denver," "custom small business website AI built").
  - Needs its own keyword check: volume/competition for "Squarespace alternative," "leave
    Squarespace," "custom website vs Squarespace small business," etc.
  - **Broaden beyond Squarespace to WordPress too.** Also currently migrating a local fab
    shop's site off WordPress to static HTML/CSS + Keystatic (git-based page editor) deployed
    at the edge (Cloudflare Pages). WordPress pain points (slow, plugin bloat, security/
    maintenance burden, hosting costs) are at least as common as Squarespace pain points among
    small/industrial businesses — same pitch, different platform: "fast, secure, self-editable
    site with no WordPress plugin/maintenance overhead."
  - **Fab shop = strong case study candidate.** Local manufacturing/metal fab is B2B,
    trades-adjacent, not yet covered by the plumber/electrician content pillar — a good
    second/third case study once live (before/after load speed, security surface, editing
    workflow via Keystatic vs. WordPress admin). Document as a Tier-1 proof-of-work post
    once shipped.
  - Needs its own keyword check too: "WordPress alternative small business," "why is my
    WordPress site slow," "static site vs WordPress," "[industry] website redesign Denver."
