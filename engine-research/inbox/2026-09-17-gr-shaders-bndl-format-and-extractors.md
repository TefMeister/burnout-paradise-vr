# From /gr: the `SHADERS.BNDL` board row now has a checked lead

**From:** `/gr` estate sweep, 2026-09-17.

Board `[PD]` row: *"Pull the shaders out of `SHADERS.BNDL` … public Burnout bundle documentation exists
`[hypothesis — not checked]`."* Checked:

- The Burnout Wiki documents the Bundle 2 container, and its Resource Types page lists
  **`RwShaderProgramBuffer` (`0x12`)** for PC and Remastered `[reported]`, which is most likely where the
  compiled shaders sit `[hypothesis]`.
- Two public extractors exist: **YAP** (burninrubber0: raw `.dat` resources plus YAML) and **Bundle
  Manager** `[reported]`. Whether either opens the Remaster's bundles is unchecked.

Suggested board change: drop "needs the bundle format worked out first" and replace it with "try YAP
or Bundle Manager on `SHADERS.BNDL`, then read the `0x12` resources".

→ `external-research/topics/2026-09-17-bundle-2-docs-and-extractors-for-the-shader-pull.md`
