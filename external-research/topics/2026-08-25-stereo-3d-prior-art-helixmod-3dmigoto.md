# Stereo-3D prior art: a solved D3D9 UI-depth fix for the original, nothing yet for Remastered's D3D11

**Status:** 🆕 new · **Priority:** medium — informs `ENGINE-DOSSIER.md` §6/§7 (camera/projection
delivery, constant-buffer mechanism) approach, and sets expectations (no shortcut exists yet).

## What exists

A **Helix Mod** stereoscopic-3D fix exists for the **original 2008 Burnout Paradise** (D3D9,
"Steam version, game version 1.0.0.1") — [helixmod.blogspot.com writeup](https://helixmod.blogspot.com/2012/12/burnout-paradise.html).
It's UI-focused: it renders menus, HUD, text, and the minimap with actual stereoscopic depth
instead of as a flat overlay pasted over the 3D scene (the standard problem any stereo/VR
conversion has to solve — HUD elements need a different, deliberate depth treatment from the 3D
world, or they read as broken/floating), and separately disables a couple of visual effects
(2D skid/crash smoke, headlamp halos) that didn't work correctly once stereo was on. The writeup
gives no public technical detail on constant-buffer offsets, shader hooks, or camera-matrix
manipulation specifics — likely because HelixMod fixes are typically distributed as compiled
shader-override packages plus a d3d9.dll proxy, not as a documented methodology.

**Community consensus explicitly confirmed no equivalent exists for Remastered**: the same
HelixMod discussion states the remaster "uses DirectX 11 with changed shaders" and that someone
*could* "potentially refix the game using 3Dmigoto if motivated" — phrased as a hypothetical, not
as something already done. A direct search across 3D-vision-focused communities (Reddit, forums)
turned up nothing for "Burnout Paradise Remastered" + 3Dmigoto specifically.

## What this means for this project

- **No shortcut exists.** Nobody has publicly reverse-engineered `BurnoutPR.exe`'s D3D11 shaders
  or constant buffers for stereo/3D purposes. `ENGINE-DOSSIER.md` §6/§7 (camera & projection
  delivery, cbuffer fill mechanism) will have to be discovered from scratch via shader reflection
  and disassembly against the live D3D11 process — no one has already solved "where does the VP
  matrix live and how does it reach the GPU" for this exact binary.
- **The tool category to reach for is confirmed correct, though**: [**3Dmigoto**](https://github.com/DarkStarSword/3d-fixes)
  (DarkStarSword's actively-maintained fork is the modern reference implementation) is exactly the
  class of tool this project needs regardless of stereo-3D goals — it's a D3D11 shader-dumping/
  constant-buffer-hooking/hlsl-override framework built precisely for "find and modify the
  camera/projection math live" work, which is this project's core §6/§7 task. Even without a
  Burnout-specific fix to reference, 3Dmigoto (or an equivalent purpose-built D3D11 hook) is the
  right instrument, not something to build from zero — it already handles shader reflection, cbuffer
  dumping/hashing, and hlsl live-reload, which is otherwise a lot of infrastructure to hand-roll.
- **The original game's UI-depth-separation problem will recur.** Whatever the D3D11 remaster's HUD
  rendering looks like, the same need — treat HUD/minimap/speedometer differently from world
  geometry — is confirmed (by the original's fix needing exactly this) to be a real, non-optional
  problem for this game's genre, consistent with `ENGINE-DOSSIER.md` §12's existing note about
  racing-HUD complexity.

## Concrete next step

When shader-reflection work on `BurnoutPR.exe` begins (§6/§7), evaluate 3Dmigoto itself as the
hooking/dumping framework rather than building an equivalent from scratch — it's mature, D3D11-
native, and exactly scoped to this problem, even though no Burnout-specific configuration for it
exists yet to reuse.

## Sources

- https://helixmod.blogspot.com/2012/12/burnout-paradise.html
- https://github.com/DarkStarSword/3d-fixes
