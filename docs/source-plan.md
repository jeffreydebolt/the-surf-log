# Perfect Little Peelers source plan

Copied from local planning notes on 2026-05-27.

This is source planning material, not final public product copy.

---

# Perfect Little Peelers

## Concept
A lightweight list/community for perfect longboard waves: soft, clean, memorable waves that are made for trimming, gliding, and checking off over a lifetime.

## Vibe
Not Surfline. Not a forecast app. Not performance surfing.

This is a dream list and personal checklist for longboard waves: perfect little peelers, soft pointbreaks, clean runners, and long walls that make people want to travel slowly.


## Inspiration Notes — Daylight Deck

Useful patterns from Daylight’s deck for Peelers:

- Lead with a worldview, not features. Daylight says “make computers bicycles for the mind again.” Peelers needs an equivalent emotional line: a lifetime glide list for people who still believe soft waves matter.
- Frame the problem simply: modern surf discovery is forecast-heavy, performance-heavy, and noisy; there is no soulful checklist of waves worth traveling slowly for.
- Position around “just right.” Peelers should not be Surfline, not a travel agency, not a social network. Just enough: browse, dream, save, check off.
- Use proof/vibe before complexity. Daylight shows launch traction and love. Peelers can start with a beautiful seed list, Jeff’s taste, and small community confirmations.
- Build a wedge that can become an ecosystem. V1 is a static list/checklist; later could become community submissions, rankings, regional guides, surf trip planning, and merch/content.
- Preserve taste as the moat. The defensible thing is not the database alone; it is the curation standard for “perfect little peelers.”

Possible Peelers one-liners:
- “A lifetime glide list for soft waves worth traveling for.”
- “Not a forecast app. A checklist for the waves you’ll remember.”
- “The world’s best little longboard waves, collected.”
- “A dream list for people who still love waist-high peelers.”

## Core Features
1. Browse a list of perfect longboard waves.
2. Community submit a wave.
3. Personal checklist: mark waves as hit / want to hit.
4. Simple login so the checklist persists.
5. Ranking so the list is not just an arbitrary “#27 of 259.”
6. Filter by break type and skill level.
7. Each wave has a simple card:
   - Name
   - Location
   - Country/region
   - Break type: reef / point / beach / cobblestone / mixed
   - Wave direction: right / left / both
   - Best season
   - Skill level: beginner-friendly / intermediate / advanced / expert-only
   - Skill/vibe notes
   - Why it belongs
   - Community submitted by

## Ranking Concept
Rank for “worth planning around,” not objective best wave in the world.

Possible score inputs:
- Community stoke: upvotes / confirmations from longboarders.
- Hit count: how many users have actually checked it off.
- Want-to-hit count: dream-list demand.
- Peeler fit: softness, length, shape, longboard suitability.
- Accessibility: easier regional wins can surface above famous impossible trips.
- Confidence: multiple confirmations beat a single random submission.

This lets a beloved North Carolina wave surface as “worth hitting” even if it is not globally famous.

## Constraints
- Must be easy to remember.
- Must be easy to log in.
- Must be easy to mark a wave off.
- Do not overbuild.
- This is cool and soulful, but should stay lightweight unless it gets traction.

## Possible Names
- Perfect Little Peelers
- Little Peelers
- The Peeler List
- The Glide List
- Long Glide
- Soft Peaks
- Waist High

## Seed List Strategy
Do not seed only from one global/Australia-heavy source.

Use a source mix:
- Global longboard lists: SurferToday, Strike Mission, Castaway Chris, Surf Hungry, SurfSista, World Surfaris.
- US-specific lists: American Surf Magazine, Quiver state pages, Ninefoot Studio, surf travel guides.
- Regional/community lists: California, Hawaii, North Carolina, East Coast, Gulf, Mexico/Central America, Portugal/Europe, Australia/NZ, Indonesia/Sri Lanka.
- Jeff-known waves and lived/travel memory: include waves that listicles miss.
- Community submissions: allow lesser-known regional peelers to compete with famous destination waves.

Initial database target: 200 waves.

Why 200: a 25-40 wave list will feel obviously incomplete. The product needs enough breadth that a surfer can find famous pilgrimage waves, regional gems, and realistic trip targets.

