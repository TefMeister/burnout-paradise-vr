# Pulling shaders out of `SHADERS.BNDL`: the Bundle 2 format is documented, and two extractors exist

**Status:** 🆕 new · **Priority:** medium — it turns the board's `[PD]` row "work out the bundle
format first; public documentation exists `[hypothesis — not checked]`" into a checked lead.

## What was found

- **The format is documented.** The Burnout Wiki's "Bundle 2/Burnout Paradise" page describes the
  container: per-resource entries with ID, uncompressed and compressed size, alignment, offset and
  type, plus import offsets for resources that pull data from other resources. Its notes name the PC
  platform constant as "reused for all platforms in Remastered" `[reported]`. Wiki text is
  CC BY-SA 4.0.
- **Shader resource types are listed** on the wiki's "Resource Types" page. For PC and Remastered the
  relevant one is **`RwShaderProgramBuffer` (type `0x12`)**, noted as not used by the original PC game;
  the `Shader` / `ShaderTechnique` types (`0x32`) are listed as PS3 and Xbox 360 only `[reported]`.
  So on the Remaster the compiled shader programs most likely sit in `0x12` resources `[hypothesis]`.
- **Two public extractors:** **Bundle Manager** (BurnoutHints / burninrubber0), a program for working
  with Paradise bundles, and **YAP** by **burninrubber0**, which splits a bundle into raw `.dat`
  resources plus YAML metadata and repacks them `[reported]`. ⚠️ YAP's README says it supports
  "Bundle 2 version 2, the version used in Burnout Paradise"; whether that includes the Remaster's
  files is **unchecked**. Neither tool decodes shaders; they only get the resources out.

## Why it matters here

vorpX's geometry 3D stereoised the sky, particles and lights but not the world
(`2026-09-11-vorpx-does-hook-the-remaster-but-its-geometry-3d-misses-the-world.md`). Reading which
constant buffers the world shaders use versus the sky and particle shaders is how to find the
projection the world pass really takes. That needs the shaders out of the bundle first.

## Next step

`[PD]`: read the two wiki pages in full, then check whether YAP or Bundle Manager opens the
Remaster's `SHADERS.BNDL` (use the public tool as a tool; copy none of its code). If it does, the
`0x12` resources are the compiled shaders to disassemble and compare.

## Sources

- https://burnout.wiki/wiki/Bundle_2/Burnout_Paradise
- https://burnout.wiki/wiki/Resource_Types
- https://github.com/burninrubber0/YAP
- https://github.com/burninrubber0/Bundle-Manager
