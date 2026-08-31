# Burnout Paradise Remastered — VR Engine Research

Engine research toward a VR conversion of **Burnout Paradise Remastered**
(2018 remaster of the 2008 original, Criterion Games / Stellar
Entertainment) — cockpit-view stereo rendering and head tracking are the
goal.

This folder holds two things:

- **[`PLAYBOOK.md`](PLAYBOOK.md)** — a reusable, engine-agnostic, point-by-point
  method for taking *any* game whose engine nobody has converted to VR and
  getting it there. It is oriented around one North Star: **the game rendering
  in a headset with head tracking**, with everything else built on top. The same
  playbook is copied into each of our VR projects' research repos.
- **[`ENGINE-DOSSIER.md`](ENGINE-DOSSIER.md)** — the distilled, current-truth
  reference for *this* game's engine. Empty scaffold for now — engine research
  is just beginning.

The blow-by-blow development history lives in the sibling folders
(`-dev-archive` for the messy in-progress record, `-modding-notes` for readable
field notes). This repo is the consolidated engine knowledge, not the diary.

## About the engine

Burnout Paradise runs on **Criterion Games' own proprietary in-house
engine** — this is a distinct, later engine, not licensed RenderWare,
despite Criterion's earlier RenderWare-era history. This remastered build
ships `d3dcompiler_47.dll` in its install directory, suggesting a Direct3D
11 renderer, but this has not yet been confirmed by live inspection — see
the dossier for the current verified state.

## The folders for Burnout Paradise VR

Everything for this game lives in one repository, one folder per job — so you
always know where to look. You are in **`engine-research/`**.

| Folder | What lives here |
| --- | --- |
| [`mod/`](../mod/) | The mod itself — the VR conversion (cockpit-view stereo rendering + head tracking). |
| [`dev-archive/`](../dev-archive/) | Full development history — snapshots, probes, dead ends, raw recon. |
| [`modding-notes/`](../modding-notes/) | Readable field notes / progress ledger. |
| [staging/burnout-paradise-vr](https://github.com/TefMeister/staging/tree/main/burnout-paradise-vr) 🔒 | **Private** — unverified WIP builds, cross-machine handoff. |
| **`engine-research/`** ← you are here | Distilled engine reference (dossier) + reusable VR RE playbook. |
| [`external-research/`](../external-research/) | Ongoing public-research leads, gathered separately from hands-on modding work. |

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
