# Research index

Every research topic gathered for this project, newest first. Each row links to a self-contained
write-up in `topics/`. Status tags:

- 🆕 **new** — found, not yet acted on by the modding side.
- 👀 **reviewed** — a modding session has read it and factored it into a decision, but nothing shipped from it yet.
- ✅ **incorporated** — directly led to a real change (code, a test, a note) in one of the other five repos; linked below.
- ❌ **dead end** — checked out, didn't pan out; kept for the record so it isn't re-investigated from scratch.

| Date | Topic | Status | Summary |
| --- | --- | --- | --- |
| 2026-08-25 | [Denuvo's 2026 landscape + ScyllaHide](topics/2026-08-25-denuvo-2026-landscape-and-scyllahide.md) | 👀 reviewed | Denuvo's anti-tamper effectiveness has reportedly collapsed industry-wide by mid-2026; ScyllaHide (x64dbg plugin) is the concrete, legitimate tool to try first for debugger attach against `BurnoutPR.exe`'s confirmed Denuvo protection. Factored into ENGINE-DOSSIER.md §4 as the plan for the first live-debugger attempt. |
| 2026-08-25 | [Stereo-3D prior art (HelixMod/3Dmigoto)](topics/2026-08-25-stereo-3d-prior-art-helixmod-3dmigoto.md) | 👀 reviewed | Original game has a D3D9 HelixMod UI-depth fix; no equivalent exists yet for Remastered's D3D11 build. Confirms 3Dmigoto is the right tool class for camera/cbuffer discovery, but no shortcut — reflection work starts from scratch. Factored into ENGINE-DOSSIER.md §6/§7/§11 as the recommended live-analysis instrument (not a shipped dependency). |
| 2026-08-25 | [The BurnoutDecomp project](topics/2026-08-25-burnoutdecomp-project.md) | 👀 reviewed | Active public AI-assisted decompilation of Burnout Paradise (Xbox 360/PS3/PC) — potential source for camera/projection/frame-loop logic, and a data point on the RenderWare question. Factored into ENGINE-DOSSIER.md §2 (softened the RenderWare claim); not yet used for actual camera research (too early). |
| 2026-08-25 | [Community modding tools & injection](topics/2026-08-25-community-modding-tools-and-injection.md) | 👀 reviewed | A working DLL-injection stack already exists for Steam `BurnoutPR.exe` (bo98's loader + Detours), plus a source-available Free Camera mod directly relevant to camera research. Factored into ENGINE-DOSSIER.md §4/§6/§12; our own M0 proxy DLL still being built independently (no third-party loader adopted), per the write-our-own-code policy. |
| 2026-08-25 | [vorpX fails to hook the Steam build](topics/2026-08-25-vorpx-steam-injection-rejection.md) | 👀 reviewed | vorpX can't inject into Steam Burnout Paradise, but the community loader can — vorpX-specific, not a blanket injection block. Factored into ENGINE-DOSSIER.md §4 as a caveat to watch for during first live injection test. |

## How to add a topic

1. New file in `topics/`, named `YYYY-MM-DD-short-slug.md`.
2. One row added to the table above, newest at the top.
3. Update the status tag here as it moves through review → incorporated/dead-end (the modding side should update this when it acts on a lead, so the index reflects reality without the research side needing to poll).
