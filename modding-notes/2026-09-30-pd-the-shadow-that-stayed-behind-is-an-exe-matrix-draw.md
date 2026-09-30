# 2026-09-30 (`/pd`, dev PC): the shadow that stayed behind is not the sun shadow

**The game was not launched, and nothing here has been run.** Everything below comes from the shader files
on disk, the two pictures from run 8 and a numerical test.

## The question

In run 8 (2026-09-28) the numpad-5 test shift moved the whole world 1 m to the right, except a dark patch
under the car, which stayed at its old screen place. The board guessed that a screen-space shadow pass was
rebuilding world position from the screen with the unshifted camera.

## What the files say

1. **The sun shadow is looked up by WORLD position, so it cannot stay behind.** Every world pixel shader in
   `SHADERS.BNDL` that reads `ShadowMap_WorldToLight` (the three cascades, `$Globals` slots 9-20 in the
   2928-byte layout) multiplies it by an interpolant that the matching vertex shader fills with
   the world position (for example `Specular_Greyscale_Singlesided`: `o4 = world * v`, and the PS does
   `dp4` of `v4` against slots 9-20). The cascade choice uses the view depth in `v3.w`, which a 1 m sideways
   shift barely changes. **No world pixel shader reads `viewProjection` or `ViewProjectionModified` at all**
   (slots 1-8 are unread in every layout, `dxbc-usage.py`) `[inferred-static 2026-09-30, n=121 PS]`.
2. **14 vertex shaders compiled into `BurnoutPR.exe` carry their own full camera matrix at `$Globals +0`**, under
   the names `worldViewProj` (8), `gWorldViewProjection` (3), `gWorldViewProj`, `gViewProjection`
   (instanced, with `gaWorldTransforms[32]`) and `viewProjectionMatrix`; four of them also carry their own
   eye position (`gEyeLocation`, `gEyePosPlusDepthBias`, `cameraPositionPlusBrightness`,
   `ViewPositionAndSkyScale`) `[inferred-static 2026-09-30, n=138 exe shaders]`. The test shift edits only
   `ViewProjectionModified`, so every one of these is still drawn from the true camera. (A 15th shader with a matrix at +0 is the headlight pixel shader, below.)
3. **The pictures fit that.** In `first-camera-edit-on-1m-right.png` the patch is a soft, car-shaped dark
   blob sitting exactly where the car was in the unshifted picture. That is a separately drawn object
   (a blob or contact shadow under the car), not a lit surface `[hypothesis]`: which of the 14 draws it is
   has not been identified. The strongest candidate is exe VS `0037` (`gWorldViewProjection`,
   `gUvBlendAlphaUnpack`, `gDepthFadeUvZOffset/Scale`): a textured quad that also outputs its own screen
   position and depth to fade against the scene depth.

## What was built

- **`bpr_plain_eye()`** (`staging/burnout-paradise-vr/stereo-math/`): given the main view's packed matrix,
  its eye version and a draw's own full matrix `M`, it works out the object's world transform
  `W = M * V_centre^-1`. If `W` is a proper (affine) transform, the draw belongs to the main view and is
  rebuilt as `W * V_eye`; otherwise (HUD, cube face, sun shadow) it is left alone.
  Test: **5,941 new checks, 0 failures, worst error 0.05 of the tolerance**; the HUD, a cube face and the
  sun-shadow matrix are refused for all six test cameras; the "accept but do not shift" and "shift the
  wrong way" mutants both fail `[verified-numerically 2026-09-30, n=5941]`.
  One trap found on the way: assuming `W`'s last column is exactly (0,0,0,1) and dropping the rounding
  cost 1e-4 of the screen, 10,000 times the game's own error, at city coordinates. Keeping all four terms
  fixed it.
- **The proxy** now applies it with the numpad-5 shift on, moves the matching eye position by the same
  1 m, and logs the first accept and the first reject of every exe shader by hash. The 5-second stats line
  gains `exe-matrix draws shifted N / left N`. Built `[compile-verified 2026-09-30]`, installed on the dev
  PC (`d3d11.dll`, sha256 `ac1acd917c8b...`; the previous build kept beside it as
  `d3d11.dll.backup-2026-09-30-before-exe-matrix-shift`).

## Everything else that reads the camera outside `ViewProjectionModified`

| What | Where | Per eye |
| --- | --- | --- |
| the 14 exe full-matrix draws (above) | exe VS | **now shifted**, when they belong to the main view |
| their eye positions | exe VS | **now shifted** by the same offset |
| headlight pool: `g_clipToHeadlight` (screen position + depth to headlight space) | exe PS `0048` | needs the eye's clip-to-centre-clip step in front of it; not done (night only) |
| camera motion blur: `BlurMatrixXXX/YYY/ZZZ/WWW` | exe post PS | built for the centre eye; turn motion blur off in VR, as Mad Max does `[hypothesis]` |
| depth fade (`gDepthConversion`), bloom, depth of field, FXAA, vignette | exe PS | screen-space, per eye as they are |
| sun shadow map (`ShadowMap_WorldToLight`) | bundle PS | world-space, correct as it is |

## Not established

- Which exe draw the blob is. The next run's log names every exe shader that followed the main view.
- That the proxy's "belongs to the main view" test holds on real game data; it is proved only on made-up
  cameras and objects. If the blob still stays behind **and** the log shows no exe shader accepted, the
  test is refusing real main-view draws (a tolerance problem, not a wrong idea). If the blob stays behind
  while exe shaders ARE shifted, the blob is drawn some other way and this hypothesis is wrong.

## The one test

Flat, parked in the city, as in run 8: numpad 5 on and off, one picture each. **The blob moves with the car
= fixed.** Then read `burnout_camlog.txt` for the `exe-matrix VS hash` lines.