Initial US/Mexico candidates from quick research and Jeff input:
- San Onofre / Old Man's / Dogpatch — California
- Malibu Surfrider — California
- Rincon — California
- Cardiff Reef — California
- Pleasure Point / Cowells — Santa Cruz, California
- Church — San Clemente, California
- C Street — Ventura, California
- Blackies — Newport Beach, California
- Swami's — Encinitas, California
- Doheny — Dana Point, California
- Tourmaline — San Diego, California
- Mondos — near Ventura, California
- Waikiki / Queens / Canoes — Oahu, Hawaii
- Honoli'i — Big Island, Hawaii
- 9 Palms — East Cape, Baja California Sur, Mexico
- La Lancha — near Punta Mita / Puerto Vallarta, Mexico
- Dominican Republic wave Jeff hit — identify later
- North Carolina candidates need a dedicated pass from Quiver/OBX/local sources.

## Tiny First Ship
A searchable static page with a 200-wave JSON seed file, simple regional filters, a fake submit button, and local checklist state. No backend until the vibe is proven.

## Decision Log
- 2026-05-26: Jeff liked “Perfect Little Peelers.” Desired shape: list of perfect longboard waves, community submit, personal checklist of waves hit.

## Seed Wave Card Fields — Research Pass 1

Use these as draft data, not sacred facts. Source-backed first pass is complete for California and NC/East Coast candidates; Hawaii/Mexico still needs a clean second pass because the research worker was interrupted.

### California seed wave cards

- **San Onofre / Old Man’s / Dogpatch — California**
  - Break type: beach-and-point / cobblestone reef peaks
  - Wave direction: rights and lefts; soft, slow, slopey
  - Best season: summer–fall for longboard-friendly S/SW swells; winter can be cleaner/consistent
  - Skill level: beginner-friendly to intermediate
  - Skill/vibe notes: Classic mellow longboard zone; Dogpatch is especially soft/beginner-friendly; crowded but generally forgiving.
  - Why it belongs: One of California’s defining longboard waves: trim, glide, noseride-friendly shoulders.
  - Tags: classic, soft peeler, crowded, pilgrimage, log-friendly, cobblestone, beginner-friendly

- **Malibu Surfrider — California**
  - Break type: right-hand point break
  - Wave direction: long right
  - Best season: summer–early fall S/SW swells
  - Skill level: intermediate to advanced because of crowd/positioning
  - Skill/vibe notes: Technically perfect but extremely crowded and competitive; etiquette is critical.
  - Why it belongs: Iconic long right walls, trim sections, and noseride potential; a global longboard benchmark.
  - Tags: iconic, right point, noseride-friendly, crowded, localized, pilgrimage, advanced-crowd

- **Rincon — California**
  - Break type: right-hand point break
  - Wave direction: long right
  - Best season: winter W/NW swells
  - Skill level: intermediate to advanced
  - Skill/vibe notes: World-class and sectiony; positioning, current, rocks, crowd pressure, and speed matter.
  - Why it belongs: Long point-wave flow with high-line trimming and classic California longboard history.
  - Tags: world-class, right point, winter, crowded, localized, performance-longboard

- **Cardiff Reef — California**
  - Break type: reef break
  - Wave direction: primarily lefts with rights available
  - Best season: winter W/NW swells
  - Skill level: intermediate
  - Skill/vibe notes: Reef and crowd awareness needed; softer on smaller days, more serious with size.
  - Why it belongs: Long, open reef shoulders with trim-friendly walls and strong longboard culture.
  - Tags: reef, left, winter, crowded, rocks, trim wave

- **Pleasure Point / Cowells — Santa Cruz, California**
  - Break type: reef/point setup; Cowells is a sheltered soft point
  - Wave direction: mostly rights at Pleasure Point; Cowells has soft rights/inside rollers
  - Best season: fall–winter; Cowells best when enough west swell wraps in
  - Skill level: beginner-friendly at Cowells; intermediate at Pleasure Point
  - Skill/vibe notes: Cowells is beginner/longboard friendly but crowded; Pleasure Point has more reef, current, and local crowd pressure.
  - Why it belongs: Santa Cruz longboard staple with long rights, playful sections, and historic surf culture.
  - Tags: Santa Cruz, right point, beginner-friendly, reef, crowded, classic longboard

- **Church — San Clemente / Trestles area, California**
  - Break type: beach-and-point / cobblestone reef
  - Wave direction: rights and lefts
  - Best season: summer–fall S/SW swells
  - Skill level: intermediate
  - Skill/vibe notes: Softer than Lowers, but still has rocks and crowd pressure; good for midlengths and longboards.
  - Why it belongs: More forgiving Trestles-area wave with long, lined-up shoulders on south swell.
  - Tags: cobblestone, south swell, soft Trestles, intermediate, crowded, longboard-friendly

