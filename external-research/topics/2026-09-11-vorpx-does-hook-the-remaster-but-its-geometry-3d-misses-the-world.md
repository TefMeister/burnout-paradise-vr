# vorpX *does* hook the Remastered exe — and its Geometry 3D stereoises only particles, lights and sky, never the world

**Status:** 🆕 new · **Priority:** medium — it narrows the 2026-08-25 vorpX caveat (which was about the
*original* Ultimate Box on Steam) and gives dossier §6/§7 their first public data point about how the
Remaster's world pass takes its projection. The project is paused; this is recorded for the resume.

**Supersedes:** the framing in `2026-08-25-vorpx-steam-injection-rejection.md` that vorpX's failure
is an *injection* failure and "isn't confirmed against Remastered at all". It is now confirmed
against Remastered, and the failure there is *stereo coverage*, not hooking.

## What was found

A second vorpX forum thread, dated 2019-12-25, is specifically about **Burnout Paradise Remastered**
`[reported 2026-09-11]`:

- The poster (0li0li) got vorpX to **hook the Remastered executable** using vorpX's *alternative
  hook* method and could build a profile on it. The store build is not stated (Steam vs Origin), so
  the 2026-08-25 "Steam Ultimate Box crashes on hook" report is not contradicted — it is a
  different exe.
- The working cloud profile for the **original** game (D3D9) does not carry over; RJK_ (the profile
  author for the original) explains that a D3D9 profile "will not provide 3D" for a D3D11 game and
  that "editing shaders will very likely not be enough".
- With a fresh D3D11 profile, **Geometry 3D stereoised only particle effects, lights and the
  skybox**. The world — road, buildings, cars — stayed flat. No official profile was ever made; the
  advice was to submit it to vorpX's wishlist.

## Why it matters for THIS project

1. **It is the first public evidence about §6 ("how the world transform reaches the GPU").** vorpX's
   Geometry 3D works by recognising a conventional view-projection in a constant buffer and
   re-issuing draws per eye. When it catches sky/particles/lights but not the world, the usual
   reading is that **the world pass does not present its projection in the shape vorpX's generic
   D3D11 matcher expects** — e.g. a pre-multiplied per-draw MVP, a projection folded into a
   non-standard layout, or a matrix delivered outside the cbuffer path vorpX watches
   `[hypothesis]`. The passes that *did* work are the ones that typically use a plain camera VP.
   That is exactly the split 3Dmigoto reflection (§6 tooling plan) would confirm or refute first.
2. **It reclassifies the 2026-08-25 caveat.** Injection into the Remaster is *not* blocked for vorpX;
   only the older Steam Ultimate Box crashed on hook. Dossier §4's "vorpX failed against the Steam
   build" line should read: *vorpX hooks the Remaster; its stereo misses the world pass; the crash
   report was the 2008 Steam build.*
3. **It is a bound on the easy route.** A generic geometry injector could not deliver a stereo world
   here, so "just profile it in vorpX" is not a fallback for this game — the project's own
   cbuffer-level work is required, as the dossier already assumed.

## Also confirmed this pass (resume conditions, not technical)

- **Burnout Paradise: The Ultimate Box (Steam app 24740) is delisted** — the Steam page carries the
  publisher-request "no longer available for sale" notice; the community dates it to 2020-06-04,
  the day the Remaster launched on Steam `[reported 2026-09-11]`. Existing owners keep it; new
  buyers cannot. The INDEX's `[hypothesis]` on this is now settled: **that resume condition is
  closed** unless a key turns up second-hand, which this lane does not pursue.
- **The Remaster's Steam page still says** "Incorporates 3rd-party DRM: EA on-line activation and
  Origin client software installation and background use required" and "Requires 3rd-Party
  Account: EA Account" `[reported 2026-09-11]`. The EA gate is unchanged.

## Sources

- vorpX forums — "I would love some clarification about making a remaster work" (0li0li, RJK_,
  2019-12-25): https://www.vorpx.com/forums/topic/i-would-love-some-clarification-about-making-a-remaster-work-2/
- vorpX forums — "Burnout Paradise" (RJK_, 2019-06-12, Ultimate Box profile; Steam build crash
  note): https://www.vorpx.com/forums/topic/burnout-paradise/
- Steam store — Burnout Paradise Remastered (DRM notice): https://store.steampowered.com/app/1238080/
- Steam store — Burnout Paradise: The Ultimate Box (delisting notice): https://store.steampowered.com/app/24740/
- Delisted Games — Burnout Paradise (delisting date; page 403s to automated fetch, date taken from
  the search summary and the Steam community thread "Original Burnout Paradise removed?"):
  https://delistedgames.com/burnout-paradise/

## Next step

None until the project resumes. On resume, the first 3Dmigoto dump should sort draws into "vorpX
would have caught this" (sky, particles, lights) and "it would not" (world) and compare their
vertex-shader constant-buffer layouts — that comparison is the cheapest test of the hypothesis above.
