# /gr 2026-09-29: sibling lead for "the shadow pass that ignores the shift"

Board `[PD]` row: with the 1 m test shift, everything moved except the car's sun shadow, suspected to be a
screen-space pass that rebuilds world position from screen position + depth.

The Alice project hit the same class of fault on 2026-09-29 (UE3 ScreenToShadowMatrix) and has a public lead on how
such passes are fed: in the Unreal lineage the input is (screen x·w, y·w, w, 1), a screen position times depth, and
the matrix carries a fix-up plus the camera's inverse view-projection `[reported]`. The general point transfers
`[hypothesis]`: a pass like that bakes in the UNEDITED camera, so it must get the edited camera's inverse (or a
correction built in the same screen-times-depth space), not a view-space nudge. When searching Burnout's shaders,
look for a 4x4 multiplied against `(uv·depth, depth, 1)` or `(uv, depth, 1)`.
See `alice-madness-returns-vr/external-research/topics/2026-09-29-screen-to-shadow-takes-screen-position-times-depth.md`.
