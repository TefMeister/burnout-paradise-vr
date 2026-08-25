# Engine Dossier — Burnout Paradise Remastered (Criterion in-house engine)

> One consolidated, living reference for this game's engine, filled in as the
> `PLAYBOOK.md` phases are worked. Chronological blow-by-blow belongs in the
> `-dev-archive` / `-modding-notes` repos; this file is the *distilled current
> truth*. Update it whenever a fact changes; correct false leads in place.

**Status:** groundwork — repos just created, engine research about to begin — this is the next active front · **VR-readiness verdict:** TBD

## 1. Identity
- Game / build / version: Burnout Paradise Remastered (2018 remaster of the 2008 original), Steam build, exe `BurnoutPR.exe`.
- Platform & store; unofficial port? (extra fragility/legal notes): Steam (PC). Official remaster, not a fan port.
- Legitimacy: owned copy confirmed.

## 2. Engine lineage
- Family / base engine and how it was modified: Criterion Games' own proprietary in-house engine. Not licensed RenderWare — Criterion used RenderWare in earlier titles, but Burnout Paradise runs a distinct in-house engine; this distinction should be kept accurate and not conflated in any writeup.
- Middleware (animation, audio, physics, megatexture, CUDA, etc.):
- Distinctive file formats / build tags / symbol naming: install directory contains `.BNDL`/`.BUNDLE`/`.DAT`/`.BIN`/`.HM`/`.HMSC` data archives (names observed: e.g. `B5TRAFFIC.BNDL`, `GLOBALMODELDICTIONARY.BIN`, `HUDMESSAGES.HM`) — not yet parsed or understood.

## 3. Binary & memory
- 32/64-bit, size, module base, ASLR behaviour (stable base? relocations?):
- Renderer API (D3D11/12, DXGI, GL, Vulkan) with evidence: Direct3D 11 likely — `d3dcompiler_47.dll` present in the install; unconfirmed by live inspection yet.
- Developer console / cvar system present? how opened?:

## 4. DRM / anti-debug & injection foothold
- DRM (CEG/Denuvo/GOG/none); launch-time-debugger behaviour:
- Attach workflow that works:
- Injection vector that works (proxy DLL name / injector / framework):

## 5. Threading & frame structure
- Immediate context only, or deferred contexts + command lists?:
- Which thread(s) do what; render-thread name(s):
- One-frame walkthrough (record → replay → present):

## 6. Camera & projection delivery (the crucial section)
- How the world transform reaches the GPU (shared VP buffer / per-draw MVP /
  other), with **shader-reflection / disassembly evidence**:
- Exact constant-buffer slot, parameter name(s), byte offset(s), layout,
  handedness, row/column convention:
- Where projection `P` / FOV comes from:
- The per-eye override maths (`K_eye = …`):

## 7. Constant-buffer fill mechanism
- Map/DISCARD ring / UpdateSubresource / D3D11.1 offset / **persistent map +
  memcpy** (trap):
- Can source contents be read cheaply (captured CPU pointer) or need staging
  read-back?:
- The chosen override patch point and why:

## 8. Pass inventory (by render target)
- Main scene (res/formats):
- Shadow passes (depth-only sizes):
- Post / AA chain (SMAA/TAA/motion vectors; downscale sizes):
- UI / HUD (how it's kept separate):

## 9. cvar / console cheat sheet
| command / cvar | effect | use |
|---|---|---|
| | | |

## 10. Autonomous harness recipe (this game)
- Launch to a known scene (commands used):
- In-process input / camera drive method that worked:
- Frame-capture method; where images land:

## 11. Dead ends & false leads (save future time)
- <what looked true but wasn't, and why>

## 12. Open risks toward the North Star
- Driving games carry an elevated motion-sickness risk vs. walking-sim/shooter conversions — comfort options (FOV vignette, fixed cockpit reference frame, etc.) are likely to matter more here than in other projects.
- Racing HUD/UI complexity (speedometer, minimap, event markers) may need special handling to stay legible and comfortable in a headset.
