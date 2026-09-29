# A vorpX profile for the 2008 game also had to fix Burnout's shadows under a per-eye camera shift

**Found:** 2026-09-29, `/gr` estate sweep (CHECK-IN).
**Relates to:** board `[PD]` ⭐⭐⭐ "find the shadow pass that ignores the shift".

## What was found

Brian Koponen's guide "How to Run Burnout Paradise in VR Using VorpX" (dated 2020-09-01) says he
made a vorpX cloud profile, named in search listings as *Burnout Paradise Ultimate Box (G3D w/
Shadows)*, specifically "to fix the broken shadows that normally appear in Geometry 3D mode", and
that with it the shadows render correctly in 3D `[reported]`. vorpX's Geometry 3D mode renders
each eye by moving the camera, which is the same kind of change as our 1 m test shift.

The guide gives **no technical detail** of what the profile changed (no shader names, no method),
and it targets the 2008 *Ultimate Box* (Direct3D 9). The Remaster we mod is Direct3D 11 with
different shaders, so nothing here carries over directly.

## Why it matters for this project

Only as corroboration: an independent tool hit the same symptom we saw — the car's sun shadow
stays put while everything else moves — on the same game's older build, and it was fixable inside
a per-game profile, which usually means a per-shader fix rather than an engine rewrite
`[hypothesis]`. It supports the board's reading that one shadow shader rebuilds world position from
the unshifted camera, and that finding and correcting that one shader is the right-sized job.

## Next step

None from this page. The board row stands as written (find the pixel shader that turns screen
position and depth back into world position for the shadow lookup).

## Source

- Brian Koponen, "How to Run Burnout Paradise in VR Using VorpX" —
  https://www.briankoponen.com/burnout-paradise-vr-vorpx/
