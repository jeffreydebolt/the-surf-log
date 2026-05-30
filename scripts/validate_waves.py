#!/usr/bin/env python3
"""Validate The Surf Log seed data.

The goal is lightweight repo hygiene: catch malformed public wave data before
it ships, without forcing premature taxonomy normalization.
"""

from __future__ import annotations

import json
import re
import sys
from collections import Counter
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_DATA_PATH = ROOT / "data" / "waves.seed.json"

REQUIRED_FIELDS = (
    "id",
    "name",
    "location",
    "country",
    "region",
    "sources",
    "breakType",
    "direction",
    "bestSeason",
    "skillLevel",
    "skillNotes",
    "whyItBelongs",
    "tags",
)

COORDINATE_PRECISIONS = {
    "public-break-approx",
    "town-or-region",
    "hidden-unmapped",
}

ID_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")


def fail(errors: list[str], message: str) -> None:
    errors.append(message)


def require_nonempty_string(errors: list[str], wave: dict[str, Any], index: int, field: str) -> None:
    value = wave.get(field)
    if not isinstance(value, str) or not value.strip():
        fail(errors, f"wave[{index}] {wave.get('id', '<missing id>')}: {field} must be a non-empty string")


def validate_sources(errors: list[str], wave: dict[str, Any], index: int) -> None:
    sources = wave.get("sources")
    if not isinstance(sources, list):
        fail(errors, f"wave[{index}] {wave.get('id', '<missing id>')}: sources must be an array")
        return
    for source_index, source in enumerate(sources):
        if not isinstance(source, str) or not source.strip():
            fail(errors, f"wave[{index}] {wave.get('id')}: sources[{source_index}] must be a non-empty string")
        elif not re.match(r"^https?://", source):
            fail(errors, f"wave[{index}] {wave.get('id')}: sources[{source_index}] must start with http:// or https://")


def validate_tags(errors: list[str], wave: dict[str, Any], index: int) -> None:
    tags = wave.get("tags")
    if not isinstance(tags, list) or not tags:
        fail(errors, f"wave[{index}] {wave.get('id', '<missing id>')}: tags must be a non-empty array")
        return
    for tag_index, tag in enumerate(tags):
        if not isinstance(tag, str) or not tag.strip():
            fail(errors, f"wave[{index}] {wave.get('id')}: tags[{tag_index}] must be a non-empty string")


def validate_coordinates(errors: list[str], wave: dict[str, Any], index: int) -> None:
    wave_id = wave.get("id", "<missing id>")
    has_lat = "lat" in wave
    has_lng = "lng" in wave
    precision = wave.get("coordinatePrecision")
    has_precision = "coordinatePrecision" in wave

    if has_lat != has_lng:
        fail(errors, f"wave[{index}] {wave_id}: lat and lng must be provided together")

    if has_lat and has_lng:
        lat = wave.get("lat")
        lng = wave.get("lng")
        if not isinstance(lat, (int, float)) or isinstance(lat, bool) or not -90 <= lat <= 90:
            fail(errors, f"wave[{index}] {wave_id}: lat must be a number between -90 and 90")
        if not isinstance(lng, (int, float)) or isinstance(lng, bool) or not -180 <= lng <= 180:
            fail(errors, f"wave[{index}] {wave_id}: lng must be a number between -180 and 180")
        if not has_precision:
            fail(errors, f"wave[{index}] {wave_id}: coordinatePrecision is required when lat/lng are present")

    if has_precision:
        if precision not in COORDINATE_PRECISIONS:
            fail(errors, f"wave[{index}] {wave_id}: coordinatePrecision must be one of {sorted(COORDINATE_PRECISIONS)}")
        if precision == "hidden-unmapped" and (has_lat or has_lng):
            fail(errors, f"wave[{index}] {wave_id}: hidden-unmapped waves must not include lat/lng")
        if precision in {"public-break-approx", "town-or-region"} and not (has_lat and has_lng):
            fail(errors, f"wave[{index}] {wave_id}: {precision} requires lat/lng")

    if (has_lat or has_lng or has_precision) and "mapNote" not in wave:
        fail(errors, f"wave[{index}] {wave_id}: mapNote is required when map fields are present")
    if "mapNote" in wave and (not isinstance(wave.get("mapNote"), str) or not wave.get("mapNote", "").strip()):
        fail(errors, f"wave[{index}] {wave_id}: mapNote must be a non-empty string when present")


def validate(data_path: Path = DEFAULT_DATA_PATH) -> tuple[list[str], dict[str, Any]]:
    errors: list[str] = []
    try:
        waves = json.loads(data_path.read_text())
    except json.JSONDecodeError as exc:
        return [f"{data_path}: invalid JSON: {exc}"], {}

    if not isinstance(waves, list):
        return [f"{data_path}: root value must be an array"], {}

    ids: list[str] = []
    for index, wave in enumerate(waves):
        if not isinstance(wave, dict):
            fail(errors, f"wave[{index}]: record must be an object")
            continue

        missing = [field for field in REQUIRED_FIELDS if field not in wave]
        if missing:
            fail(errors, f"wave[{index}] {wave.get('id', '<missing id>')}: missing required fields: {', '.join(missing)}")

        wave_id = wave.get("id")
        if isinstance(wave_id, str):
            ids.append(wave_id)
            if not ID_RE.match(wave_id):
                fail(errors, f"wave[{index}] {wave_id}: id must be lowercase kebab-case")
        else:
            fail(errors, f"wave[{index}]: id must be a string")

        for field in REQUIRED_FIELDS:
            if field in {"sources", "tags", "id"} or field not in wave:
                continue
            require_nonempty_string(errors, wave, index, field)

        validate_sources(errors, wave, index)
        validate_tags(errors, wave, index)
        validate_coordinates(errors, wave, index)

    duplicate_ids = sorted([wave_id for wave_id, count in Counter(ids).items() if count > 1])
    for wave_id in duplicate_ids:
        fail(errors, f"duplicate id: {wave_id}")

    summary = {
        "waves": len(waves),
        "countries": len({w.get("country") for w in waves if isinstance(w, dict) and w.get("country")}),
        "regions": len({w.get("region") for w in waves if isinstance(w, dict) and w.get("region")}),
        "with_sources": sum(1 for w in waves if isinstance(w, dict) and w.get("sources")),
        "with_coordinates": sum(1 for w in waves if isinstance(w, dict) and "lat" in w and "lng" in w),
    }
    return errors, summary


def main() -> int:
    data_path = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_DATA_PATH
    errors, summary = validate(data_path)
    if errors:
        print("Wave seed validation failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1
    print(json.dumps({"ok": True, **summary}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
