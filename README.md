# Burnout Paradise VR

A VR conversion mod for **Burnout Paradise Remastered** (2018 remaster of the
2008 original, Criterion Games / Stellar Entertainment) — the goal is
cockpit-view racing with real head tracking, not a flat screen bolted into a
headset.

> **Status: work in progress — nothing playable released yet, no code
> written yet.** Repos have just been created; engine research is about to
> begin. This repository will hold releases only; watch it if you want to
> know the moment there is something to try.

## What this will be

Burnout Paradise runs on Criterion's own proprietary in-house engine — not
licensed RenderWare, despite Criterion's earlier RenderWare-era history; this
is a distinct, later in-house engine. How the VR conversion is built (proxy
DLL, hook point, render path) is still to be determined by the engine
research this project starts with. As with our other conversions, the
playable mod is almost the by-product — the real goal is the knowledge
gained on the way there, written down and shared so anyone can do the same
for any game. See the
[engine dossier](https://github.com/TefMeister/burnout-paradise-vr-engine-research)
and the cross-engine
[flat-to-VR library](https://github.com/TefMeister/flat-to-vr-cross-engine-research).

Driving games carry an extra motion-sickness risk beyond the usual VR
concerns — a mismatch between visual motion and vestibular sense is
especially pronounced at racing speeds — so comfort options will be a first-
class concern here, not an afterthought.

## What you will need

- Your own legitimate copy of **Burnout Paradise Remastered** (this mod
  contains **no** game files).
- A PC VR headset (target runtime to be decided during engine research).

## The six repositories for Burnout Paradise VR

Everything for this game lives in six repositories, each with one job — so you
always know where to look. You are in **burnout-paradise-vr-mod**.

| Repository | What lives here |
| --- | --- |
| **burnout-paradise-vr-mod** ← you are here | The mod itself — the VR conversion (cockpit-view stereo rendering + head tracking). |
| [burnout-paradise-vr-dev-archive](https://github.com/TefMeister/burnout-paradise-vr-dev-archive) | Full development history — snapshots, probes, dead ends, raw recon. |
| [burnout-paradise-vr-modding-notes](https://github.com/TefMeister/burnout-paradise-vr-modding-notes) | Readable field notes / progress ledger. |
| [burnout-paradise-vr-staging](https://github.com/TefMeister/burnout-paradise-vr-staging) 🔒 | **Private** — unverified WIP builds, cross-machine handoff. |
| [burnout-paradise-vr-engine-research](https://github.com/TefMeister/burnout-paradise-vr-engine-research) | Distilled engine reference (dossier) + reusable VR RE playbook. |
| [burnout-paradise-vr-external-research](https://github.com/TefMeister/burnout-paradise-vr-external-research) | Ongoing public-research leads, gathered separately from hands-on modding work. |

## Credits, scope, and legality

Non-commercial fan project; requires an owned copy; redistributes no original
assets. We credit everyone whose work this builds on — see
[`CREDITS.md`](CREDITS.md) — and we honour correction/removal requests from
rights holders promptly.

## Contributing & policy

See [CONTRIBUTING.md](CONTRIBUTING.md) — how we credit and link sources, our
**study-everything-public but write-our-own-code** rule (we copy no one else's
source code or files, any license or price), the terms for reusing our work
(free, with credit), and how to request a correction or removal.
