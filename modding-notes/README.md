# burnout-paradise-vr — `modding-notes/`

Project notes for the Burnout Paradise Remastered VR conversion — design
docs, progress, decisions. This is one of five games started together on
2026-08-25, and the first one this project is doing hands-on reverse-
engineering work on.

## The folders for Burnout Paradise VR

Everything for this game lives in one repository, one folder per job — so you
always know where to look. You are in **`modding-notes/`**.

| Folder | What lives here |
| --- | --- |
| [`mod/`](../mod/) | The mod itself — the VR conversion (cockpit-view stereo rendering + head tracking). |
| [`dev-archive/`](../dev-archive/) | Full development history — snapshots, probes, dead ends, raw recon. |
| **`modding-notes/`** ← you are here | Readable field notes / progress ledger. |
| [staging/burnout-paradise-vr](https://github.com/TefMeister/staging/tree/main/burnout-paradise-vr) 🔒 | **Private** — unverified WIP builds, cross-machine handoff. |
| [`engine-research/`](../engine-research/) | Distilled engine reference (dossier) + reusable VR RE playbook. |
| [`external-research/`](../external-research/) | Ongoing public-research leads, gathered separately from hands-on modding work. |

## Contributing & policy

See [CONTRIBUTING.md](CONTRIBUTING.md) — how we credit and link sources, our
**study-everything-public but write-our-own-code** rule (we copy no one else's
source code or files, any license or price), the terms for reusing our work
(free, with credit), and how to request a correction or removal.
