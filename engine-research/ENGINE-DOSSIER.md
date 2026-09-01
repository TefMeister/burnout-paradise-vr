# Engine Dossier — Burnout Paradise Remastered (Criterion in-house engine)

> One consolidated, living reference for this game's engine, filled in as the
> `PLAYBOOK.md` phases are worked. Chronological blow-by-blow belongs in the
> `-dev-archive` / `-modding-notes` repos; this file is the *distilled current
> truth*. Update it whenever a fact changes; correct false leads in place.

**Status:** ⏸️ **PAUSED (2026-08-25) — blocked on an EA App/Origin account requirement outside this project's control, not a technical dead end.** M0 (static recon, external-research folding, proxy DLL build) is fully done and stands as good reference work; the launch chain itself is what's blocked. See §4 for the full story and the exact resume conditions. **VR-readiness verdict:** still genuinely TBD on the technical merits — nothing found says this game *can't* be VR'd, the blocker is account access, not engineering difficulty.

## 1. Identity
- Game / build / version: Burnout Paradise Remastered (2018 remaster of the 2008 original), Steam build, exe `BurnoutPR.exe`.
- Platform & store; unofficial port? (extra fragility/legal notes): Steam (PC). Official remaster, not a fan port.
- Legitimacy: owned copy confirmed.

## ⛔️ Re-confirmed 2026-09-01: the game is NOT installed on the dev machine

