# 2026-08-25 — First live launch attempt: blocked, but not by us

Deployed the M0 proxy DLL (`d3d11.dll`, see `burnout-paradise-vr-staging/proxy-d3d11/`) to
the game folder and asked the user to launch normally via Steam, per the collaborative
live-test protocol.

## What happened

**Attempt 1 (proxy DLL present):** Steam showed *"Failed to start process for this game:
'The operation was canceled by the user.' (0x4C7)"*. No log file appeared at all, meaning
our proxy's own code never ran.

Checked on our end before asking for another live attempt: the deployed DLL was untouched on
disk (not quarantined by antivirus — Windows Defender's operational log showed nothing but
routine health-check entries around that time), and the Application/System event logs showed
no crash or block event either. Also confirmed via the exe's actual PE import table that
`d3d11.dll` isn't a *static* dependency of `BurnoutPR.exe` at all — the only static import is
`Core/Activation.dll` (EA's own licensing library) — so a missing export in our proxy
couldn't have caused a process-creation-time failure either.

**Control test:** renamed the proxy DLL aside (not deleted) and asked for a second launch
attempt, completely proxy-free.

**Attempt 2 (no proxy DLL at all):** a *different* error — a Windows "Application not found"
dialog for a `link2ea://launchgame/1238080?platform=steam&theme=bprm` URI.

## What this actually means

Both errors trace back to the same root cause, and it has nothing to do with our mod: **this
Steam copy of Burnout Paradise Remastered still hands the actual launch off to EA's own
"Link2EA" protocol**, which requires the **EA App** to be installed and registered as the
handler for `link2ea://` URIs. It isn't installed on this machine, so Windows has nothing to
open that link with. The first error was almost certainly the same underlying failure,
just surfaced differently by Steam's wrapper.

**Our proxy DLL is cleared of suspicion** — it was restored to the game folder afterward,
since there's no evidence it did anything wrong. We simply can't get far enough into the
launch sequence yet to find out whether it loads correctly.

## Next step

Not a modding task — this needs the **EA App** installed and the account linked to this
game's entitlement before any further live testing is possible. Once that's done, the same
launch test (with the proxy DLL in place) can be retried.
