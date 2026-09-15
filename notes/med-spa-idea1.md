# Idea 1: Med Spa / Aesthetics — Dedicated AI-Agency Brand

Status: research phase, not yet named/built. Explored via Semrush MCP on 2026-09-14.
Split out of `ai-consulting-seo-strategy.md` as its own vertical file — see that doc for the
original business-model context (retainer-based AI services, broader vertical survey) this
grew out of.

## The decision

Build this as its **own dedicated brand/domain**, separate from adambourg.com.

- adambourg.com is a personal developer portfolio/blog — checked via Semrush: 8 organic
  keywords, 0 organic traffic. Nothing to inherit, so there's no cost to starting fresh.
- Med spa buyers need vertical-specific trust signals (name, positioning, case studies) that a
  general "hire Adam, developer" site can't credibly project.
- adambourg.com stays the personal portfolio + the meta case study ("I built this with Claude,
  deployed on Cloudflare") — this med spa brand becomes its own product with its own identity.

**Delivery model: agentic, not manual.** The retainer is delivered by an agent pipeline, not by
Adam doing SEO/content/follow-up by hand per client:
- Likely automated: inbound call/chat handling (AI receptionist), review-request/response
  drafts, monthly report generation, content drafts, lead nurture sequences
- Likely human-supervised: anything client-facing that needs judgment, escalations, contract/
  pricing, setup/onboarding
- This is also the marketing story itself — "an agency run by AI agents, for a business that
  runs on AI" — doubles as proof-of-work content for both this brand and adambourg.com.

## Why med spa (vs. other verticals considered)

Selected over massage/wellness, personal injury law intake, dog boarding, dental, and real
estate after a broad curiosity pass across ~50 Denver-metro business types.

- High ticket size — owners can plausibly afford a $300-500/mo retainer
- Appointment/no-show economics — "missed call = missed revenue" story, same shape as a trades
  pitch but for a higher-ticket, more sophisticated buyer
- Fragmented, owner-operator market — no dominant local chain; top 10 organic results for
  "med spa denver" are almost entirely independent single/multi-location spas
- Growing category — "how to open a med spa" / "how to find a medical director for a med spa"
  pull 260/mo each nationally, signaling steady new-business formation (not a mature, saturated
  vertical)
- HIPAA/compliance background is a real differentiator here — intake forms and health-history
  questionnaires touch PHI-adjacent data, and a generic marketing agency (studio3marketing,
  brentonway, etc.) can't credibly claim that trust signal
- Ruled out: dental (2,400/mo Denver volume, but "ai for dental office" only 40/mo — Weave/
  Solutionreach/Lighthouse 360 already own that mental space); real estate agents (local-intent
  search volume collapses outside city proper — "real estate agent thornton co" = 20/mo, buyers
  use Zillow/Realtor.com instead); dog boarding/moving/self-storage (decent volume, likely
  smaller deal size than aesthetics)

## Local consumer demand (Denver metro, Semrush US database, 2026-09-14)

- med spa denver: 1,000/mo (CPC $4.53)
- botox denver: 1,900/mo | laser hair removal denver: 1,300/mo | iv therapy denver: 880/mo |
  hydrafacial denver: 590/mo | coolsculpting denver: 390/mo
- "near me" intent is enormous nationally: botox near me = 74,000/mo, medical spa near me =
  8,100/mo — consumers search generically and rely on Google Maps/local pack, not city-name
  queries. GBP/local-pack optimization matters more than blog content for the consumer-facing
  side.
- Suburbs (Broomfield 30/mo, Arvada 10/mo) don't sustain standalone local search on their own —
  Denver proper + neighborhoods (Cherry Creek, Highlands) are the real concentration; suburbs
  are service-area, not separate markets.

## Competitive landscape (who ranks for "med spa denver")

- Independent operators, not a national chain: rejuvenatecolorado.com (#1, ~16K organic
  traffic/mo, ~$39K/mo organic traffic value), restormedicalspa.com (#2, ~5K/mo),
  aobmedspa.com (#10, ~1.7K/mo)
- **None of the top 10 run Google Ads (0 paid keywords each).** Category wins on organic/social/
  referral only — real gap for a paid or AI-driven after-hours lead-capture offer that nobody
  local is doing.

## AI-specific search demand — doesn't exist yet, don't lead with it

- "med spa ai": 10/mo, but trend jumped from a flat 0 to 1.00 in the last ~6 months of data —
  brand-new query, worth re-checking periodically, too early to build content around
- "med spa answering service," "med spa virtual receptionist," "med spa business coach": all
  0 volume — nobody phrases the need this specifically
- Nationally, "ai receptionist" (5,400/mo, strong upward trend) and "virtual receptionist for
  small business" (1,000/mo, CPC $52) show real category-level interest, but med spa owners
  aren't the ones typing it — they search in generic marketing/services terms instead

## What med spa owners actually search for help with

- med spa marketing: 1,000/mo (CPC $21) | med spa marketing agency: 1,000/mo (CPC $17,
  competitive density only 0.32) | med spa seo: 1,000/mo (CPC $21, competitive density 0.08 —
  low ad competition relative to volume)
- med spa lead generation: 210/mo but CPC $35 — highest CPC checked, strongest buyer intent
- med spa website design: 390/mo (CPC $23) | med spa consulting: 260/mo | med spa consultant:
  170/mo
- Avoid competing on "med spa software" (590/mo, CPC $56) or "med spa crm" (70/mo, CPC $54) —
  entrenched SaaS category (Boulevard, Zenoti, PatientNow, Pabau) bidding hard; not selling
  booking software, so don't fight that keyword war
- **Positioning implication:** lead with "marketing / lead generation / website," with AI-driven
  phone/booking as the differentiating mechanism inside that offer and in case studies — not as
  the headline hook. Matches actual search behavior (nobody searches "AI for my med spa").

## Service offering shape — two-pillar packaging: "AI Front Office" + free converting site

Reframed from a one-time-fee foundation into a **free site as the wedge, funded by the
retainer** — the offer becomes "free site that converts, with automated SEO baked in" +
"AI Front Office" retainer, rather than a separate upfront build fee. This is about as
frictionless a call-to-action as an inbound-only model can have (literally $0 to start), and
nothing in the competitive set (rejuvenatecolorado.com, restormedicalspa.com, etc.) offers
anything like it.

**Tradeoff to resolve before this becomes a real pitch:** giving the site away free means the
build cost sits entirely upfront on our side, recouped only through the retainer over time —
this only works with a minimum-term commitment (e.g. 12 months) in the agreement, otherwise a
client could take the free site and cancel immediately. Ties directly to the
"business entity/structure" / contracts-MSA-before-signing-clients open question in
`ai-consulting-seo-strategy.md`. The "free" economics also depend on the agentic-delivery
thesis — a fast, AI-assisted build is what makes giving the site away financially sane; a fully
manual custom build wouldn't be.

**Pillar 1 — Free site that converts, with Auto SEO (funded by retainer, not a separate fee):**
- Fast custom website (Cloudflare-hosted) replacing whatever Squarespace/Wix/WordPress they're
  on — same wedge angle as the fab-shop/adambourg.com rebuild, but given away rather than sold
- Built for conversion, not just presence — clear CTAs, click-to-call, booking widget front and
  center (matches the "near me" / local-pack-driven consumer behavior found earlier)
- **Auto SEO** — automated technical/local SEO baked into the site itself (schema markup,
  page speed, local business schema, sitemap), not a manual one-off task — Google Business
  Profile optimization + local pack setup, ongoing not one-time
- Review funnel setup (auto-request after appointment)

**Pillar 2 — AI Front Office (~$300-500/mo retainer):**
- AI phone/chat answering: after-hours and overflow capture, books consultations directly
- **AI website chatbot** for after-hours web visitors who won't call — the non-phone equivalent
  of the same capture problem (ai chatbot for website: 1,000/mo, CPC $10.92)
- Missed-call text-back + appointment reminders (no-show reduction)
- Monthly local SEO/GBP maintenance
- Bundling multiple capture channels (phone + chat + text) into one retainer spreads risk if
  any single channel turns out to be a harder sell for a given client, and is a stronger,
  stickier pitch than "AI phone answering" alone

**Upsell tier (once trust established):**
- Paid search management on the commercial terms med spas rank on (genuinely differentiating —
  none of the top 10 Denver med spas run any Google Ads today)
- Lead nurture sequences for consultation inquiries who didn't book — fits directly with
  "ai email marketing" demand (1,600/mo, CPC $26.27)
- **Social media management** — AI-drafted content + scheduling; social media management for
  small business shows 1,300/mo volume at CPC $9.02 with competitive density only **0.08**,
  the same wide-open pattern as med spa's core commercial terms
- **Review response drafting** — see reputation-management caveat below; don't sell this as a
  platform, sell it as a managed service on top of whatever platform is used

### Reputation/review management — real demand, but don't build or sell the platform

Checked as a candidate add-on since "online reputation management" (9,900/mo, CPC $25.89) and
"review management software" (1,900/mo, CPC $23.98) are large national terms. Ruled out
building or competing as a platform:

- "birdeye reviews" alone pulls **22,200/mo** in brand search; "nicejob" 1,900/mo, "podium
  reviews" 720/mo — Birdeye, Podium, and NiceJob are massive, well-funded, entrenched SMB
  reputation-management platforms. Same trap as "med spa software"/"med spa crm" — this is an
  incumbent SaaS category, not a gap.
- Organic rankings for "reputation management service" are dominated by big agencies/platforms
  (reputation.com, thriveagency.com, sproutsocial.com, reputationdefender.com) — too broad and
  generic a term to win directly, not vertical-specific.
- **The workable version:** manage review responses and follow-up as a done-for-you service —
  either reselling/integrating an existing platform under the hood or building lighter tooling —
  rather than trying to be the platform. "ai review response" (170/mo, rising trend) shows some
  direct demand for the AI-drafted-response angle specifically. Treat as a retainer add-on
  feature, not a product to sell on its own.

## Distribution: inbound only — no cold calling, no hard sales

Constraint from the business owner: customers must come to us, not the other way around. This
changes the earlier SEO conclusion — the "zero local volume" finding only applies to
*Denver-modified* terms. The **national** commercial terms have real volume with low ad
competition, and a marketing/AI-ops service doesn't need local physical presence to deliver —
so we don't need to restrict to "Denver" for the acquisition side at all.

Priority order for inbound channels:

1. **Organic content/SEO on the national commercial terms** — pages/posts targeting "med spa
   marketing agency," "med spa seo," "med spa lead generation," "med spa website design," "med
   spa consultant." Low ad competition (0.08-0.32) relative to volume (170-1,000/mo) means this
   is winnable without ad spend, just takes time. Highest-leverage channel, zero marginal cost
   once built.
2. **Case studies as the trust engine, not cold outreach.** Real before/after results (missed-
   call recovery, booking rate) sitting on the site, found rather than pitched. Fab-shop
   before/after is the template; need a med spa before/after once a first client is live.
3. **Paid search as an accelerant, not a requirement.** Given low competitive density and
   reasonable CPC ($17-21), a modest budget on the same commercial terms could get inbound leads
   flowing while organic content ranks. Still fully inbound — click an ad, land on the site,
   never a cold call.
4. **Lower priority: presence (not promotion) in r/MedSpa and aesthetic industry Facebook
   groups** — answering real questions with name/site in profile, found rather than pitched.

Explicitly ruled out: cold outreach to individual spas, conference booth sales, agency-style
discovery calls initiated by us.

## Local SEO does NOT work for selling the agency itself — important caveat

- Checked 6 Denver-modified variants of the marketing/consulting terms (marketing agency denver,
  seo denver, consultant denver, website design denver, lead generation denver, "marketing
  agency for med spas colorado") — all zero volume except "med spa marketing denver" at 10/mo.
- Organic results for the national term "med spa marketing agency" (1,000/mo) are 100% niche
  national agencies (studio3marketing, medspamarketing.com, brentonway, influxmarketing,
  orangecarrotmedia, etc.) — zero Denver-based competitors visible. Several run per-city landing
  pages (e.g. pilotpractice.com: separate Las Vegas / Miami pages) that rank on the national
  term's authority, not local search volume for the city+term combo — a programmatic-SEO
  pattern worth copying even though it won't be Denver-search-volume driven.
- r/MedSpa (Reddit) ranks #3 for "med spa marketing agency" — confirms community/word-of-mouth
  discovery is real here too, not just search.
- **Conclusion:** don't build content pillars around "med spa marketing agency Denver" — no
  local search volume to capture for selling our own services there. Use consumer-facing local
  SEO (med spa denver, botox denver, etc.) as case-study proof-of-work instead (rank a client's
  own site locally, then use that result as sales material).

## Open next steps

1. Naming/domain — signal med-spa-specific trust, not generic "AI agency"
2. Define exact scope of the agentic pipeline (automated vs. human-supervised steps)
3. Launch content plan against the validated national SEO term list
4. Land a first client to generate the real before/after case study
