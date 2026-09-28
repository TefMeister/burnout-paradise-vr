# 2026-09-28 — /pd: the world is drawn with `ViewProjectionModified`, and the shaders say so by name

Dev PC, `/pd`, no game launched, nothing run. **The game is installed on the dev PC now**, at
`E:\SteamLibrary\steamapps\common\BurnoutPR\` (Steam manifest, `StateFlags 4`). The old
`D:\...\steamapps\common\BurnoutPR\` folder still holds only our stray `d3d11.dll` + `steam_appid.txt`.
That leftover is the trap the 2026-09-01 entries warned about; the real install is on `E:`.

## What was done

1. **`SHADERS.BNDL` opened with our own reader**, `dev-archive/tools/bnd2_dump.py` (Bundle 2 layout from the
   public Burnout community documentation, the lead `/gr` checked on 2026-09-17). Header: `bnd2`, version 2,
   platform 1, flags `0xF` (zlib per block), **337 resources**. The bundle carries its own debug string table,
   so every resource has its name: **121 `VertexShader` + 121 `PixelShader`** (type `0x12`, the
   `RwShaderProgramBuffer` the wiki names), 86 `Shader` descriptions, a few textures/materials.
   242 DXBC blobs extracted, **reflection intact** (variable names, offsets) `[inferred-static 2026-09-28]`.
2. **Every one of the 121 world vertex shaders keeps the camera in one big `$Globals` at `b0`**, with the
   same five names: `viewProjection`, `ViewProjectionModified`, `ViewPosition`, `worldViewProj`, `world`.
   **The offsets differ from shader to shader**: `viewProjection` sits at +16 or +32, `ViewPosition`
   anywhere from +304 to +3472, `$Globals` from 384 to 3776 bytes (26 distinct layouts)
   `[inferred-static 2026-09-28, n=121]`.
3. **Which matrix actually puts the vertex on screen**, by disassembly (`dxbc-usage.py`, the register feeding
   `SV_Position`/`o0`): **`ViewProjectionModified`, in 121 of 121** `[inferred-static 2026-09-28, n=121]`.
   Worked example, terrain VS (`$Globals` 800 bytes): `o0.x = dp4(r0, cb0[5])`, `o0.y = dp4(r0, cb0[6])` —
   slot 5 is +80, `ViewProjectionModified`. The input `r0` comes from `world` (slots 42–45).
   **`viewProjection` (slots 1–4) and `worldViewProj` (slots 38–41) are not read at all by that shader.**
4. **The other 138 shaders are inside `BurnoutPR.exe` itself** (DXBC readable in the file despite Denuvo,
   because shaders are data). Their constants look nothing like the world set: 93 have a `$Globals` with no
   matrix, 30 have no constant buffer, and **15 have their one matrix at +0** under different names
   (`worldViewProj`, `gWorldViewProjection`, `viewProjectionMatrix`, `gWorldViewProj`, `gViewProjection`).
   No sky or particle shaders are in `SHADERS.BNDL`, `PARTICLES.BUNDLE` or `GLOBALBACKDROPS.BNDL`
   `[inferred-static 2026-09-28]`.

## What it means

- **The vorpX puzzle has a likely answer.** vorpX made only the sky, particles and lights 3D. The exe's own
  shaders (the likely home of those effects) put a conventional matrix at the top of the buffer, which a
  generic "find the view-projection" injector finds. The world shaders keep it at a *different* place in
  every shader, under a name no generic tool looks for, and they ignore the matrix called `viewProjection`
  entirely. A tool that edits `viewProjection` changes nothing the world draws with `[hypothesis]`.
- **The VR route is now concrete.** Our proxy can read each vertex shader's reflection when the game creates
  it (`CreateVertexShader` hands over the same bytecode), note where `ViewProjectionModified` sits in that
  shader's `$Globals`, and rewrite those 64 bytes per eye when `b0` is filled. No scanning, no guessing.
- **What "Modified" means is not known.** Candidates: a jittered projection for anti-aliasing, a reversed
  depth range, or the camera shake applied. The FLAT logger answers it: log `viewProjection` and
  `ViewProjectionModified` from the same buffer and compare.

## NOT established

- That these bundle shaders are the ones the game really binds (it also ships `d3dcompiler_47.dll`).
  A logger that hashes bound vertex shaders against these 121 settles it.
- That the 15 exe shaders are the sky/particles. Nothing names them; it is the best fit to the vorpX report.
- How `b0` is filled (Map/DISCARD, UpdateSubresource, or one big ring). Still the §7 question.

## The next FLAT run, one sentence

Run the logging proxy with a `CreateVertexShader` reflection pass + a `b0` dump for one world draw per frame,
drive, turn: if `ViewProjectionModified` changes as the camera turns and matches `viewProjection` except for a
small offset, that offset is what "Modified" is, and the per-eye edit goes there.
