# BurnoutDecomp now builds a playable native PC game from source (it needs Xbox 360 game data)

**Status:** 🆕 new · **Priority:** high. Follow-up to the 2026-08-25 decomp topic. Since then the project has gone
from "reconstructing source" to a whole-game PC build that is played, measured and released for bug reports. A
source-built Burnout Paradise has no Denuvo and puts the camera and renderer in readable C++, which is a different
project shape from patching `BurnoutPR.exe` from outside.

## What is public

Read online from the repositories' READMEs and docs (GitHub viewer and API), 2026-10-26. Nothing was downloaded.
All `[reported 2026-10-26]`.

- **`BurnoutDecomp/b5-decomp`** (the recovered source; pushed 2026-10-25, very active: DualSense adaptive triggers,
  free-roam fixes, HUD fixes, network CMake all landed 2026-10-24/25). Its docs describe a **PC build that runs**:
  - `PLATFORM_SUPPORT.md`, validation 2026-10-10: shipping MSVC build, **2,848 translation units, zero compile
    failures, successful link**.
  - `tests/PCPerformance.md`, 2026-10-03: a captured **120-second maximum-settings Road Rage** with takedowns and no
    assertions; ~180-192 FPS VSync off on the authors' laptop.
  - `PC_DISPLAY.md`: **starts windowed** unless fullscreen was saved, F11 toggles borderless, draws at the window's
    physical 16:9 pixels; the UI keeps a 1280x720 logical layout. "Changing the game's field of view ... is a
    separate feature" (not done yet).
  - `PC_GRAPHICS.md`: `config.ini` beside `Burnout_PC.exe`; a `[Debug]` section sets **any registered debug-menu
    variable by its menu path** (e.g. bloom scale, LODs, shadow casting from traffic).
  - `DEBUG_MENU.md`: the reconstructed **ARTIST development menu** on Ctrl+Space, plus a command console on the
    backtick key.
  - Controllers through SDL3; renderer support code lives under `src/pc/gcm/renderengine` (the PS3 renderer's
    structure, ported).
- **`BurnoutDecomp/BP-Decomp_Workflow`** (MIT; orchestration). `BUILD.md`: `build doctor` then `build all` produces
  `build/game/Burnout_PC.exe` plus a converted game-data folder. Prerequisites: Visual Studio 2022, Python 3.11+,
  .NET SDK, CMake, Qt6, and, for FFmpeg, either MSYS2 or a prebuilt download.
  - **Input it refuses to do without: a dumped retail Xbox 360 Burnout Paradise folder** (~5,923 files, 3.69 GiB,
    checked to be platform-2 X360 data). The Steam *Remastered* install is only an optional check for a few
    converters.
- No VR work on the decomp was found `[reported 2026-10-26, n=1 look]`.

## Why it matters here

1. **Denuvo goes away** (dossier §12's "single biggest open risk"): the decomp's exe is built from source and has
   none, going by the build recipe `[inferred-static 2026-10-26]`.
2. **Stereo becomes a source change, not an outside patch.** The per-eye camera, the shadow pass that ignored the
   shift, and the headlight pool our proxy edits per eye would all be readable C++ functions. Dossier §11's "nobody
   has reverse engineered `BurnoutPR.exe`'s shaders" stops mattering on this route.
3. **It runs windowed and has a debug menu and an INI for every debug variable**, which covers our window rule and
   gives switches for screen effects and testing.
4. **What it costs:** an Xbox 360 dump of the game (Tefa has a Kreon-flashed drive from Condemned 2, if a 360 disc
   of Burnout Paradise is owned), a heavy toolchain, and a moving target: the project changes daily and is not
   finished. Our D3D11-proxy route on the Remastered build stays valid; this is a second road, not a replacement.
5. The 2008-era console data means the original game's content (no Remastered texture upgrades) `[hypothesis]`.

## Next step it unlocks

Ask Tefa whether a retail Xbox 360 Burnout Paradise disc is owned. If yes, the decomp route deserves a design
decision: build it once on the home PC and see whether its camera code is the place for per-eye rendering.

## Sources

- BurnoutDecomp, b5-decomp: <https://github.com/BurnoutDecomp/b5-decomp> (README, docs/PC_DISPLAY.md, docs/PC_GRAPHICS.md, docs/DEBUG_MENU.md, docs/PLATFORM_SUPPORT.md, tests/PCPerformance.md)
- BurnoutDecomp, BP-Decomp_Workflow: <https://github.com/BurnoutDecomp/BP-Decomp_Workflow> (README, BUILD.md)
