# M0 static recon — 2026-08-25

Pure file-based static analysis of the installed `BurnoutPR.exe` — no process was launched
or attached to, per the standing no-live-game-driving rule. Tools used: `file`, `objdump`
(llvm-mingw), `strings` (llvm-mingw), all read-only against the file on disk.

## Raw evidence

### `file` / `objdump -f`
```
BurnoutPR.exe: PE32 executable for MS Windows 6.00 (GUI), Intel i386, 13 sections
Characteristics 0x123: relocations stripped, executable, large address aware, 32 bit words
Time/Date: Fri Jun 29 19:16:51 2018
Magic: 010b (PE32, i.e. 32-bit)
AddressOfEntryPoint: 0x07f7c000
SizeOfImage: 0x07f7d000  (~127 MB)
Subsystem: Windows GUI
```

`BurnoutPR.exe` is 124.6 MB on disk; a second binary, `BurnoutPR_trial.exe` (224.3 MB), also
exists in the install root — not yet investigated, Steam launches `BurnoutPR.exe`.

### Section table (`objdump -h`)
```
Idx Name          Size     VMA      Type
  0 .code         008ad000 00401000 TEXT
  1 .link         00278800 00cae000 DATA
  2 .sdata        003d7e00 00f27000
  3 .text         00000200 015e7000
  4 .rdata        00000200 015e8000
  5 .edata        00000200 015e9000
  6 .data         00009200 015ea000
  7 .trace        06c854fc 015f4000 TEXT   <- ~108 MB, almost the whole image
  8 .srdata       000064da 0827a000 TEXT
  9 .text1        000006a6 08281000 TEXT
 10 .rsrc         00009930 08282000 DATA
 11 .sbss         000ef708 0828c000 DATA
 12 .ooa          00000612 0837c000 TEXT
```

The entry point RVA (`0x7f7c000`) falls inside `.trace` (`0x15f4000` .. `0x8279500`), not
inside `.code` (which ends at `0xcae000`) — i.e. the loader's first instruction is inside the
giant opaque blob, not the section holding recognizable symbols.

### Export table (`objdump -p`, tail)
Confirmed Denuvo:
```
0x5c04950  GetDenuvoTicketLocation
0x5c05010  GetDenuvoTimeTicketRequest
```
Confirmed Scaleform GFx UI + EA string lib, e.g.:
```
AptRenderItemCustomControl, AptValue, AptMovieClip, AptActionInterpreter,
AptCharacterTextInst, EAStringC, DOGMA_MemPool
```

### Renderer strings (`strings | grep -iE "d3d11|dxgi|d3dcompiler"`)
```
CreateDXGIFactory
D3D11CreateDevice
D3D11CreateDeviceAndSwapChain
D3DCOMPILER_47.dll
d3d11.dll
d3dcompiler_47.dll
dxgi.dll
```
No `d3d9`, `d3d12`, `vulkan-1`, or `opengl32` hits anywhere in the binary.

### Engine self-ID strings
```
Criterion
Criterion Games
EA_Criterion_Logo
gamedb://criterion_burnout5/Burnout-PrePro/Scenes_New/renderworld2#39971
```
No `RenderWare` or `Chameleon` hits — nothing in the binary itself supports either name for
this engine; "Criterion's own in-house engine" is as specific as the evidence currently
allows.

### Other anti-tamper / DRM checks (all negative except Denuvo)
```
battleye / easyanticheat / EAC.dll / securom / safedisc -> no hits
```
`Core\Activation.dll` / `Activation64.dll` are present (EA's own entitlement/activation
DRM, separate from Denuvo, standard for any EA-published PC title) — not expected to
interfere with modding directly, unlike Denuvo.

### Install layout notes
- `ENGINES\` — ~150 hex-named `.BUNDLE` files (e.g. `01FE7FE4.BUNDLE`), purpose unidentified.
- `GPGPU\GPGPU.bin` — 4 KB. No DirectCompute/CUDA strings found in the exe itself, so this is
  likely just data, not evidence of compute shaders in the render path (not confirmed).
- `__overlay\steam_api.dll` + `overlayinjector.exe` — Steam overlay only; no `steam_api`
  strings found inside `BurnoutPR.exe` itself, suggesting Steamworks isn't linked directly
  into the main exe (EA's own Activation DLLs look like the primary entitlement check).

## What this means for the project (see ENGINE-DOSSIER.md §3/§4/§12 for the distilled version)

- **Renderer is Direct3D 11 — confirmed**, not an inference anymore.
- **Denuvo Anti-Tamper is present** — the biggest open risk this session found. It shouldn't
  block a DXGI/D3D11 proxy-DLL injection approach (doesn't touch the protected exe's memory,
  same mechanism ReShade and similar tools already use on many Denuvo titles), but it may
  complicate or block debugger-based investigation later — untested either way.
- Engine is Criterion's own in-house tech (not licensed RenderWare) with Scaleform GFx for UI
  and EA's internal string library linked in.

## Dead ends / non-findings worth recording
- No deferred-context (`CreateDeferredContext`/`FinishCommandList`) strings found — but this
  is inconclusive by itself, since D3D11 interface calls are vtable calls, not
  `GetProcAddress`-resolved names, so their absence as strings doesn't rule out a
  multi-threaded render path. Needs live inspection (module/vtable check) to actually answer.
