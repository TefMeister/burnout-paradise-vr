# 2026-08-25 — Project kickoff

Burnout Paradise VR started today, one of five game projects seeded together
(Burnout Paradise, Mad Max, Prince of Persia 2008, Alice: Madness Returns,
Alan Wake). Of the five, this is the user's favorite and the one hands-on
reverse-engineering starts on first.

**Game:** Burnout Paradise Remastered (2018 remaster of the 2008 original),
developed by Criterion Games (original) and Stellar Entertainment
(remaster), published by Electronic Arts. Steam build, `BurnoutPR.exe`.

**Engine:** Criterion's own proprietary in-house engine — not licensed
RenderWare, despite Criterion's earlier RenderWare-era work; a distinct,
later in-house engine. The install ships `d3dcompiler_47.dll`, suggesting a
Direct3D 11 renderer, but this is unconfirmed until live inspection.

**Status:** repos established (this is the six-repo standard's first entry
for this project). Nothing has been reverse-engineered yet. Next step is the
"first look" phase: identify the renderer API in use, find the injection
foothold, and start locating how the camera/projection reaches the GPU —
per the playbook in `burnout-paradise-vr-engine-research`.

**Special note for this project:** driving games carry a higher motion-
sickness risk than the walking-sim/shooter conversions in the other
projects — comfort options should be treated as a first-class design
concern, not an afterthought, once the mod reaches a testable state.
