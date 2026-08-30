# 2026-08-25 — Project paused: EA App/Origin blocks launch, no viable path right now

Wrapping up today's session in plain terms, since this ended differently than expected.

## The short version

We can't currently get Burnout Paradise Remastered to launch at all on this machine — not
because of anything our mod did, but because the game itself requires the EA App/Origin to
be installed and linked, and every avenue around that turned out to be closed:

- **Direct-exe launch** (skipping Steam's own launcher) still demands Origin — the check is
  built into the game's own code, not just Steam's launch button.
- **The older, non-remastered Steam release** (`Burnout Paradise: The Ultimate Box`), which
  genuinely doesn't need any EA launcher, would have solved this cleanly — but it's been
  delisted from Steam and isn't owned on this account, so it's simply not available anymore.
- **Recovering EA account access** (a password reset would normally be the easy fix) isn't
  possible either, since the email address tied to that old account is also no longer
  accessible.
- **Patching the check out of the exe** was considered and explicitly declined — not for lack
  of technical means, but because it's a genuinely different, legally riskier act than
  everything else this portfolio does (see `ENGINE-DOSSIER.md` §4 for the full reasoning).
  Every other VR mod here changes how an already-unlocked game renders; this would be
  removing the mechanism that decides whether the game considers itself licensed at all —
  not something to do even on a legitimately owned copy.

## What doesn't need to be redone later

Nothing technical here was wasted. The D3D11 confirmation, the Denuvo findings, the
external-research leads (BurnoutDecomp, the community injection precedent, ScyllaHide,
3Dmigoto), and the from-scratch proxy DLL (built clean, staged, just never successfully
tested live) are all still exactly as good as they were this morning. If EA account access
ever comes back, or Ultimate Box ever becomes available again, this project picks up right
where it left off — no do-overs needed.

## Portfolio-wide lesson

Going forward, game selection for this whole portfolio should lean toward Steam/Epic/GOG
titles (or old, freely-downloadable games) that don't gate launch behind a third-party
publisher account. This isn't unique to EA — the same logic would apply to any
launcher-account requirement. Recorded in the cross-machine `PREFERENCES.md` so it informs
future picks, not just this one.

## Status

Paused, not abandoned. Moving on to Mad Max VR next.
