# 2026-10-01 (`/lm`, dev PC, driven by Claude): the car's dark blob now moves with the car

*Still camera, parked in the city; the game launched, driven and closed by Claude.*

## The test

The `d3d11.dll` built by `/pd` on 2026-09-30 (`ac1acd917c8b`) also shifts the exe's own full-matrix draws
(`bpr_plain_eye`). Parked as in run 8, numpad 5 on and off, one picture each.

## What was seen `[verified-live 2026-10-01, n=1 toggle]`

- **The blob is fixed.** With the 1 m shift on, the car and world moved together and the place where the dark
  car-shaped blob used to stay behind (right of the car) shows clean road with a painted arrow it had been covering.
- **Which draws followed the main view:** the log names four exe vertex shaders accepted as main-view draws and
  shifted (`93f9fda4` and `82d755c5` with an eye position at +64; `88956c54`, `c2b9abd0` without), and
  `93f9fda4` also seen in another view, where it was correctly left alone. 603 such draws shifted and 402 left alone
  in the 5 seconds of the toggle. So the "belongs to the main view" test works on real game data, not only in the
  synthetic test.
- The blob draw is one of those four `[hypothesis]` as to which (not separated).

## Also done

- **Music off**: pause (Esc) → F2 to "Under the Hood" → Audio Options → Music Volume to 0 → Backspace → Save
  Changes: Yes (Enter). ⚠️ In these menus **Backspace is Back**; Esc only works on some pages, and an Esc on the
  Save Changes box answers **No** (the first attempt did not stick). Re-opened to confirm 0 `[verified-live 2026-10-01]`.
- The reader worked out and tested the headlight-pool correction (`bpr_headlight_eye`, 6,269 checks, 0 failures),
  in staging; folded from its inbox note into the dossier.

Pictures and log lines: `dev-archive/recon/2026-10-01-lm-blob-fixed/`.
