# 2026-10-07 — night on demand, and the headlight pass seen per eye

`[verified-live 2026-10-07, n=1]`, dev PC. d3d11 `eded7cf60d0c` (headlight per eye + day/night readout).

- **Night via the game's own menu**: Esc → F2 (Under the Hood) → Game Options → TIME OF DAY: 48 minute day / 2 hour
  day / 24 hour day / Match local time / Midday / **Midnight** → Backspace → Save Changes? Yes. It sticks across a
  restart (clock shows 12:00 am). `night-via-menu.png`.
- The `daynight` readout says NIGHT (sky top luma ~0.003).
- **Headlight pool**: 0 draws while parked at first; after driving a few metres, ~120 draws/s (constants
  `g_headlightConstants.x` 0.1, depthConversion.w ~6.1). With numpad 5 (shift) on: `headlight: first edited upload
  (per eye on)` — the per-eye edit now runs.
- **Not judged**: whether the pool stays on the same patch of road under the shift. When the car stops the camera
  swings round to its idle view, so on/off pictures are taken from different angles (`shift-off-on-camera-swung.png`).
  Needs a spot where the car faces a wall/road under steady camera — Tefa drives there and hands over.
- Numpad keys: NumLock on; send them as virtual keys (scancode-only 0x4C did toggle once, keybd_event VK_NUMPAD5
  works reliably).
