# 2026-09-28 — State-o-matiC's first live run, on Burnout Paradise

While Menu-o-matiC drove the game from launch to the city, State-o-matiC watched every ~5 s (2 s of looks each).
The full timeline is in the session write-up; the pattern, against what the route was doing:

| What was on screen | Verdict | Deciding sign |
| --- | --- | --- |
| intro / title / save notice | moving, cutscene (bars), menu or loading screen | motion, letterbox |
| the two loading screens | **loading** | disk 30 to 74 MB/s |
| main menu | menu or loading screen | only a small patch moved |
| vehicle, car and paint screens | moving / cutscene | a 3D car moves behind the menu: a TAUGHT screen is needed here |
| parked in the city, nothing moving | still, then "menu or loading screen" | picture exactly unchanged; a key that visibly moves the camera, or a taught screen, is needed |
| idle cinematic camera | **cutscene** | black bars |
| throttle held | moving | motion 0.2 |

A tap of W during the idle cinematic changed the picture (poke answer 0.11); a tap of A while parked changed
nothing. Since then, a still picture that answers a key is judged "gameplay". `[verified-live 2026-09-28, n=1 run]`
