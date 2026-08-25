# Burnout Paradise Remastered has an active PC modding community with a working DLL-injection stack

**Status:** 🆕 new · **Priority:** high — directly informs `ENGINE-DOSSIER.md` §4 (injection
foothold) and §6 (camera).

## What exists

The Steam PC version of Burnout Paradise Remastered (our exact target, `BurnoutPR.exe`) has an
established, currently-maintained modding scene, centered on a community index repo
([RomulusMirauta/Burnout-Paradise-Remastered](https://github.com/RomulusMirauta/Burnout-Paradise-Remastered))
and a Discord ("Burnout Hints") used for support.

**Injection stack (two layers):**
1. **[bo98's "BPR Modder"](https://bpr.bo98.uk/)** — a mod-manager/installer that installs "bo98's
   Mod Loader" and copies built mod DLLs into a `mods` folder inside the game directory. This is
   the piece that actually gets a third-party DLL loaded into the running `BurnoutPR.exe` process.
   Bo98 (Bo Anderson) also maintains `xenia-burnout5` (see the companion BurnoutDecomp topic) and
   `libbndl`, `bpr-bugs` — an active, technically-credible figure in this scene.
2. **[matty-ross's bpr-open-mods](https://github.com/matty-ross/bpr-open-mods)** (archived
   Dec 2023, but complete) — the actual mod DLLs. Structure: `lib/` (shared code), `mods/`
   (individual mods), `vendor/` containing **Dear ImGui**, **Microsoft Detours**, and
   **yaml-cpp**. Detours is a runtime API-hooking library — confirms mods hook game *functions*
   (not raw byte-patching) once loaded, and ImGui provides in-game debug/config UI, which is
   exactly the kind of harness this project will eventually want for its own camera-override tooling.

**Critically: this proves DLL injection into the Steam build of BurnoutPR.exe is a solved, working
problem** for at least one third-party toolchain (bo98's loader). This directly seeds
`ENGINE-DOSSIER.md` §4's "injection vector that works" — the modding session shouldn't need to
rediscover this from scratch, though it should still independently verify the loader still works
against the currently-installed Steam build version before relying on it. See the companion vorpX
topic for an important caveat: not *all* third-party injectors succeed against this game.

## The mod most relevant to camera/projection research: Free Camera

matty-ross's **Free Camera** mod ("moves the external camera around the city, plus various camera
properties that can be changed" — [demo](https://rumble.com/v3zui7g-expanded-map-free-camera-portable-junkyard-burnout-paradise-remastered-mods.html))
is source-available inside `bpr-open-mods`. Because it necessarily already found and hooked
whatever function(s) control camera position/orientation each frame, its source is a direct,
already-solved reference for part of `ENGINE-DOSSIER.md` §6 (camera & projection delivery) —
specifically the "where does the camera get set" half of that question, even if it doesn't
necessarily cover the VP/projection constant-buffer delivery to the GPU (§6/§7's harder half,
about how the transform reaches the shader).

## Other useful tools from this scene

- **[burninrubber0/YAP](https://github.com/burninrubber0/YAP)** and
  **[BurnoutHints/Bundle-Manager](https://github.com/burninrubber0/Bundle-Manager)** — bundle
  (`.BNDL`)  extraction/creation tools, "Bundle 2 version 2" format. Not urgent for VR work (asset
  format, not renderer/camera), but useful if the mod ever needs to read level/vehicle data.
- **orimarc's BPR Speed Patch** — unlocks the frame rate from 30 to 60 FPS. Worth knowing about
  since VR needs a high, stable frame rate — if the base game is capped at 30 by default, this
  patch (or understanding how it uncaps it) may be a prerequisite, not just a nice-to-have.
- **Brick Remastered** (JeBobs et al.) — general QoL mod; less relevant but shows the scene is
  active and maintained into 2026.

## Concrete next step

When engine research resumes: read `bpr-open-mods`'s Free Camera mod source (own-words
understanding only, no copying) to identify the camera-control function(s)/offsets it hooks, and
use bo98's loader as the starting injection foothold rather than building one from scratch,
pending independent verification against the currently-installed build.

## Sources

- https://github.com/RomulusMirauta/Burnout-Paradise-Remastered
- https://bpr.bo98.uk/
- https://github.com/bo98
- https://github.com/matty-ross/bpr-open-mods
- https://github.com/matty-ross/bpr-mods-repository
- https://matty-ross.github.io/bpr-mods/
- https://rumble.com/v3zui7g-expanded-map-free-camera-portable-junkyard-burnout-paradise-remastered-mods.html
- https://github.com/burninrubber0/YAP
- https://github.com/burninrubber0/Bundle-Manager
