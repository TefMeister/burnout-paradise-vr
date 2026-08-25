# Engine Dossier — Burnout Paradise Remastered (Criterion in-house engine)

> One consolidated, living reference for this game's engine, filled in as the
> `PLAYBOOK.md` phases are worked. Chronological blow-by-blow belongs in the
> `-dev-archive` / `-modding-notes` repos; this file is the *distilled current
> truth*. Update it whenever a fact changes; correct false leads in place.

**Status:** M0 static recon done (binary/renderer/DRM identified, no live process touched) — see §11 for the one open risk this raised · **VR-readiness verdict:** TBD, likely feasible but Denuvo raises the injection/debugging difficulty above this portfolio's usual baseline

## 1. Identity
- Game / build / version: Burnout Paradise Remastered (2018 remaster of the 2008 original), Steam build, exe `BurnoutPR.exe`.
- Platform & store; unofficial port? (extra fragility/legal notes): Steam (PC). Official remaster, not a fan port.
- Legitimacy: owned copy confirmed.

## 2. Engine lineage
- Family / base engine and how it was modified: Criterion Games' own proprietary in-house engine. Not licensed RenderWare — Criterion used RenderWare in earlier titles, but Burnout Paradise runs a distinct in-house engine; this distinction should be kept accurate and not conflated in any writeup.
- Middleware (animation, audio, physics, megatexture, CUDA, etc.): **Scaleform GFx (Autodesk)** confirmed for UI — the export table is full of `Apt*`/`AptValue`/`AptMovieClip`/`AptActionInterpreter` symbols, which is Scaleform's internal name for a compiled SWF ("Apt" format); `EAStringC` in the same exports confirms EA's internal string library (EAStdC/EASTL family) is linked in. A `DOGMA_MemPool` symbol also appears (custom memory pool allocator, name not otherwise identified yet).
- Distinctive file formats / build tags / symbol naming: install directory contains `.BNDL`/`.BUNDLE`/`.DAT`/`.BIN`/`.HM`/`.HMSC` data archives (names observed: e.g. `B5TRAFFIC.BNDL`, `GLOBALMODELDICTIONARY.BIN`, `HUDMESSAGES.HM`) — not yet parsed or understood. `ENGINES\` holds ~150 numbered/hashed `.BUNDLE` files (hex-named, e.g. `01FE7FE4.BUNDLE`) — purpose not yet identified. `GPGPU\GPGPU.bin` (4KB) exists but no DirectCompute/CUDA strings were found in the exe itself — likely just data, not evidence of GPU compute shaders in the render path (unconfirmed).

## 3. Binary & memory
- 32/64-bit, size, module base, ASLR behaviour (stable base? relocations?): **32-bit** (PE32, `coff-i386`), linked 2018-06-29. `BurnoutPR.exe` is unusually large on disk (124.6 MB) with `SizeOfImage` ≈ 127 MB — see §4, this is Denuvo, not real code size. Relocations are stripped per the file characteristics flags; ASLR/base-address behaviour not yet tested live. A second binary, `BurnoutPR_trial.exe` (224 MB), also ships in the install — purpose (an old EA Origin trial build?) not yet investigated; `BurnoutPR.exe` is the one Steam launches.
- Renderer API (D3D11/12, DXGI, GL, Vulkan) with evidence: **Direct3D 11, confirmed** by literal strings in the binary: `d3d11.dll`, `dxgi.dll`, `D3D11CreateDevice`, `D3D11CreateDeviceAndSwapChain`, `CreateDXGIFactory`, plus `D3DCOMPILER_47.dll` (matches the `d3dcompiler_47.dll` shipped alongside the exe). No D3D12, Vulkan, or D3D9 strings found anywhere — this remaster fully moved off the 2008 original's D3D9 path.
- Developer console / cvar system present? how opened?: not yet investigated.

## 4. DRM / anti-debug & injection foothold
- DRM (CEG/Denuvo/GOG/none); launch-time-debugger behaviour: **Denuvo Anti-Tamper confirmed present**, found via two literal exported functions in `BurnoutPR.exe`: `GetDenuvoTicketLocation` and `GetDenuvoTimeTicketRequest`. Corroborating structural evidence: the PE has a ~108 MB `.trace` section (VMA `0x15f4000`, size `0x6c854fc`) — almost the entire image — and the file's `AddressOfEntryPoint` (RVA `0x7f7c000`) lands *inside* that `.trace` blob, not inside the normal-looking `.code` section that holds the recognizable Scaleform/EA/Denuvo export symbols. That's the classic virtualization-wrapper shape: the real OEP is hidden inside an opaque encrypted/virtualized region, and the loader jumps there first. The Import Directory is also abnormally tiny (40 bytes) for a game this size, consistent with most real imports being resolved at runtime post-unpack rather than sitting in a normal static IAT. **Not yet tested: whether a debugger attach is survivable** (Denuvo often detects/kills on attach) — flagged as a real risk for any future live-inspection session, not verified either way yet. No EasyAntiCheat/BattlEye/SecuROM/SafeDisc strings found — Denuvo appears to be the only anti-tamper layer. Separately, EA's own entitlement/activation DRM is present too (`Core\Activation.dll` / `Activation64.dll`, `__Installer\` EA/Origin installer scripts) — this is standard EA-App licensing, unrelated to Denuvo, and shouldn't affect modding directly.
- Attach workflow that works: not yet tested.
- Injection vector that works (proxy DLL name / injector / framework): not yet tested, but a **DXGI or D3D11 proxy DLL is the natural candidate** (the pattern already proven on this portfolio's other D3D9/D3D11 titles) — plausibly more Denuvo-resistant than debugger-based approaches, since it only relies on the ordinary Windows DLL-search-order loader mechanism (the same mechanism ReShade and similar overlays use on plenty of other Denuvo titles) rather than attaching to or patching the protected executable's own memory.

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
- **Denuvo Anti-Tamper (confirmed present, 2026-08-25 — see §4) is the single biggest open risk for this project specifically**, and the reason this game's difficulty may run higher than this portfolio's usual baseline. It doesn't block the DLL-proxy injection approach that has worked on every other project here (that technique doesn't touch the protected executable's own memory), but it likely does complicate or block live-debugger-based investigation (disassembly of the actual camera/projection code, breakpoint-based tracing) — untested either way yet, flagged for the first live session that tries it.
- Driving games carry an elevated motion-sickness risk vs. walking-sim/shooter conversions — comfort options (FOV vignette, fixed cockpit reference frame, etc.) are likely to matter more here than in other projects.
- Racing HUD/UI complexity (speedometer, minimap, event markers) may need special handling to stay legible and comfortable in a headset.
