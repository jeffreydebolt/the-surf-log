# Shipping hygiene

Perfect Little Peelers should stay clean, lightweight, and professional.

## Rules

- Keep commits focused.
- Commit source/docs/data, not generated junk.
- Do not commit scraped raw dumps.
- Do not commit build outputs unless intentionally required for deploy.
- Do not merge stale branches forward if they create giant line-count spikes.
- If a commit exceeds 10k lines, it needs a clear reason.

## Good daily ships

- Add 10–20 wave seed records.
- Add a search/filter component.
- Improve card copy.
- Add one region guide.
- Normalize one data field.
- Add one small design pass.

## Bad daily ships

- Dump 100k lines of scraped pages.
- Commit generated builds.
- Merge old branches with generated artifacts.
- Add unreviewed raw source dumps.

## Current seed size

The initial seed should remain comfortably below the 10k-line guardrail.
