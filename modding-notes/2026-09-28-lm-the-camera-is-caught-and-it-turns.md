# 2026-09-28 — /lm: the world camera is caught live, it turns with the car, and it is a packed matrix

Dev PC, `/lm`, driven unattended: launched through Steam (the EA app hands over in ~10 s when it is already
running), driven to Paradise City by keyboard, closed through its window. Seven launches.

## What the run established

**1. The logger works, after three fixes** (`staging/burnout-paradise-vr/proxy-d3d11-camlog/`, a 32-bit
`d3d11.dll` = the shared logging proxy + `camlog.c` + MinHook). Each fix is recorded because each one is a trap the
next session would walk into:

| run | what happened | fix |
| --- | --- | --- |
| 1 | crashed on the intro video (BEX, `0xc0000005` at `0x00010000`) | the video maps a **texture** with `WRITE_DISCARD`; calling `ID3D11Buffer::GetDesc` on it wrote a 44-byte texture description into a 24-byte struct. Ask `GetType` first |
| 2–4 | no draw call ever reached the hooks | the immediate context's vtable is a **heap table** d3d11 builds at run time (`ctx+4`), and patching it catches nothing; **EA's `igo32.dll` and Steam's `gameoverlayrenderer.dll` are both loaded** in the game |
| 5 | draws arrive | hooks moved onto **the functions themselves** inside `d3d11.dll` (MinHook detours, found through the context's table before anything patches it) |
| 5–6 | the first world draw each second was always a shadow or reflection pass | log only perspective passes that are not 90° cube faces |

`[verified-live 2026-09-28, n=1 launch each]`.

**2. The world shaders the game uses ARE the `SHADERS.BNDL` ones.** 183 vertex shaders are created at start-up;
exactly **121 carry `ViewProjectionModified`**, the bundle's count, with the same offsets (+80 or +96)
`[verified-live 2026-09-28, n=4 launches]`. The reader's hash table (`recon/2026-09-28-lm-camera-logger/
vs-hashes.tsv`) identifies each logged hash.

**3. `viewProjection` is never filled.** All zeros in every logged draw `[verified-live 2026-09-28, n>200 draws]`.
Only `ViewProjectionModified` carries the camera.

**4. Four camera families share the same slot**, told apart by the numbers themselves `[verified-live 2026-09-28]`:

| pass | row 3 | row 0 / row 1 length | meaning |
| --- | --- | --- | --- |
| **main view** | `(1, -0.3, 1, 0)` in the city, `(1, -0.2, 1, 0)` on the car screen | 0.95 / 1.68 in the city; 1.36 / 2.42 on the car screen | perspective, near plane 0.3 m (0.2 m), **no far plane**; 16:9; vertical field of view ~61° driving, ~45° on the car screen |
| sun shadow | `(0.0009, 0.4091, 0, 1)` | small | no perspective (orthographic) |
| car reflections | `(-1.0027, -0.2003, -1, 0)` | 1 / 1 | 90° cube-map faces, axis-aligned, placed at the car |
| car-select scenes | as main view | | |

**5. The packed form is confirmed live.** The reader derived it from the shader code before the run: rows 0 and 1
are clip x and y, row 2 is the forward direction with its depth, row 3 holds four depth numbers
(`z = d·A + B`, `w = d·C + D`). Live, for the main view: **the 4th number of rows 0–2 equals −(row · camera
position) with the camera position = `ViewPosition` from the same buffer**, e.g. row 0: 3109.8 computed vs 3109.67
logged; row 2: 1485.6 vs 1485.54 `[verified-live 2026-09-28, n=2 frames, hand check]`.

**6. It turns with the camera.** Steering left while driving, row 2 (forward) went from `(-0.15, -0.05, -0.99)` to
`(-0.86, 0.01, -0.52)` in 1.3 s, and `ViewPosition` moved with the car `[verified-live 2026-09-28, n=1 turn]`.

**7. ⭐ THE FIRST CAMERA EDIT WORKS.** Same build plus a test shift: numpad 5 moves the main view 1 m along the
camera's own right axis (the reader's `bpr_packed_eye()` on `ViewProjectionModified`, `ViewPosition` moved by the
same vector, re-uploaded before each main-view draw with `UpdateSubresource`). Parked in the city, shift on: **the
whole world moved as one piece with correct depth** — the car, a few metres away, slid well across the picture,
the far sign barely moved, the gantry and fences in between by amounts in between; **switching off returned the
exact picture** (mean pixel difference 1.9 off-vs-off, 22.9 off-vs-on) `[verified-live 2026-09-28, n=1 toggle
pair]`. Pictures: `dev-archive/recon/2026-09-28-lm-camera-logger/first-camera-edit-{off,on-1m-right}.png`.
**One thing did not follow: the car's sun shadow stayed at its old place on screen**, so the shadow is applied by
a pass that reconstructs position from the screen with the unshifted camera `[hypothesis]`. That pass is the next
target. (A first attempt missed the city entirely because a "cube face" filter by row length also caught the
wide driving view; the filter now tests shape — square vs 16:9.)

## What it means for VR

The camera the world is drawn with is found, it is live, and it is one 64-byte value per vertex shader at an offset
the shader itself declares. The per-eye edit is: rewrite rows 0–2's fourth number for the eye's position (the
reader's `bpr_packed_eye()`, 19,296 numerical checks, mutants fail), and move `ViewPosition` by the same offset
(70 of 80 unique world shaders read it). **The game recomputes the whole buffer before almost every draw**
(`UpdateSubresource` ≈ one per draw, ~25,000 per 5 s in menus, 1.8 million per 5 s at the car screen), so the edit
belongs in the `UpdateSubresource` / `Unmap` hook, on the way to the GPU.

## NOT established

- Head tracking and a real per-eye projection (the reader's function does a parallel eye shift with the game's own
  projection).
- Whether the edit survives the shadow and reflection passes untouched (it must skip them; the numbers above tell
  them apart).
- The logger's cost: the game ran noticeably slower through the menus with it installed (dev PC; not measured).
- The keyboard: **W** drives, the **Up arrow does not**, **A** steers `[verified-live 2026-09-28, n=1]`.

## Left installed

`E:\SteamLibrary\steamapps\common\BurnoutPR\d3d11.dll` = the camera logger (hash in
`claude-memory/deployed/DESKTOP-V8GTSIR/burnout-paradise-vr.tsv`). Window: `%LOCALAPPDATA%\Criterion Games\
Burnout Paradise Remastered\config.ini` → 1280×720, `WindowMode=1` (backup `config.ini.bak-2026-09-28`).