- **C Street — Ventura, California**
  - Break type: point/reef and cobblestone-style point setup
  - Wave direction: mostly rights
  - Best season: winter W/NW swells
  - Skill level: intermediate to advanced
  - Skill/vibe notes: Long and rippable but crowded; current, rocks, and stronger winter surf require experience.
  - Why it belongs: Long right walls and multiple takeoff zones make it a strong longboard/midlength point-wave entry.
  - Tags: right point, winter, Ventura, crowded, rocks, performance-longboard

- **Blackies — Newport Beach, California**
  - Break type: beach-and-point / pier-influenced beachbreak
  - Wave direction: mostly lefts with point influence; mixed peaks depending sand
  - Best season: winter W swells
  - Skill level: beginner-friendly to intermediate on small days
  - Skill/vibe notes: Friendly longboard scene but can be crowded; rips and winter punch need respect.
  - Why it belongs: Newport’s classic small-wave longboard hangout with soft, easy rollers when modest.
  - Tags: beachbreak, Newport, small-wave, beginner-friendly, crowded, winter

- **Swami’s — Encinitas, California**
  - Break type: beach-and-reef / right reef
  - Wave direction: right
  - Best season: winter W swells
  - Skill level: intermediate to advanced
  - Skill/vibe notes: Quality wave with rocks and heavy crowd/local presence; not ideal for true beginners.
  - Why it belongs: Long, clean reef rights with excellent trim and turn sections for skilled longboarders.
  - Tags: right reef, Encinitas, winter, crowded, localized, advanced-longboard

- **Doheny — Dana Point, California**
  - Break type: reef / cobblestone-soft point style
  - Wave direction: right-hand reef
  - Best season: summer–early fall S/SW swells
  - Skill level: beginner-friendly to intermediate
  - Skill/vibe notes: Soft, slow, very approachable; crowded with learners and longboards; watch rocks and water quality after rain.
  - Why it belongs: Gentle peelers and forgiving takeoffs make it one of SoCal’s best beginner longboard waves.
  - Tags: beginner-friendly, soft right, south swell, Dana Point, crowded, longboard-school

- **Tourmaline — San Diego, California**
  - Break type: soft reef / beachbreak mix
  - Wave direction: rights and lefts
  - Best season: summer–fall S/SW swells; winter can be consistent
  - Skill level: beginner-friendly to intermediate
  - Skill/vibe notes: Classic mellow longboard and fish wave; crowded but generally less high-performance than nearby reefs.
  - Why it belongs: San Diego’s archetypal longboard playground: soft peaks, easy takeoffs, trim sections.
  - Tags: San Diego, soft reef, beginner-friendly, longboard classic, crowded, mellow

- **Mondos — near Ventura, California**
  - Break type: sandbar / soft point-like beach setup
  - Wave direction: mostly soft rights/lefts depending sandbar
  - Best season: winter W swells
  - Skill level: beginner-friendly to intermediate
  - Skill/vibe notes: Very mellow learning/longboard wave; can be crowded when small and clean.
  - Why it belongs: Soft, slow rollers near Ventura that suit gliding, learners, and relaxed longboard sessions.
  - Tags: beginner-friendly, soft peeler, Ventura, sandbar, winter, mellow

### North Carolina / East Coast candidates

- **Kitty Hawk Pier — North Carolina**
  - Break type: exposed beach / pier break
  - Wave direction: lefts and rights
  - Best season: summer for consistency; fall for cleaner tropical/groundswell windows
  - Skill level: beginner-friendly to intermediate on small days
  - Skill/vibe notes: Public OBX pier zone; can get crowded, with rips and pier hazards.
  - Why it belongs: Reliable, accessible Outer Banks beachbreak with rideable left/right sandbar peaks.
  - Tags: NC, Outer Banks, pier, beachbreak, longboard, public

- **Jennette’s Pier — Nags Head, North Carolina**
  - Break type: beach / pier break
  - Wave direction: lefts and rights
  - Best season: fall–winter, with hurricane/tropical-season pulses
  - Skill level: beginner-friendly to intermediate
  - Skill/vibe notes: Very public, easy-access Nags Head spot; watch pier/current zones.
  - Why it belongs: Recognizable public OBX setup; sandbars can produce forgiving, makeable shoulders.
  - Tags: NC, Outer Banks, Nags Head, pier, beachbreak, longboard, public

