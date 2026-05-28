# Perfect Little Peelers

A lightweight dream list and personal checklist for soft longboard waves worth traveling for.

Not Surfline. Not a forecast app. Not performance surfing.

Perfect Little Peelers is for people who still love waist-high runners, soft points, clean little walls, and the kind of wave you remember because it let you glide.

## Working one-liners

- A lifetime glide list for soft waves worth traveling for.
- Not a forecast app. A checklist for the waves you’ll remember.
- The world’s best little longboard waves, collected.
- A dream list for people who still love waist-high peelers.

## V1 shape

Start small and static:

- searchable wave list
- region / country / break type / skill filters
- wave cards with why-it-belongs notes
- local checklist state: `want to hit` / `hit it`
- fake or lightweight submit-a-wave CTA

No backend until the checklist proves people care.

## Repository map

```text
data/
  waves.seed.json          Draft seed data from research pass 1

docs/
  product-brief.md         Concept, vibe, features, constraints
  build-plan.md            V1 build checklist
  data-model.md            Wave-card fields and enum notes
  shipping-hygiene.md      GitHub / ShipRank cleanliness rules
  source-plan.md           Existing planning notes copied from local source
```

## Shipping rule

This repo should stay lightweight and clean:

- source/docs/data only
- no generated build artifacts unless intentionally needed for deploy
- no scraped/raw dumps
- no stale-branch bulk merges
- if a commit exceeds 10k lines, it needs a clear reason
