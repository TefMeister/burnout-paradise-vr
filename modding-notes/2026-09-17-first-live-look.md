# 2026-09-17 — first live look: Burnout Paradise Remastered

Home PC `RTX`, `/lm` session. The user asked for a first look at six games: does each run, and does it still run with our own file added.

## Does it run?

Launches via Steam → EA app on the user's account and reaches the MAIN MENU (Enter Paradise City / Start a Party / Big Surf Island / Quit) `[verified-live 2026-09-17, n=3 launches]`. The EA app takes ~140 s to hand over on a cold start, ~6 s when already running.

## With our file added

⭐ **OUR DLL SURVIVES DENUVO.** A full-export 32-bit `d3d11.dll` proxy (`staging/burnout-paradise-vr/proxy-d3d11-full/`) in `BurnoutPR\` loaded, resolved 51/51 real exports and logged `D3D11CreateDeviceAndSwapChain`; the game played its intro and reached the main menu `[verified-live 2026-09-17, n=3]`. That answers this project's ⭐ open question. The old 2-export proxy was replaced (kept locally, not needed). Only `D3D11CreateDeviceAndSwapChain` was called, so the swap chain comes from that one call — the natural place to hook `Present` next `[verified-live 2026-09-17, n=3]`.

## Windowed mode

`%LOCALAPPDATA%\Criterion Games\Burnout Paradise Remastered\config.ini` `[Display]` `Width=1280`, `Height=720`, `WindowMode=1` → a 1280×720 client window `[verified-live 2026-09-17, n=1]`. `WindowMode=2` = borderless, sized to the desktop work area `[verified-live 2026-09-17, n=1]`; the shipped `0` gave full 3440×1440 `[measured 2026-09-17]`. Backup: `config.ini.bak-2026-09-17`.

## How it was driven

Intro: Enter skips. First run shows a save-icon notice (Enter) and a Windows Firewall prompt (pressed Cancel — online play only). Main menu: arrow keys + Enter. Quit → `LEAVE PARADISE?` → Enter = Yes. `WM_CLOSE` also exits cleanly.

## Not established

- Nothing past the menus: no gameplay was loaded, no camera data read.
- Every result is from one machine (`RTX`, 21:9 desktop) on one day.

## Next

- [PD] ⭐ **Add a swap-chain `Present` + constant-buffer logger to the shared proxy generator** (32-bit path), so a FLAT run can list which cbuffers change when the camera moves (dossier §6/§7). Denuvo is no longer the blocker.
- [FLAT] run that logger in windowed 1280×720, drive into Paradise City, turn the camera, and read which cbuffer carries the view/projection
- [PD] **Pull the shaders out of `SHADERS.BNDL` without the game running** and read which constant buffers the world shaders use versus the sky/particle shaders (vorpX 3D-ed only the second group — dossier §6). Needs the bundle format worked out first; public Burnout bundle documentation exists `[hypothesis — not checked]`.
