# Research index

Every research topic gathered for this project, newest first. Each row links to a self-contained
write-up in `topics/`. Status tags:

- 🆕 **new** — found, not yet acted on by the modding side.
- 👀 **reviewed** — a modding session has read it and factored it into a decision, but nothing shipped from it yet.
- ✅ **incorporated** — directly led to a real change (code, a test, a note) in one of the other five repos; linked below.
- ❌ **dead end** — checked out, didn't pan out; kept for the record so it isn't re-investigated from scratch.

| Date | Topic | Status | Summary |
| --- | --- | --- | --- |
| 2026-08-25 | [The BurnoutDecomp project](topics/2026-08-25-burnoutdecomp-project.md) | 👀 reviewed | Active public AI-assisted decompilation of Burnout Paradise (Xbox 360/PS3/PC) — potential source for camera/projection/frame-loop logic, and a data point on the RenderWare question. Factored into ENGINE-DOSSIER.md §2 (softened the RenderWare claim); not yet used for actual camera research (too early). |
| 2026-08-25 | [Community modding tools & injection](topics/2026-08-25-community-modding-tools-and-injection.md) | 👀 reviewed | A working DLL-injection stack already exists for Steam `BurnoutPR.exe` (bo98's loader + Detours), plus a source-available Free Camera mod directly relevant to camera research. Factored into ENGINE-DOSSIER.md §4/§6/§12; our own M0 proxy DLL still being built independently (no third-party loader adopted), per the write-our-own-code policy. |
| 2026-08-25 | [vorpX fails to hook the Steam build](topics/2026-08-25-vorpx-steam-injection-rejection.md) | 👀 reviewed | vorpX can't inject into Steam Burnout Paradise, but the community loader can — vorpX-specific, not a blanket injection block. Factored into ENGINE-DOSSIER.md §4 as a caveat to watch for during first live injection test. |

## How to add a topic

1. New file in `topics/`, named `YYYY-MM-DD-short-slug.md`.
2. One row added to the table above, newest at the top.
3. Update the status tag here as it moves through review → incorporated/dead-end (the modding side should update this when it acts on a lead, so the index reflects reality without the research side needing to poll).
