# BurnoutDecomp now builds a playable, Denuvo-free PC exe from source (needs Xbox 360 game data)

From: `/gr`, 2026-10-26 (estate sweep, CHECK-IN). Topic: `external-research/topics/2026-10-26-burnoutdecomp-now-builds-a-playable-pc-exe.md`.

**Dossier sections it touches:**
- §12: "**Denuvo Anti-Tamper** (confirmed present, 2026-08-25) is the single biggest open risk for this project".
- §11: "nobody has publicly reverse engineered `BurnoutPR.exe`'s shaders/cbuffers for stereo purposes".

**Finding** `[reported 2026-10-26, project docs]`: `BurnoutDecomp/b5-decomp` links a whole-game `Burnout_PC.exe`
(2,848 translation units, 2026-10-10), plays a 120-second max-settings Road Rage (2026-10-03), starts windowed, and
has the ARTIST debug menu (Ctrl+Space), a console, and a `config.ini` `[Debug]` section for any debug variable. Its
build refuses anything but a dumped retail **Xbox 360** game folder; Remastered is optional.

**Suggested dossier change:** add under §12 that a source-built route exists which removes Denuvo and makes stereo a
source change, at the cost of an Xbox 360 dump and a moving upstream; tag it `[reported]`. A `[USER]` question for
the board: is a retail Xbox 360 Burnout Paradise disc owned?
