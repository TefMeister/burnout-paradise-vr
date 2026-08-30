# 2026-08-25 — First look: renderer confirmed, and a real complication found (Denuvo)

Session type: static file analysis only. The game was never launched — this was reading the
installed `BurnoutPR.exe` on disk (PE headers, section table, export table, embedded
strings), nothing more.

## What we now know for sure

- **The renderer is Direct3D 11.** The exe literally names `d3d11.dll`, `dxgi.dll`, and the
  D3D11 device-creation functions. No trace of D3D12, Vulkan, or the original 2008 game's
  D3D9 anywhere — this remaster runs on D3D11 only.
- **The engine is Criterion's own in-house tech**, not licensed RenderWare (the strings in
  the binary only say "Criterion"/"Criterion Games", never "RenderWare"). UI is built with
  Scaleform GFx (Autodesk middleware, very common in this console generation).
- **The game is protected by Denuvo Anti-Tamper.** This is the one real piece of bad-ish
  news from today: the exe has two functions built specifically for Denuvo's licensing
  system, and the file's shape (a ~108 MB opaque blob making up almost the entire 127 MB
  image, with the actual entry point hidden inside it) matches Denuvo's known wrapping
  pattern exactly. No other anti-cheat (no EasyAntiCheat, no BattlEye) — just Denuvo.

## What Denuvo actually means for us, in plain terms

Denuvo wraps and encrypts the game's own code to stop tampering/piracy. It does **not**
generally stop the kind of VR modding this portfolio does elsewhere — every other project
here works by swapping in our own version of a system DLL (like `d3d9.dll` or `winmm.dll`)
that the game loads normally through Windows itself; that's the same trick tools like
ReShade use on plenty of Denuvo-protected games without issue, because it never touches or
patches the protected executable's own memory.

Where Denuvo is more likely to bite us: **attaching a live debugger to poke around inside the
running game** (which is normally how we'd trace exactly where the camera/projection data
gets built) is a much dicier proposition against Denuvo — it's specifically designed to
notice and react to that. We haven't tested this yet, so we don't know if it'll crash the
game, silently misbehave, or just work fine. It's a real open question for whenever we first
try live inspection, not a confirmed blocker.

## Bottom line for "can this be VR'd at all"

Nothing found today rules it out. D3D11 with a normal `CreateDXGIFactory`/
`D3D11CreateDeviceAndSwapChain` device-creation path is exactly the shape of every other
successful D3D11 project in this portfolio (The Evil Within, RE2/RE Village via
REFramework). Denuvo raises the difficulty of the *investigation* phase, not necessarily the
difficulty of the eventual fix — assuming the DLL-proxy injection route holds up the way it
has everywhere else. That's the thing to prove first.

## Next step

Build a minimal DXGI/D3D11 proxy DLL — logs `CreateDevice`/`CreateSwapChain`/`Present` calls
to a file, does nothing else yet. This can be built and even deployed to the game folder
without running the game at all. Actually seeing it load correctly needs the game running
once, which — per our current workflow — means a live session where I hand off exact
instructions and you drive the game yourself.

Full raw technical findings: `burnout-paradise-vr-dev-archive`, `recon/2026-08-25-m0-static-recon/`.
Distilled reference: `burnout-paradise-vr-engine-research`, `ENGINE-DOSSIER.md` §3/§4/§12.
