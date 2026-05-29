#!/usr/bin/env python3
"""Turn a wave-submission issue into a data/waves.seed.json PR.

This is intentionally conservative: it only creates a draft-ish record from
public issue fields and opens a PR for human review. It does not auto-merge.
"""

from __future__ import annotations

import json
import os
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DATA_PATH = ROOT / "data" / "waves.seed.json"


def slugify(value: str) -> str:
    value = value.lower().strip()
    value = re.sub(r"[^a-z0-9]+", "-", value)
    return value.strip("-") or "wave"


def section(body: str, heading: str) -> str:
    pattern = rf"^##\s+{re.escape(heading)}\s*$([\s\S]*?)(?=^##\s+|\Z)"
    match = re.search(pattern, body or "", flags=re.MULTILINE | re.IGNORECASE)
    if not match:
        return ""
    return match.group(1).strip()


def run(cmd: list[str]) -> str:
    print("+", " ".join(cmd))
    result = subprocess.run(cmd, cwd=ROOT, text=True, capture_output=True)
    if result.stdout:
        print(result.stdout)
    if result.stderr:
        print(result.stderr, file=sys.stderr)
    if result.returncode != 0:
        raise SystemExit(result.returncode)
    return result.stdout.strip()


def main() -> int:
    event_path = os.environ.get("GITHUB_EVENT_PATH")
    if not event_path:
        raise SystemExit("GITHUB_EVENT_PATH is required")

    event = json.loads(Path(event_path).read_text())
    issue = event.get("issue") or {}
    issue_number = issue.get("number")
    body = issue.get("body") or ""
    title = issue.get("title") or "Wave suggestion"

    labels = {label.get("name") for label in issue.get("labels", [])}
    if "wave-submission" not in labels:
        print("Issue is not labeled wave-submission; skipping.")
        return 0

    name = section(body, "Wave name") or re.sub(r"^Wave suggestion:\s*", "", title, flags=re.I).strip()
    region = section(body, "General region / country") or "Needs review"
    why = section(body, "Why it belongs") or "Submitted for review."
    season = section(body, "Best season / window if known") or "Needs research"
    watch_out = section(body, "Anything to watch out for")
    source = section(body, "Public source or reference, if any")

    if not name or name.lower() == "wave suggestion":
        raise SystemExit("Could not parse a wave name from the issue")

    country = "Needs review"
    if "," in region:
        country = region.rsplit(",", 1)[-1].strip() or country

    wave_id = slugify(f"{name}-{region}")
    waves = json.loads(DATA_PATH.read_text())
    if any(w.get("id") == wave_id for w in waves):
        print(f"Wave id {wave_id} already exists; skipping.")
        return 0

    tags = ["submitted", "needs-review"]
    if country and country != "Needs review":
        tags.append(country)

    waves.append({
        "id": wave_id,
        "name": name,
        "location": region,
        "country": country,
        "region": country if country != "Needs review" else region,
        "sources": [source] if source else [],
        "breakType": "submitted wave — needs review",
        "direction": "needs review",
        "bestSeason": season,
        "skillLevel": "needs review",
        "skillNotes": watch_out or "Submitted through the public review queue; details need review.",
        "whyItBelongs": why,
        "tags": tags,
    })
    DATA_PATH.write_text(json.dumps(waves, ensure_ascii=False, indent=2) + "\n")

    branch = f"wave-submission-{issue_number}-{slugify(name)[:40]}"
    run(["git", "config", "user.name", "github-actions[bot]"])
    run(["git", "config", "user.email", "41898282+github-actions[bot]@users.noreply.github.com"])
    run(["git", "checkout", "-b", branch])
    run(["python3", "-m", "json.tool", str(DATA_PATH)])
    run(["git", "add", str(DATA_PATH)])
    run(["git", "commit", "-m", f"data: add submitted wave {name}"])
    run(["git", "push", "-u", "origin", branch])

    pr_body = (
        f"## Summary\n"
        f"- Adds submitted wave: {name}\n"
        f"- Created from issue #{issue_number}\n\n"
        f"## Review notes\n"
        f"This is an automated draft from a public submission. Please review location, country/region, season, hazards, and whether it fits The Surf Log before merging.\n\n"
        f"Closes #{issue_number}\n"
    )
    run([
        "gh", "pr", "create",
        "--title", f"data: add submitted wave {name}",
        "--body", pr_body,
        "--base", "main",
        "--head", branch,
    ])
    run(["gh", "issue", "comment", str(issue_number), "--body", "Created a review PR for this wave submission."])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
