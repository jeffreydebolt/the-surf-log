# Build plan

## Product correction from Jeff

The Surf Log is not just a generic surf journal. It comes from the old Perfect Little Peelers idea: a lifetime glide list for soft longboard waves worth traveling for.

The next version should feel like a travel map / dream list, not a blog and not Surfline.

## Product decisions

- [x] V1 is public browse plus local checklist first.
- [x] Use `thesurflog.com` as the canonical domain.
- [x] Host on GitHub Pages with Cloudflare DNS.
- [ ] Add map view so the list feels like a pin map for future trips.
- [ ] Add Mexico and international waves; current data is too US-heavy.
- [ ] Add general coordinates for public/famous breaks only.
- [ ] Decide whether map pins show exact public break coordinates or general town/region coordinates.
  - Recommendation: famous/public breaks can use approximate public coordinates; avoid secret-spot precision.

## Data expansion priorities

Current seed has California + a few East Coast records only. Next seed pass should add 40–80 international longboard-friendly waves.

### Priority 1 — Mexico

Add and verify famous/public longboard waves such as:

- La Saladita
- Sayulita
- La Lancha / Punta Mita area
- San Blas / Stoner’s
- 9 Palms
- Cerritos
- Scorpion Bay / San Juanico

### Priority 2 — Hawaii

Add classic public longboard waves:

- Waikiki / Queens / Canoes
- Waikiki / Publics
- Diamond Head on friendly days
- Honoli’i

### Priority 3 — Central America

Add public/famous soft wave candidates:

- Costa Rica: Tamarindo, Nosara / Guiones, Pavones if framed as long left pilgrimage not beginner wave
- Nicaragua: Popoyo beginner/inside options where appropriate, Playa Maderas if it fits
- El Salvador: El Zonte / Sunzal as public long right-point candidates

### Priority 4 — wider dream list

Add classic longboard-friendly public candidates from:

- Australia: Noosa points, Byron Bay / The Pass, Crescent Head
- France/Spain/Portugal: Biarritz/Côte des Basques, Zarautz, Ericeira/Foz do Lizandro where appropriate
- Morocco: Taghazout / Banana Point / Anchor Point caveated for skill/conditions
- Indonesia: Batu Karas, Medewi, Canggu longboard-friendly days
- Sri Lanka: Weligama, Arugam Bay baby/inside sections where appropriate

## Map view

Goal: give the feeling of a travel wall map with pins.

### V1 map behavior

- Toggle between `List` and `Map`.
- Show pins for every wave with coordinates.
- Pin color/state:
  - default: unmarked
  - warm/gold: `want to hit`
  - green/kelp: `hit it`
- Hover or tap pin:
  - wave name
  - country / region
  - one-line why it belongs
  - buttons: `Want to hit`, `Hit it`
- Clicking a pin should highlight/open the matching wave card.
- Checklist state should remain localStorage-backed for now.

### Map library recommendation

Use **Leaflet + OpenStreetMap tiles** for V1.

Why:

- No Google Maps API key.
- No billing surprise.
- Simple static-site integration.
- Good enough for travel pin map.

Files likely touched:

- `index.html` — add map/list toggle and map container.
- `assets/styles.css` — map layout, pin state styles, popup/card styles.
- `assets/app.js` — load Leaflet, render markers, sync checklist state.
- `data/waves.seed.json` — add `lat`, `lng`, and `coordinatePrecision` fields.
- `docs/data-model.md` — document coordinate fields and source requirement.

## Data model additions

Add to each wave record when known:

```json
{
  "lat": 20.1234,
  "lng": -105.1234,
  "coordinatePrecision": "public-break-approx",
  "mapNote": "Approximate public break area, not secret-spot precision"
}
```

Allowed `coordinatePrecision` values:

- `public-break-approx`
- `town-or-region`
- `hidden-unmapped`

## Tonight build list — 2026-05-28

### 1. Email forwarding

Set up the simplest useful email path:

```text
hello@thesurflog.com → Jeff's inbox
```

Recommended first path: Cloudflare Email Routing. Do not add a paid mailbox unless Jeff asks for send-as/custom mailbox behavior.

Acceptance criteria:

- `hello@thesurflog.com` exists as an inbound route.
- Test message reaches Jeff.
- Site submit CTA points to `hello@thesurflog.com` if the local form is not yet backed by real storage.

### 2. Map + data expansion

Build the next product-feel pass:

1. Add `lat/lng/coordinatePrecision` to existing records where obvious/public.
2. Add 15–25 Mexico/Hawaii/international records with approximate public coordinates and source URLs.
3. Add Leaflet map toggle.
4. Verify list filters still work.
5. Verify localStorage state updates both cards and map pins.
6. Push as one focused GitHub-visible commit.

### 3. Product path sketch

Add a short product note for future account/trip-planner features:

- V1 remains no-account/local-first.
- Account should be optional and appear as “Save my log” only after someone marks waves.
- Trip planner should answer season/skill/vibe/travel questions and suggest soft longboard destinations/clusters.
- Do not turn this into Surfline, social media, or a generic travel booking site.


## Quality / vibe

- Keep copy soulful and specific.
- Avoid generic surf-brand language.
- Avoid pretending the site knows current conditions.
- Avoid surf safety advice beyond a simple caveat.
- Do not expose secret spots or precise sensitive locations.

## Deploy

- GitHub Pages deploys from `main`.
- Cloudflare DNS points `thesurflog.com` to GitHub Pages.
- After each push, verify:

```bash
curl -I https://thesurflog.com
curl -I https://www.thesurflog.com
```
