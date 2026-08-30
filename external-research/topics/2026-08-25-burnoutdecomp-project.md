# The BurnoutDecomp project — a public, active Burnout Paradise decompilation effort

**Status:** 🆕 new · **Priority:** high — this is potentially the single most valuable
prior-art source available for this project.

## What it is

[`BurnoutDecomp`](https://github.com/BurnoutDecomp) is a public GitHub organization running an
active, AI-agent-assisted decompilation of **Burnout 5** (Criterion's internal codename for
Burnout Paradise) into compilable C++. It is not affiliated with this project — an independent
group of enthusiasts/researchers.

Key repos:

- **[BP-Decomp_Workflow](https://github.com/BurnoutDecomp/BP-Decomp_Workflow)** — the orchestration
  repo. Explains the methodology: AI agents claim a "translation unit" (TU) from a central ledger,
  reconstruct its source using IDA Pro export data, run MSVC 2022 compile/parity gates against the
  original binary, and record a review verdict. Progress is tracked per-TU (todo → in-progress →
  compiled → reviewed → done) in `progress/status.json`. As of this check, 1,891 commits deep on
  the main branch — this is a substantial, ongoing effort, not a stub.
- **[b5-decomp](https://github.com/BurnoutDecomp/b5-decomp)** — the actual recovered source tree,
  pulled in as a submodule of the workflow repo. Source is organized under `src/` "mirroring
  original paths"; `vendor/` contains EA open-source libraries **and RenderWare support files**.
- **[YAP](https://github.com/BurnoutDecomp/YAP)** (fork of burninrubber0's tool) — bundle
  extractor/creator, only handles "Bundle 2 version 2" (the format Burnout Paradise uses).
- **volatility** — described as a "Burnout Paradise platform-agnostic resource interface" (C#).
- **[bo98/xenia-burnout5](https://github.com/bo98/xenia-burnout5)** — a fork of `xenia-canary`
  (the Xbox 360 emulator) "with experimental fixes for Burnout Paradise," almost certainly built
  to run/debug the Xbox 360 build (`BURNOUT_X360_ARTIST.XEX`) that the decomp targets.

## What's being decompiled, exactly

The primary decomp target is the **Xbox 360 build**, cross-referenced against:
- PS3 ELF builds, which are described as "symbol-rich and DWARF-annotated" (i.e. carry real debug
  info publicly usable for corroboration),
- stripped PC binaries including **`BurnoutPR.exe`** — our exact target exe — and
  `TUB_Burnout_PC_External.exe` (the original 2009 PC release),
- a leaked Feb-2007 source code slice used as the highest-fidelity reconstruction template.

## Why this matters for the VR mod specifically

1. **RenderWare, reconciled.** Our `ENGINE-DOSSIER.md` §2 currently states Burnout Paradise runs a
   distinct in-house engine, *not* licensed RenderWare. `b5-decomp`'s `vendor/` folder containing
   "RenderWare support" doesn't necessarily contradict that — Criterion's later engine could still
   use RenderWare-derived math/asset libraries under the hood even if the renderer itself isn't
   RenderWare proper — but it's a concrete public data point worth reconciling once someone has
   eyes on the actual vendor tree, rather than leaving the dossier's claim unqualified.
2. **A second, symbol-rich build to cross-reference against.** If `BurnoutPR.exe`'s D3D11 code is
   ever hard to read stripped, the PS3 ELF (DWARF-annotated) or the reconstructed Xbox 360 source
   may name the same camera/projection functions and data structures, even though the renderer
   backend differs per platform. Decompiled camera/vehicle-physics/frame-loop C++ — once a given
   TU reaches "done" — would very plausibly cover the camera rig and per-frame view/projection
   setup this project's §6 (Camera & projection delivery) is built around, since that logic is
   normally platform-shared game code rather than renderer-specific.
3. **Bundle format is already solved** (YAP / Bundle-Manager, also covered in the companion
   community-tools topic) — not this project's job to redo.

## Concrete next step

When engine research resumes, have the modding session:
- Check `BP-Decomp_Workflow`'s `progress/status.json` (or browse `b5-decomp/src/`) for any TU whose
  path suggests camera, view, projection, or frame/render-loop ownership, and see whether it's
  already reconstructed (`done`/`reviewed`).
- Skim `b5-decomp/vendor/` to confirm/refute the RenderWare relationship precisely, and correct
  `ENGINE-DOSSIER.md` §2 accordingly (in either direction) rather than leaving it ambiguous.
- Treat the PS3 DWARF-annotated ELF as a second, independently-useful decompilation aid if the PC
  binary alone proves hard to reverse.

This is public GitHub research/tooling, not anyone's copyrighted game asset — safe to read and
learn from under this project's normal "study public sources, write our own code" policy. Do not
copy any of its reconstructed source verbatim into this project even once code is written; treat
it exactly like any other prior-art reference: read it, understand the mechanism, reimplement
independently, credit it.

## Sources

- https://github.com/BurnoutDecomp
- https://github.com/BurnoutDecomp/BP-Decomp_Workflow
- https://github.com/BurnoutDecomp/b5-decomp
- https://github.com/BurnoutDecomp/YAP
- https://github.com/bo98/xenia-burnout5
