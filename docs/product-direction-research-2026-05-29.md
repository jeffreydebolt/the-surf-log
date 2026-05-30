# The Surf Log — product direction research

Date: 2026-05-29

## Current premise to preserve

The Surf Log is not a generic surf journal and not a forecast product.

Core line:

> A lifetime glide list for soft longboard waves worth traveling for.

It should feel closer to a travel wall map, passport, and curated dream list than to Surfline, Strava, or a generic spot directory.

## Reference-site patterns

### Surfline / Magicseaweed pattern

Observed pattern:

- Forecast-first utility: know before you go.
- Live cams, hourly wind/tide/swell, expert forecast, session clips/logging, alerts, premium subscription.
- Magicseaweed now routes into Surfline, reinforcing that forecast/cam utility is consolidated.

What to borrow:

- Session/logging language only if softened.
- Optional outbound links to forecast sources later.

What not to build:

- Forecast models.
- Cams.
- Current-conditions promises.
- Performance stats.

### Surf-Forecast / spot directory pattern

Observed pattern:

- Huge global spot database.
- Country/region/break selectors.
- Spot pages with structured surf guide data: type, best season, wind/swell/tide, map, nearby breaks, photos, reviews.
- Premium features around long forecasts, alerts, maps, ad-free use.
- Explicit sensitivity around secret spots.

What to borrow:

- Structured wave-card grammar.
- Region/country hierarchy.
- Nearby breaks / map context.
- Clear secret-spot policy.

What not to build:

- Exhaustive every-break database.
- Detailed operational/safety guide that pretends to replace local knowledge.
- Fragile/secret spot exposure.

### Wannasurf / community atlas pattern

Observed pattern:

- “Surf spot atlas made by surfers for surfers.”
- Community contribution, photos, videos, countries/zones, feed of new content.
- Older community atlas feel.

What to borrow:

- Contribution loop.
- Community-confirmed spots.
- “Submitted by” / “confirmed by” provenance.

What not to build:

- Cluttered old-forum feel.
- Open-ended everything directory.
- Unmoderated submissions.

### Atlas Obscura / travel curiosity pattern

Observed pattern:

- A database of places becomes editorial discovery, trips, books, media, community, and experiences.
- Value is taste and curation, not utility alone.

What to borrow:

- Collections and editorial travel angles.
- “Why this belongs” as the heart of each card.
- Future field guide / zine / trip ideas.

### AllTrails pattern

Observed pattern:

- Searchable outdoor database.
- Saved lists, recording, recaps, maps, custom routes, offline maps, partner collections, SEO by region/city/trail.

What to borrow:

- Save/checklist behavior.
- Collections.
- Map-first discovery.
- Region/country landing pages later.

What not to build yet:

- Route planning complexity.
- Full mobile app.
- Heavy account system before local checklist proves demand.

### Strava pattern

Observed pattern:

- Track, explore, compete.
- Personal history, routes, segments, leaderboards, challenges, subscription insights.

What to borrow:

- Personal history.
- Private notes.
- Gentle completion/progress.

What not to build:

- Leaderboards.
- KOM/performance/competition energy.
- Anything that turns gliding into a metric contest.

## Differentiated product thesis

The white space is:

> A curated, emotionally resonant, longboard-specific travel atlas and lifetime checklist — closer to Atlas Obscura + AllTrails saved lists + a surf passport, with none of Surfline’s forecast burden and none of Strava’s performance pressure.

The moat is not data quantity. The moat is taste:

- what counts as a soft longboard wave worth traveling for;
- what gets excluded;
- how the site talks about glide, memory, place, and restraint;
- how it protects fragile spots.

## Buildable product directions

### 1. The glide map

The obvious next product-feel step.

Build:

- List / Map toggle.
- Leaflet + OpenStreetMap.
- Approximate pins only for public/famous breaks.
- Pin states synced to local checklist:
  - unmarked;
  - want to hit;
  - hit it.
- Popup uses existing card data.

Why it matters:

- Changes the product from a list into a travel dream object.
- Reinforces the “lifetime glide list” premise.

### 2. Source-backed wave data

Current seed has wave cards, but source URLs are not populated. Before expanding heavily, add a validator and sources.

Build:

- `scripts/validate_waves.py`.
- GitHub Action validation.
- Require unique IDs and core fields.
- Validate optional map fields.
- Populate source URLs for existing records.

Why it matters:

- Keeps public wave data trustworthy.
- Prevents sloppy data expansion as GitHub daily-shipping pressure increases.

### 3. Collections

This is the best “what can this become?” feature after map.

Possible collections:

- First longboard pilgrimage.
- Warm-water rights for noseriders.
- Soft waves near good coffee and slow mornings.
- California glide canon.
- Mexico mellow points.
- Family-friendly surf towns with real waves.
- Waves for a 9'6 log, not a shortboard.

V1 implementation:

- Add `collections` metadata to data model.
- Static collection sections/pages generated from JSON.
- No backend needed.

### 4. Surf passport / personal log

Keep it soulful, not quantified.

States:

- Want to glide.
- Paddled out.
- Got one worth remembering.
- Would return.

Optional local note prompts:

- Board ridden.
- Date/month.
- Who was there.
- One wave remembered.
- Post-surf meal / place note.

Account should appear later as “save my log,” not as a forced signup.

### 5. Editorial queue / contribution loop

Current GitHub issue submission queue is a good hacky V1.

Improve later:

- Submitter must explain why the wave belongs as a longboard/glide wave.
- Ask for public source URL.
- Ask for coordinate sensitivity.
- Review before merge.
- Show “submitted by” only after approval.

### 6. Secret-spot policy

Needs to be explicit before map/data expansion.

Policy:

- No fragile/secret waves.
- Public/famous breaks only for map pins.
- Approximate public-break or town/region coordinates.
- Takedown/correction path.
- Do not reward exposing spots.

### 7. Future monetization that fits the vibe

Do not start here, but these fit if traffic grows:

- Field guide / printable passport.
- Annual longboard travel zine.
- Tasteful affiliate links for surf camps, longboard rentals, travel lodging, board shapers.
- Sponsored collections with strong taste control.
- Small-group longboard trips much later.
- Membership for cloud-saved private log, printable passport, and member notes.

## Product risks

- Forecast creep: competing with Surfline would kill focus and create maintenance burden.
- Directory creep: including every break destroys taste.
- Secret-spot/localism risk: map expansion needs restraint.
- Strava creep: performance metrics and leaderboards conflict with the product soul.
- Data quality risk: open submissions need editorial gatekeeping.
- Generic copy risk: do not flatten this into “sessions, boards, places, notes.”

## Near-term GitHub shipping ladder

1. `test: add wave seed validation workflow`
2. `data: add source urls to existing seed waves`
3. `data: add approximate map coordinates to seed waves`
4. `feat: add checklist-synced map view`
5. `docs: add public spot and coordinate policy`
6. `data: add mexico public longboard seed pack` — only after Jeff reviews/approves public-facing wave copy.

## Weekend recommendation

Ship one Surf Log brick and one bookkeeping-awareness brick per day if energy allows, but keep them focused:

- Surf Log: validation → sources → coordinates → map.
- Bookkeeping awareness: rollout roadmap → read-only operator UI → onboarding scaffold → safe publish preview.

The Surf Log gives creative/public product momentum. Bookkeeping awareness gives revenue/product leverage. Both can be GitHub-visible without noisy generated artifacts.
