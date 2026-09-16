# vorpX hooks the Remaster; its Geometry 3D misses the world pass — narrows the §4 caveat, first data point for §6
Supersedes: ENGINE-DOSSIER.md §4 "vorpX failed against the Steam build" caveat (from topic 2026-08-25-vorpx-steam-injection-rejection.md)

**From:** `/gr` estate sweep, 2026-09-11 (CHECK-IN). Project is paused; this is for the resume.
**Topic:** `external-research/topics/2026-09-11-vorpx-does-hook-the-remaster-but-its-geometry-3d-misses-the-world.md`

## The dossier line this corrects

§4 records, from the 2026-08-25 vorpX topic, that vorpX failed to hook the Steam build — treated as
a possible sign of anti-injection behaviour. A second vorpX thread (2019-12-25) shows vorpX **did
hook Burnout Paradise Remastered** via its alternative hook method `[reported 2026-09-11]`. The crash
report was the **2008 Ultimate Box** Steam build, a different exe. So the §4 caveat should say:
*vorpX hooks the Remaster; the 2008 Steam build crashed on hook; neither is evidence about
`BurnoutPR.exe` resisting injection.*

## What it adds to §6 / §7 (currently empty)

With a D3D11 profile, vorpX's Geometry 3D stereoised **only particles, lights and the skybox**; the
world stayed flat. Suggested one-line entry under §6: *a generic cbuffer-matching stereo injector
catches the sky/particle/light passes but not the world pass, so the world's projection is probably
not delivered as a conventional VP in a cbuffer vorpX recognises — per-draw MVP or non-standard
layout suspected `[hypothesis]`; first 3Dmigoto dump should compare the two groups' VS cbuffers.*

## Resume conditions, for the board (not the dossier)

Ultimate Box (Steam 24740) is delisted at the publisher's request (community-dated 2020-06-04); the
Remaster's Steam page still requires EA activation and the Origin/EA client `[reported 2026-09-11]`.
Both resume conditions are unchanged/closed.
