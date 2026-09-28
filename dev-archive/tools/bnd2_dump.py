"""Read a Burnout Paradise Remastered 'bnd2' bundle (e.g. SHADERS.BNDL) without the game running.

Lists every resource (id, type, name from the bundle's own debug string table) and, with --out,
writes each resource's decompressed blocks and any DXBC shader found inside them to a folder.
The output is game content: keep it OUT of git.

Layout (public Burnout community documentation of Bundle 2, checked against this file's header):
  header: magic 'bnd2', u32 version, u32 platform, u32 debugDataOffset, u32 resourceCount,
          u32 resourceEntriesOffset, u32 resourceDataOffsets[3], u32 flags
  entry (64 bytes): u64 id, u64 importHash, u32 uncompSizeAlign[3], u32 diskSizeAlign[3],
          u32 diskOffset[3], u32 importOffset, u32 typeId, u16 importCount, u8 flags, u8 streamIndex
  flags bit 0 = compressed (zlib per block); the top 4 bits of a size word are the alignment.

Usage: python bnd2_dump.py SHADERS.BNDL [--out DIR]
"""
import re
import struct
import sys
import zlib
from pathlib import Path

ENTRY_SIZE = 64
SIZE_MASK = 0x0FFFFFFF


def read_bundle(path):
    data = Path(path).read_bytes()
    if data[:4] != b"bnd2":
        raise SystemExit(f"{path}: not a bnd2 bundle (magic {data[:4]!r})")
    (version, platform, dbg_off, count, entries_off,
     d0, d1, d2, flags) = struct.unpack_from("<9I", data, 4)
    names = {}
    if dbg_off:
        end = data.find(b"</ResourceStringTable>", dbg_off)
        xml = data[dbg_off:end].decode("latin-1", "replace")
        for rid, typ, name in re.findall(r'<Resource id="([0-9a-fA-F]+)" type="([^"]*)" name="([^"]*)"', xml):
            names[int(rid, 16)] = (typ, name)
    entries = []
    for i in range(count):
        o = entries_off + i * ENTRY_SIZE
        rid, imp_hash = struct.unpack_from("<QQ", data, o)
        uncomp = struct.unpack_from("<3I", data, o + 16)
        disk = struct.unpack_from("<3I", data, o + 28)
        offs = struct.unpack_from("<3I", data, o + 40)
        imp_off, type_id = struct.unpack_from("<2I", data, o + 52)
        imp_count, eflags, stream = struct.unpack_from("<HBB", data, o + 60)
        entries.append(dict(id=rid, type=type_id, uncomp=uncomp, disk=disk, offs=offs,
                            name=names.get(rid, ("?", "?"))))
    return data, dict(version=version, platform=platform, count=count, flags=flags,
                      data_offsets=(d0, d1, d2)), entries


def blocks(data, hdr, e):
    compressed = hdr["flags"] & 1
    for b in range(3):
        size = e["disk"][b] & SIZE_MASK
        if not size:
            yield b, b""
            continue
        start = hdr["data_offsets"][b] + e["offs"][b]
        raw = data[start:start + size]
        yield b, zlib.decompress(raw) if compressed else raw


def dxbc_blobs(buf):
    i = buf.find(b"DXBC")
    while i >= 0:
        total = struct.unpack_from("<I", buf, i + 24)[0] if i + 28 <= len(buf) else 0
        if 32 <= total <= len(buf) - i:
            yield i, buf[i:i + total]
            i = buf.find(b"DXBC", i + total)
        else:
            i = buf.find(b"DXBC", i + 4)


def main():
    if len(sys.argv) < 2:
        raise SystemExit(__doc__)
    path = sys.argv[1]
    out = Path(sys.argv[sys.argv.index("--out") + 1]) if "--out" in sys.argv else None
    data, hdr, entries = read_bundle(path)
    print(f"version {hdr['version']} platform {hdr['platform']} flags {hdr['flags']:#x} "
          f"resources {hdr['count']}")
    by_type = {}
    for e in entries:
        by_type.setdefault((e["type"], e["name"][0]), []).append(e)
    for (t, tname), es in sorted(by_type.items()):
        print(f"  type {t:#06x} {tname:<28} {len(es)}")
    shader_count = 0
    for e in entries:
        for b, buf in blocks(data, hdr, e):
            for off, blob in dxbc_blobs(buf):
                shader_count += 1
                if out:
                    out.mkdir(parents=True, exist_ok=True)
                    safe = re.sub(r"[^A-Za-z0-9_.-]+", "_", e["name"][1])[-80:]
                    (out / f"{e['id']:016x}_{safe}_b{b}_{off:x}.dxbc").write_bytes(blob)
    print(f"DXBC shaders found: {shader_count}")


if __name__ == "__main__":
    main()