- **Kill Devil Hills / Avalon Pier zone — North Carolina**
  - Break type: beach / pier break
  - Wave direction: lefts and rights
  - Best season: fall–winter; small summer windswell can be longboardable
  - Skill level: beginner-friendly to intermediate
  - Skill/vibe notes: Classic public OBX town beach feel; crowds possible near better sandbars and piers.
  - Why it belongs: Realistic longboard seed candidate when sandbars line up.
  - Tags: NC, Outer Banks, Kill Devil Hills, pier, beachbreak, longboard, public

- **S-Turns / Rodanthe — North Carolina**
  - Break type: exposed beachbreak / sandbar
  - Wave direction: lefts and rights
  - Best season: fall–winter; clean hurricane swell windows
  - Skill level: intermediate
  - Skill/vibe notes: More exposed OBX energy; currents, shifting bars, and crowd pressure when good.
  - Why it belongs: Publicly known Hatteras Island sandbar zone with peeling potential when small-to-medium and organized.
  - Tags: NC, Outer Banks, Hatteras Island, sandbar, beachbreak, peeler, intermediate

- **Avon Pier — North Carolina**
  - Break type: beach / pier break
  - Wave direction: lefts and rights
  - Best season: fall–winter; late-summer tropical swell windows
  - Skill level: beginner-friendly to intermediate on smaller days
  - Skill/vibe notes: Public pier zone; more manageable than heavier Hatteras spots when small, but still exposed to OBX currents.
  - Why it belongs: Known Hatteras Island pier setup that can offer long, softer sandbar shoulders.
  - Tags: NC, Outer Banks, Avon, pier, beachbreak, longboard

- **Old Lighthouse / Buxton — North Carolina**
  - Break type: exposed beachbreak / cape sandbar
  - Wave direction: lefts and rights
  - Best season: fall–winter
  - Skill level: intermediate; advanced when bigger
  - Skill/vibe notes: Not a mellow beginner spot with size; small, clean, lined-up days can peel.
  - Why it belongs: One of NC’s iconic public surf zones with strong sandbar potential.
  - Tags: NC, Outer Banks, Buxton, Cape Hatteras, sandbar, iconic, intermediate

- **Frisco Pier / Frisco — North Carolina**
  - Break type: beach / pier break, somewhat more sheltered depending wind/swell
  - Wave direction: lefts and rights
  - Best season: fall–winter
  - Skill level: beginner-friendly to intermediate on small days
  - Skill/vibe notes: Public Hatteras south-facing zone; watch shifting sand and structure/current context.
  - Why it belongs: Often a mellower Hatteras option for clean, smaller longboard runners.
  - Tags: NC, Outer Banks, Frisco, Hatteras, pier, sheltered-option, longboard

- **Wrightsville Beach / Oceanic–Crystal–Mercer pier zones — North Carolina**
  - Break type: beachbreak with pier/sandbar influence
  - Wave direction: mixed peaks; often lefts/rights depending bar
  - Best season: winter and fall
  - Skill level: beginner-friendly to intermediate
  - Skill/vibe notes: Highly accessible surf-town vibe, popular/crowded, with lots of learners and longboarders.
  - Why it belongs: One of the obvious southern NC longboard seeds: public, consistent enough, established surf community.
  - Tags: NC, Wrightsville Beach, beachbreak, pier, longboard, learner-friendly, crowded

- **Masonboro Island / Masonboro Inlet — North Carolina**
  - Break type: beachbreak / inlet-influenced sandbars
  - Wave direction: lefts and rights
  - Best season: fall–winter
  - Skill level: intermediate due to access/logistics
  - Skill/vibe notes: Access is less casual than town beaches; boat/kayak/paddle logistics and changing inlet currents matter.
  - Why it belongs: Publicly listed NC beachbreak with right/left waves and less dense crowd than central Wrightsville.
  - Tags: NC, Masonboro, inlet, sandbar, adventure-access, longboard

- **Surf City Pier / Topsail Island — North Carolina**
  - Break type: beach / pier break
  - Wave direction: lefts and rights
  - Best season: fall–winter; small summer windswells for logging
  - Skill level: beginner-friendly to intermediate
  - Skill/vibe notes: Public pier-town setup; family beach vibe, can get busy around the pier.
  - Why it belongs: Realistic southern/central NC longboard card: softer beachbreak peaks, public access, small-wave days.
  - Tags: NC, Topsail, Surf City, pier, beachbreak, longboard, public

