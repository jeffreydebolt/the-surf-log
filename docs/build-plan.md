# Build plan

## Tiny first ship

A searchable static page with a seed wave JSON file, simple regional filters, a fake submit button, and local checklist state.

No backend until the vibe is proven.

## Product decisions

- [ ] Decide whether V1 is public browse-only plus local checklist, or login-backed checklist.
  - Recommendation: public browse + local checklist first.
- [ ] Decide first geography scope.
  - Recommendation: seed 40–60 waves first, then expand.
- [ ] Decide whether to show exact map pins or general regions.
  - Recommendation: public/famous waves only; no secret-spot precision.

## Data

- [x] Create `data/waves.seed.json` with draft fields.
- [x] Add California seed records from research pass 1.
- [x] Add NC/East Coast seed records from research pass 1.
- [ ] Complete Hawaii/Mexico research pass.
- [ ] Add Waikiki / Queens / Canoes.
- [ ] Add Honoli’i.
- [ ] Add 9 Palms.
- [ ] Add La Lancha.
- [ ] Add Jeff-known Dominican Republic wave once identified.

## V1 interface

- [ ] Static page with title and vibe sentence.
- [ ] Search.
- [ ] Filters: region, country, break type, skill level, direction, tags.
- [ ] Wave cards.
- [ ] Card actions: “Want to hit” and “Hit it.”
- [ ] Store checklist state in localStorage.
- [ ] Add “submit a wave” fake CTA or lightweight form.

## Quality / vibe

- [ ] Write short copy so it feels soulful, not like Surfline.
- [ ] Add “not a forecast app” disclaimer.
- [ ] Add safety/conditions disclaimer: skill labels are general, not live safety advice.
- [ ] Make mobile layout excellent first.

## Deploy

- [ ] Deploy static V1 to Vercel, Netlify, or GitHub Pages.
- [ ] Share private link with 3–5 surf friends/clients.
- [ ] Collect missing-wave suggestions and confusion points.
