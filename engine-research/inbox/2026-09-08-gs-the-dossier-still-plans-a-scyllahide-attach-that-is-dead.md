# §4's attach plan is dead, and the only correction lives in a lane the modding session may not read

**From:** `/gs` (twenty-sixth sweep, 2026-09-08) · **For:** the modding lane, to fold into
`ENGINE-DOSSIER.md` **§4** (the "Attach workflow that works" bullet)

Supersedes: `burnout-paradise-vr/engine-research/ENGINE-DOSSIER.md` §4 — the "Attach workflow that works" bullet, specifically its **Plan (external-research, 2026-08-25)** clause "load the **ScyllaHide** x64dbg plugin … before assuming Denuvo blocks attach outright"

## The claim that is still live and is now known wrong

`ENGINE-DOSSIER.md:45`, verbatim and unchanged:

> **Plan (external-research, 2026-08-25):** load the **ScyllaHide** x64dbg plugin (legitimate,
> open-source, already the standard "first thing to try" against usermode anti-debug per the RE
> community) before assuming Denuvo blocks attach outright.

That plan cannot be executed, for three separate reasons, none of which is Denuvo:

1. **ScyllaHide is ABI-incompatible with the x64dbg build in use** — `objdump`-verified by
   `mad-max-vr`, 2026-08-25.
2. **Upstream is dormant** — v1.4 (2023-03-24) is still the latest release and `master` has been
   untouched since 2023-07-29 `[verified-live 2026-09-07, GitHub API]`. No fix is coming.
3. **The only remaining route makes things worse estate-wide** — downgrading x64dbg to ScyllaHide's
   legacy `TitanRegisterPlugin` ABI would break **`x64dbg-automate`**, the bridge every project on
   the account drives the debugger through `[inferred-static 2026-09-07]`.

⭐ **The workable shape, if this is ever wanted:** a **second, pinned-old x64dbg install** kept
apart from the automation one. The machine already has two installs, so this is configuration, not
new work.

## Why this needed a drop rather than being already handled

**It has been correctly researched — the problem is purely one of lane.** `/gr` wrote all of the
above into this project's **`external-research/INDEX.md:3`** on 2026-09-07, accurately and in
detail, and closed with: *"Written up and filed in `mad-max-vr`, where the measurement lives;
deliberately not duplicated here."*

That decision was right for `/gr`'s own lane and wrong for the reader, because:

- `ENGINE-DOSSIER.md` is the **modding lane's** file. `/gr` may not edit it, so the correction
  could not travel the last step on its own.
- The dossier carries **no pointer** to the INDEX entry. A session that opens the dossier — the
  normal thing to do when picking a project up — sees a confident, dated plan and no hint it is dead.
- **This project is IDLE**, which makes the failure *more* likely, not less: an idle project is
  read cold, by a session with no memory of the 09-07 research, months later.

This is the exact shape `/gs` exists to catch, and it is the second instance this sweep of a
correction that exists but never reached the curated doc it corrects (the other:
`far-cry-2-vr` §AER's "last activity 2019-11-23", wrong for six consecutive sweeps).

## Suggested edit

Replace the plan clause with the finding, keep the tag, and point at where the measurement lives —
`mad-max-vr/engine-research/ENGINE-DOSSIER.md` — rather than restating it. One or two lines is
enough; the full write-up should not be copied a third time.

**What is NOT claimed here:** nothing about whether Denuvo actually blocks attach on
`BurnoutPR.exe`. That is still untested and stays open. Only the *tool* named in the plan is dead.

## Not filed, deliberately

The related estate-wide item — proxies that load the real system module by path and never
`FreeLibrary` it — is **already fully curated** in
`flat-to-vr-cross-engine-research/docs/techniques/README.md` (mechanism, the `DllMain`
third-parameter guard, the renamed-copy alternative, and the confirmed-live fix). It needs no drop
anywhere; it needs applying, per project.
