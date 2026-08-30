# vorpX cannot hook the Steam build — but community DLL injection can (caveat, not a dead end)

**Status:** 🆕 new · **Priority:** medium — a risk/caveat for `ENGINE-DOSSIER.md` §4, not a blocker.

## What was found

On the [vorpX forums' Burnout Paradise thread](https://www.vorpx.com/forums/topic/burnout-paradise/),
vorpX (a general-purpose 3D-driver VR injector) has a profile for Burnout Paradise, but the thread
states: *"Profile will only work with retail game. Steam game crashes with an error (looks like the
game doesn't like third party software to hook into it)."* The profile that does work targets the
older **retail Ultimate Box** edition, not the Steam release, and isn't confirmed against
**Remastered** at all (the thread predates the 2018 remaster / never mentions it).

## Why this isn't necessarily bad news

Taken alone, this could read as "the Steam build actively resists third-party hooking" — a serious
concern for a project whose entire premise is hooking the renderer. But the companion topic on
[community modding tools](2026-08-25-community-modding-tools-and-injection.md) documents an
**actively maintained, currently-working DLL injection toolchain (bo98's mod loader + Detours-based
hooking)** that *does* successfully inject into the Steam `BurnoutPR.exe` — used by a whole
ecosystem of mods including the Free Camera mod. So blanket "the game blocks third-party code" is
false; what's true is narrower: **vorpX specifically** fails against the Steam build, for reasons
undocumented in that thread (could be vorpX's particular hooking method tripping something
Steam-specific, could be outdated/unmaintained vorpX profile logic, could be anything — the thread
gives no diagnostic detail).

## Why it's still worth recording

- It's a concrete data point that **not every injection approach works** against this exe — if this
  project's own injector ever fails mysteriously, "vorpX also failed here, and a from-scratch
  Detours-based loader succeeded" is a useful precedent: prefer the community's proven method (or
  something architecturally similar to it) over assuming a from-scratch approach will trivially work.
- Worth a quick sanity check once hands-on RE starts: does Steam's overlay/anti-cheat-adjacent
  behavior (if any) apply here, or was this just a vorpX-side bug? The dossier's §4 (DRM/anti-debug)
  currently has no entry either way — this is the first signal in either direction.

## Concrete next step

No action needed beyond noting it in §4 as "one third-party injector (vorpX) failed against Steam
build in an undated forum report; community DLL-injection loader (bo98's) succeeds — treat vorpX's
failure as tool-specific, not evidence of blanket anti-injection protection, but keep an eye out for
any DRM/integrity-check behavior during first-look RE."

## Sources

- https://www.vorpx.com/forums/topic/burnout-paradise/
