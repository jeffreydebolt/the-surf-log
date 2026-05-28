# Data model

## Wave card fields

```json
{
  "id": "san-onofre-old-mans-dogpatch-california",
  "name": "San Onofre / Old Man’s / Dogpatch",
  "location": "California",
  "region": "California",
  "country": "USA",
  "breakType": "beach-and-point / cobblestone reef peaks",
  "direction": "rights and lefts; soft, slow, slopey",
  "bestSeason": "summer–fall for longboard-friendly S/SW swells; winter can be cleaner/consistent",
  "skillLevel": "beginner-friendly to intermediate",
  "skillNotes": "Classic mellow longboard zone...",
  "whyItBelongs": "One of California’s defining longboard waves...",
  "lat": 33.372,
  "lng": -117.568,
  "coordinatePrecision": "public-break-approx",
  "mapNote": "Approximate public break area, not secret-spot precision",
  "tags": ["classic", "soft peeler", "log-friendly"],
  "sources": []
}
```

## Map fields

Map coordinates are for a travel pin-map feeling, not navigation-grade surf guidance.

Required once map view exists:

- `lat` — decimal latitude
- `lng` — decimal longitude
- `coordinatePrecision` — one of the values below
- `mapNote` — short caveat if location is generalized

### Coordinate precision

- `public-break-approx` — famous/public break; approximate public coordinate is acceptable.
- `town-or-region` — use town/region center where exact break pin would be too specific or not useful.
- `hidden-unmapped` — keep wave in list but do not show a precise map pin.

## Enum targets

Normalize later, but do not over-normalize before the vibe is clear.

### Break type

- point
- reef
- beachbreak
- cobblestone
- pier / sandbar
- mixed

### Direction

- right
- left
- both
- mixed peaks

### Skill level

- beginner-friendly
- beginner-friendly to intermediate
- intermediate
- intermediate to advanced
- advanced / expert-only

### Tags

Tags should support discovery and taste, not just taxonomy:

- soft peeler
- log-friendly
- noseride-friendly
- pilgrimage
- beginner-friendly
- crowded
- public
- mellow
- winter
- south swell
- right point
- beachbreak
- cobblestone
- travel-dream
- long left
- long right
- warm water
- classic longboard

## Source caution

The current seed data is a draft research pass. It should be treated as useful starting material, not sacred truth.

Before public confidence ratings or guide language, add source URLs and/or local surfer confirmation per wave.

Do not add secret-spot precision. If a wave is not clearly public/famous, use `town-or-region` or `hidden-unmapped` instead of a precise pin.
