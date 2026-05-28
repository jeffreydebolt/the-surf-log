# The Surf Log

A lifetime glide list for soft longboard waves worth traveling for.

Not Surfline. Not a forecast app. Not performance surfing.

The Surf Log is for people who still love waist-high runners, soft points, clean little walls, and the kind of wave you remember because it let you glide.

## V1

Static first:

- searchable wave list
- region / skill filters
- wave cards with why-it-belongs notes
- local checklist state: `want to hit` / `hit it`
- lightweight submit-a-wave email CTA

No backend until the checklist proves people care.

## Local preview

```bash
python3 -m http.server 4177
# open http://127.0.0.1:4177
```

## Deploy recommendation

Use **Cloudflare Pages** for `thesurflog.com`.

Why: free static hosting, no app server to sleep/timeout, automatic SSL, private GitHub repo support, and simple DNS if the domain uses Cloudflare nameservers.

Cloudflare Pages settings:

- Framework preset: `None`
- Build command: leave blank
- Build output directory: `/`
- Production branch: `main`

See `docs/deploy-cloudflare-pages.md` for DNS steps.

## Repository map

```text
index.html                  Static V1 app
assets/styles.css           Site styles
assets/app.js               Search/filter/checklist behavior
data/waves.seed.json        Draft seed data from research pass 1
docs/product-brief.md       Concept, vibe, features, constraints
docs/build-plan.md          V1 build checklist
docs/deploy-cloudflare-pages.md DNS/deploy instructions
docs/data-model.md          Wave-card fields and enum notes
docs/shipping-hygiene.md    GitHub / ShipRank cleanliness rules
docs/source-plan.md         Existing planning notes copied from local source
```

## Shipping rule

This repo should stay lightweight and clean:

- source/docs/data only
- no generated build artifacts unless intentionally needed for deploy
- no scraped/raw dumps
- no stale-branch bulk merges
- if a commit exceeds 10k lines, it needs a clear reason