- **The Washout, Folly Beach — South Carolina**
  - Break type: beachbreak
  - Wave direction: lefts and rights
  - Best season: fall–winter; tropical season can produce quality windows
  - Skill level: beginner-friendly to intermediate on small days; intermediate when bigger/crowded
  - Skill/vibe notes: Public Charleston-area surf zone; busy and variable.
  - Why it belongs: Strong nearby East Coast addition with friendly sandbar shoulders in clean smaller surf.
  - Tags: South Carolina, Folly Beach, Washout, beachbreak, longboard, public

- **Cocoa Beach Pier / Cocoa Beach — Florida**
  - Break type: beach / pier sandbar break
  - Wave direction: lefts and rights
  - Best season: winter and hurricane season; summer often small but longboardable
  - Skill level: beginner-friendly to intermediate
  - Skill/vibe notes: Very public, established surf/longboard/learner scene; crowds common but approachable.
  - Why it belongs: Archetypal East Coast longboard-friendly town wave: soft, accessible, public, small-wave famous.
  - Tags: Florida, Cocoa Beach, pier, beachbreak, longboard, learner-friendly, East Coast classic

### Source URLs from research pass 1

- https://www.surf-forecast.com/breaks/San-Onofre
- https://www.surf-forecast.com/breaks/Malibu_1
- https://www.surf-forecast.com/breaks/Rincon-Point
- https://www.surf-forecast.com/breaks/Cardiff-Reef
- https://www.surf-forecast.com/breaks/Pleasure-Point-Second-Peak
- https://www.surf-forecast.com/breaks/Cowells-Cove
- https://www.surf-forecast.com/breaks/Church
- https://www.surf-forecast.com/breaks/Ventura-Overhead
- https://www.surf-forecast.com/breaks/San-Buenaventura-State-Beach
- https://www.surf-forecast.com/breaks/Blackies
- https://www.surf-forecast.com/breaks/Swamis
- https://www.surf-forecast.com/breaks/Doheney-Beach
- https://www.surf-forecast.com/breaks/Tourmaline
- https://www.surf-forecast.com/breaks/Mondos
- https://www.surf-forecast.com/breaks/Kitty-Hawk-Pier
- https://www.surf-forecast.com/breaks/Wrightsville-Beach
- https://www.surf-forecast.com/breaks/S-Turns/forecasts/latest/six_day
- https://www.surfing-waves.com/atlas/north_america/usa/east_coast/north_carolina.html
- https://www.surfing-waves.com/atlas/north_america/usa/east_coast/south_carolina.html
- https://www.surfing-waves.com/atlas/north_america/usa/east_coast/florida.html

## V1 Build Checklist

### Product decisions
- [ ] Pick working name for repo/app: `perfect-little-peelers` unless Jeff changes it.
- [ ] Decide whether V1 is public browse-only plus local checklist, or login-backed checklist. Recommendation: public browse + local checklist first.
- [ ] Decide the first geography scope. Recommendation: seed ~40-60 waves first, not 200, then expand.
- [ ] Decide whether to show exact map pins or general regions. Recommendation: public/famous waves only; no secret spot precision.

### Data model
- [ ] Create `waves.json` with fields: id, name, location, region, country, breakType, direction, bestSeason, skillLevel, skillNotes, whyItBelongs, tags, sources.
- [ ] Normalize enums for break type, direction, skill level, season, and tags.
- [ ] Add initial California seed records from research pass 1.
- [ ] Add initial NC/East Coast seed records from research pass 1.
- [ ] Complete Hawaii/Mexico research pass and add Waikiki/Queens/Canoes, Honoli’i, 9 Palms, La Lancha.
- [ ] Add Jeff-known Dominican Republic wave once identified.

### V1 interface
- [ ] Build a dead-simple static page: title, vibe sentence, search, filters, wave cards.
- [ ] Filters: region, country, break type, skill level, direction, tags.
- [ ] Card actions: “Want to hit” and “Hit it”.
- [ ] Store checklist state in localStorage for V1.
- [ ] Add “submit a wave” fake CTA or form that saves locally / opens email later.

### Quality / vibe
- [ ] Write short copy so it feels soulful, not like Surfline.
- [ ] Add “not a forecast app” disclaimer.
- [ ] Add safety/conditions disclaimer: skill labels are general, not live safety advice.
- [ ] Make mobile layout excellent first.

### Shipping
- [ ] Create GitHub repo.
- [ ] Commit plan and seed data.
- [ ] Deploy static V1 to Vercel/Netlify/GitHub Pages.
- [ ] Share private link with 3-5 surf friends/clients.
- [ ] Collect missing-wave suggestions and confusion points.
- [ ] Only add login/backend after people actually use the checklist.
