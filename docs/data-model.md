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
  "tags": ["classic", "soft peeler", "log-friendly"],
  "sources": []
}
```

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

## Source caution

The current seed data is a draft research pass. It should be treated as useful starting material, not sacred truth.

Before public confidence ratings or guide language, add source URLs and/or local surfer confirmation per wave.