A `/pd` session checked before planning any work. `D:\Program Files (x86)\Steam\steamapps\common\BurnoutPR\`
**exists but contains 89 KB in two files** — our own built `d3d11.dll` proxy and a `steam_appid.txt`
(app 1238080). No executable, no game data. `[inferred-static 2026-09-01]`

**⚠️ The leftover folder is itself the trap:** a directory listing of `steamapps\common` shows
`BurnoutPR/` alongside genuinely installed games, so a session that checks for the folder rather than
its contents will conclude the game is present and plan work that cannot run. Check for the
executable, not the directory.

Nothing was lost: the proxy source is committed at `staging/burnout-paradise-vr/proxy-d3d11/`
(`src/proxy.c`, `src/d3d11.def`, `build.sh`), so the deployed DLL is reproducible and the folder can
be deleted freely.

This is a **confirmation of the recorded blocker, not an unblock** — the project stays paused, and
static work on it stays impossible for the reason already recorded: there is no binary here to read.

## 2. Engine lineage
- Family / base engine and how it was modified: Criterion Games' own proprietary in-house engine ("Burnout 5" internally, per the public BurnoutDecomp project — see external-research). Not licensed RenderWare as the renderer itself — **caveat added 2026-08-25**: the public `BurnoutDecomp/b5-decomp` source-recovery project's `vendor/` tree reportedly contains RenderWare support files alongside EA's own open-source libraries, so some RenderWare-derived math/asset code may still be present under the hood even though the D3D11 renderer we're targeting is Criterion's own. Treat "not RenderWare" as true for the renderer specifically, not yet fully verified for the whole codebase — revisit once someone has actually looked at that vendor tree.
- Middleware (animation, audio, physics, megatexture, CUDA, etc.): **Scaleform GFx (Autodesk)** confirmed for UI — the export table is full of `Apt*`/`AptValue`/`AptMovieClip`/`AptActionInterpreter` symbols, which is Scaleform's internal name for a compiled SWF ("Apt" format); `EAStringC` in the same exports confirms EA's internal string library (EAStdC/EASTL family) is linked in. A `DOGMA_MemPool` symbol also appears (custom memory pool allocator, name not otherwise identified yet).
- Distinctive file formats / build tags / symbol naming: install directory contains `.BNDL`/`.BUNDLE`/`.DAT`/`.BIN`/`.HM`/`.HMSC` data archives (names observed: e.g. `B5TRAFFIC.BNDL`, `GLOBALMODELDICTIONARY.BIN`, `HUDMESSAGES.HM`) — not yet parsed or understood. `ENGINES\` holds ~150 numbered/hashed `.BUNDLE` files (hex-named, e.g. `01FE7FE4.BUNDLE`) — purpose not yet identified. `GPGPU\GPGPU.bin` (4KB) exists but no DirectCompute/CUDA strings were found in the exe itself — likely just data, not evidence of GPU compute shaders in the render path (unconfirmed).

## 3. Binary & memory
- 32/64-bit, size, module base, ASLR behaviour (stable base? relocations?): **32-bit** (PE32, `coff-i386`), linked 2018-06-29. `BurnoutPR.exe` is unusually large on disk (124.6 MB) with `SizeOfImage` ≈ 127 MB — see §4, this is Denuvo, not real code size. Relocations are stripped per the file characteristics flags; ASLR/base-address behaviour not yet tested live. A second binary, `BurnoutPR_trial.exe` (224 MB), also ships in the install — purpose (an old EA Origin trial build?) not yet investigated; `BurnoutPR.exe` is the one Steam launches.
- Renderer API (D3D11/12, DXGI, GL, Vulkan) with evidence: **Direct3D 11, confirmed** by literal strings in the binary: `d3d11.dll`, `dxgi.dll`, `D3D11CreateDevice`, `D3D11CreateDeviceAndSwapChain`, `CreateDXGIFactory`, plus `D3DCOMPILER_47.dll` (matches the `d3dcompiler_47.dll` shipped alongside the exe). No D3D12, Vulkan, or D3D9 strings found anywhere — this remaster fully moved off the 2008 original's D3D9 path.
- Developer console / cvar system present? how opened?: not yet investigated.

## 4. DRM / anti-debug & injection foothold
- DRM (CEG/Denuvo/GOG/none); launch-time-debugger behaviour: **Denuvo Anti-Tamper confirmed present**, found via two literal exported functions in `BurnoutPR.exe`: `GetDenuvoTicketLocation` and `GetDenuvoTimeTicketRequest`. Corroborating structural evidence: the PE has a ~108 MB `.trace` section (VMA `0x15f4000`, size `0x6c854fc`) — almost the entire image — and the file's `AddressOfEntryPoint` (RVA `0x7f7c000`) lands *inside* that `.trace` blob, not inside the normal-looking `.code` section that holds the recognizable Scaleform/EA/Denuvo export symbols. That's the classic virtualization-wrapper shape: the real OEP is hidden inside an opaque encrypted/virtualized region, and the loader jumps there first. The Import Directory is also abnormally tiny (40 bytes) for a game this size, consistent with most real imports being resolved at runtime post-unpack rather than sitting in a normal static IAT. **Not yet tested: whether a debugger attach is survivable** (Denuvo often detects/kills on attach) — flagged as a real risk for any future live-inspection session, not verified either way yet. No EasyAntiCheat/BattlEye/SecuROM/SafeDisc strings found — Denuvo appears to be the only anti-tamper layer. Separately, EA's own entitlement/activation DRM is present too (`Core\Activation.dll` / `Activation64.dll`, `__Installer\` EA/Origin installer scripts) — this is standard EA-App licensing, unrelated to Denuvo, and shouldn't affect modding directly.
- Attach workflow that works: not yet tested live. **Plan (external-research, 2026-08-25):** load the **ScyllaHide** x64dbg plugin (legitimate, open-source, already the standard "first thing to try" against usermode anti-debug per the RE community) before assuming Denuvo blocks attach outright. Context for why this is worth trying first rather than assuming the worst: mainstream outlets (PCGamesN, dsogaming) report Denuvo's practical anti-tamper effectiveness declined industry-wide through 2025-2026, with a growing list of publishers removing it post-launch — general trend context only, not a claim about this specific build. Record the actual result here once tested, replacing this placeholder either way.
- Injection vector that works (proxy DLL name / injector / framework): not yet tested by us, but a **DXGI or D3D11 proxy DLL is the natural candidate** (the pattern already proven on this portfolio's other D3D9/D3D11 titles) — plausibly more Denuvo-resistant than debugger-based approaches, since it only relies on the ordinary Windows DLL-search-order loader mechanism rather than attaching to or patching the protected executable's own memory. **Encouraging public precedent found 2026-08-25 (external-research):** an active community modding scene has a currently-working DLL-injection toolchain against this exact Steam build — bo98's "BPR Modder"/Mod Loader + a Detours-based hooking library, used by a real ecosystem of mods (see `bpr-open-mods`, archived Dec 2023 but complete). This proves *some* form of third-party code injection survives Denuvo + whatever other protections this exe has, which is a good sign for our own from-scratch proxy DLL — but their loader's exact mechanism (likely an active injector, not just a passive DLL-search-order proxy) may differ from ours, so this is encouraging precedent, not proof our specific technique will work. **Caveat found the same day:** vorpX's Burnout Paradise profile explicitly fails against the Steam build ("game doesn't like third party software to hook into it," per vorpX's own forum) while bo98's loader succeeds — so this exe is picky about *how* it's hooked, not blanket-hostile to all injection. Worth watching for DRM/integrity-check reactions during our own first live injection attempt. We are **not** adopting bo98's loader or copying any of its code — per this portfolio's write-our-own-code policy, it's prior-art confirmation only. **Our own DLL-proxy foothold is built and deployed** (`staging/burnout-paradise-vr/proxy-d3d11/`): a from-scratch `d3d11.dll` proxy, builds clean with the correct two exports (`D3D11CreateDevice`/`D3D11CreateDeviceAndSwapChain`), 32-bit, verified via `objdump`. **Still functionally unverified — the game has never successfully launched with it present**, for reasons unrelated to the DLL itself (see below).

**⏸️ PROJECT PAUSED HERE (2026-08-25): the game cannot currently be launched at all, by anyone on this machine, regardless of our mod.** Full chain of evidence from the first live-test session:
1. First launch attempt (proxy DLL present, via Steam): Steam error `"Failed to start process for this game: 'The operation was canceled by the user.' (0x4C7)"`. No log file appeared — our proxy's own code never ran. Windows Event Viewer (Application/System/Defender operational logs) showed nothing correlating — no crash, no AV block.
2. Ruled out a broken proxy DLL causing this at the loader level: `BurnoutPR.exe`'s only *static* PE import is `Core/Activation.dll` (EA's own licensing library) — `d3d11.dll` isn't a static dependency at all, so a missing export in our proxy couldn't cause a `CreateProcess`-time failure.
3. Control test: proxy DLL renamed aside, relaunched via Steam. **Different error** — Windows `"Application not found"` for a `link2ea://launchgame/1238080?platform=steam&theme=bprm` URI. This is EA's own launcher-handoff protocol; nothing was registered to handle it because the **EA App isn't installed** on this machine. Both errors trace to the same root cause.
4. Direct-exe-launch test (bypassing Steam's launcher entirely, double-clicking `BurnoutPR.exe`): still failed, reporting **Origin specifically as required**. This proves the check is baked into the exe's own code (via the statically-imported `Core/Activation.dll`), not just Steam's launch wrapper — bypassing Steam doesn't help.
5. **Alternative considered and ruled out:** `Burnout Paradise: The Ultimate Box` (the original 2008 Steam release, confirmed via community reports to need no Origin/EA App at all) would have sidestepped this entirely — but it's since been **delisted from the Steam store and not owned** on this account, so it's not currently obtainable.
6. **EA account recovery ruled out too:** the user's EA account credentials are lost along with access to the email address that would receive a password-reset link, so the "install EA App once, test if it's a one-time entitlement cache vs. a persistent runtime dependency" path isn't currently viable either.
7. **Explicitly considered and declined: patching out the `Core/Activation.dll` licensing check from the exe.** This would be a materially different act from everything else this portfolio does — every other technique here (D3D hooking, camera overrides, render injection) modifies *rendering/gameplay* behavior on an already-unlocked game, never whether the game considers itself licensed. Removing an entitlement check is circumventing a technological access-control measure, which sits in DMCA-anti-circumvention territory (17 U.S.C. §1201 and equivalents) even for a legitimately-owned copy — a real legal line, not just a technical one. Declined on that basis, not attempted.

**Resume conditions (any one of):** EA account access is recovered in the future (e.g. old email regained); `Burnout Paradise: The Ultimate Box` becomes purchasable/owned again; or the EA App/Origin requirement is otherwise resolved by the user outside of this project's own work. Nothing about the technical findings above (D3D11 confirmed, Denuvo confirmed, proxy DLL built clean) needs to be redone when that happens — this dossier and the staged proxy DLL are ready to pick back up as-is.

**Portfolio-wide takeaway (recorded in `PREFERENCES.md`, 2026-08-25):** future game selection for this portfolio should prefer Steam/Epic/GOG titles (or old free-to-download games) that don't gate launch behind a third-party publisher account (EA App/Origin, and by the same logic anything similarly gated) — not a hard rule, but a real lesson from this session.

## 5. Threading & frame structure
- Immediate context only, or deferred contexts + command lists?:
- Which thread(s) do what; render-thread name(s):
- One-frame walkthrough (record → replay → present):

## 6. Camera & projection delivery (the crucial section)
- **Tooling plan (external-research, 2026-08-25):** no public prior art exists for this exact
  binary's shaders/constant buffers (checked — see §11), so this section gets discovered from
  scratch via live shader reflection. **3Dmigoto** (DarkStarSword's maintained fork) is the
  recommended *analysis instrument* for that work — a mature D3D11 shader-dump/cbuffer-hook/
  HLSL-live-reload framework, used here the same way x64dbg is used elsewhere in this
  portfolio: to find and understand the mechanism live, not as something our shipped mod
  depends on or is built from. Our own proxy DLL (see §4) remains the thing we actually ship,
  written from scratch per this portfolio's policy.
- How the world transform reaches the GPU (shared VP buffer / per-draw MVP /
  other), with **shader-reflection / disassembly evidence**:
- Exact constant-buffer slot, parameter name(s), byte offset(s), layout,
  handedness, row/column convention:
- Where projection `P` / FOV comes from:
- The per-eye override maths (`K_eye = …`):
- **Lead, not yet used (external-research, 2026-08-25):** matty-ross's `bpr-open-mods` (archived,
  source-available) includes a **Free Camera** mod that already found and hooks whatever
  function(s) control the external camera's position/orientation each frame. That's the
  "where does the camera get set" half of this section, potentially saving significant
  reverse-engineering time later — study its own-words mechanism (never copy its code) when
  this section is actually worked. It likely does **not** cover the harder half (how the
  transform reaches the GPU as a constant buffer), which still needs shader-reflection work
  either way.

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
- **Not a dead end, but a confirmed non-shortcut (external-research, 2026-08-25):** a HelixMod
  stereoscopic-3D fix exists for the **original 2008 D3D9 release** (UI/HUD depth separation +
  disabling a couple of broken 2D effects under stereo), but the same source explicitly
  confirms **no equivalent exists for Remastered's D3D11 build** — nobody has publicly reverse
  engineered `BurnoutPR.exe`'s shaders/cbuffers for stereo purposes. Worth knowing the D3D9 fix
  exists (as confirmation the UI-depth problem is real for this game's genre, matching §12's
  racing-HUD note) but it gives no directly reusable technical detail for our D3D11 target.

## 12. Open risks toward the North Star
- **Denuvo Anti-Tamper (confirmed present, 2026-08-25 — see §4) is the single biggest open risk for this project specifically**, and the reason this game's difficulty may run higher than this portfolio's usual baseline. It doesn't block the DLL-proxy injection approach that has worked on every other project here (that technique doesn't touch the protected executable's own memory), but it likely does complicate or block live-debugger-based investigation (disassembly of the actual camera/projection code, breakpoint-based tracing) — untested either way yet, flagged for the first live session that tries it.
- Driving games carry an elevated motion-sickness risk vs. walking-sim/shooter conversions — comfort options (FOV vignette, fixed cockpit reference frame, etc.) are likely to matter more here than in other projects.
- Racing HUD/UI complexity (speedometer, minimap, event markers) may need special handling to stay legible and comfortable in a headset.
- **Frame rate (external-research, 2026-08-25):** the community scene has a "BPR Speed Patch" (orimarc) that unlocks the frame rate from a 30 FPS default to 60 FPS. VR needs a high, stable frame rate to avoid discomfort — if the base game really is 30 FPS-capped by default, understanding (and independently reimplementing) whatever that patch does is likely a prerequisite for this project, not just a nice-to-have. Not yet verified whether the currently-installed build is actually capped at 30.
