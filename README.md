# Burnout Paradise Remastered — VR Engine Research

Engine research toward a VR conversion of **Burnout Paradise Remastered**
(2018 remaster of the 2008 original, Criterion Games / Stellar
Entertainment) — cockpit-view stereo rendering and head tracking are the
goal.

This repository holds two things:

- **[`PLAYBOOK.md`](PLAYBOOK.md)** — a reusable, engine-agnostic, point-by-point
  method for taking *any* game whose engine nobody has converted to VR and
  getting it there. It is oriented around one North Star: **the game rendering
  in a headset with head tracking**, with everything else built on top. The same
  playbook is copied into each of our VR projects' research repos.
- **[`ENGINE-DOSSIER.md`](ENGINE-DOSSIER.md)** — the distilled, current-truth
  reference for *this* game's engine. Empty scaffold for now — engine research
  is just beginning.

The blow-by-blow development history lives in the sibling repositories
(`-dev-archive` for the messy in-progress record, `-modding-notes` for readable
field notes). This repo is the consolidated engine knowledge, not the diary.

## About the engine

Burnout Paradise runs on **Criterion Games' own proprietary in-house
engine** — this is a distinct, later engine, not licensed RenderWare,
despite Criterion's earlier RenderWare-era history. This remastered build
ships `d3dcompiler_47.dll` in its install directory, suggesting a Direct3D
11 renderer, but this has not yet been confirmed by live inspection — see
the dossier for the current verified state.

## The six repositories for Burnout Paradise VR

Everything for this game lives in six repositories, each with one job — so you
always know where to look. You are in **burnout-paradise-vr-engine-research**.

| Repository | What lives here |
| --- | --- |
| [burnout-paradise-vr-mod](https://github.com/TefMeister/burnout-paradise-vr-mod) | The mod itself — the VR conversion (cockpit-view stereo rendering + head tracking). |
| [burnout-paradise-vr-dev-archive](https://github.com/TefMeister/burnout-paradise-vr-dev-archive) | Full development history — snapshots, probes, dead ends, raw recon. |
| [burnout-paradise-vr-modding-notes](https://github.com/TefMeister/burnout-paradise-vr-modding-notes) | Readable field notes / progress ledger. |
| [burnout-paradise-vr-staging](https://github.com/TefMeister/burnout-paradise-vr-staging) 🔒 | **Private** — unverified WIP builds, cross-machine handoff. |
| **burnout-paradise-vr-engine-research** ← you are here | Distilled engine reference (dossier) + reusable VR RE playbook. |
| [burnout-paradise-vr-external-research](https://github.com/TefMeister/burnout-paradise-vr-external-research) | Ongoing public-research leads, gathered separately from hands-on modding work. |

## Status

Project started 2026-08-25. Groundwork phase: repos created, hands-on engine
research about to begin. See the dossier for the current phase and open
risks as they're found.

## Scope, ethics, and legality

- This is a **non-commercial fan project**. It requires owning a legitimate copy
  of the game and **redistributes no original game assets** — only files we
  create. See [`.gitignore`](.gitignore).
- We **credit everyone** whose work or research this builds on, and we honour
  correction/removal requests from actual rights holders. See
  [`CREDITS.md`](CREDITS.md).

## Templates

New engine? Start its dossier from
[`templates/per-engine-research-template.md`](templates/per-engine-research-template.md).

## Contributing & policy

See [CONTRIBUTING.md](CONTRIBUTING.md) — how we credit and link sources, our
**study-everything-public but write-our-own-code** rule (we copy no one else's
source code or files, any license or price), the terms for reusing our work
(free, with credit), and how to request a correction or removal.
