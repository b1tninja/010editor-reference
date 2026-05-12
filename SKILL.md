---
name: 010bt
description: >-
  Author or review SweetScape 010 Editor Binary Templates (.bt) and related
  scripts: template execution model, FTell/FSeek/Read*, startof, read=/write=,
  local hint variables, endianness, control flow in structs, limitations vs C.
  Use when the user mentions 010 Editor, Binary Templates, .bt files,
  Template Results, Pkgstream_2WIRE_SP.bt, NAND inline 2112 templates, or
  hex-template syntax in the 010editor-reference repository.
---

# 010 Editor Binary Templates (`.bt`)

## Primary documentation (read this repo first)

**Primary indexes:** [`templates.md`](templates.md) (Binary Templates), [`scripts.md`](scripts.md) (`.1sc`), and the per-page mirror [`manual/markdown/README.md`](manual/markdown/README.md).

The shorter cheat sheet [`010_TEMPLATE_AND_SCRIPTING.md`](010_TEMPLATE_AND_SCRIPTING.md) summarizes SweetScape's official manual (mirrored under **`manual/html/*.htm`**) for:

- Template vs **`.1sc`** script execution
- **Declaring variables**, **`FTell` / `FSeek`**, **`ReadUByte` / `ReadUInt`** (peek without consuming)
- **`startof(var)`**, **`BigEndian()` / `LittleEndian()`**
- **`read=` / `write=`**, **`local`**, **`optimize=false`**, **`comment=`** for Template Results hints
- **ANSI differences** (no `*`, no `goto`, array limits, preprocessor limits)
- Practical patterns aligned with **`Pkgstream_2WIRE_SP.bt`**, **`OpenTL_NAND_inline_2112.bt`**, **`S34ML_NAND_inline_2112.bt`**

## When editing templates here

1. For language/API depth, read **[`templates.md`](templates.md)** (and **[`scripts.md`](scripts.md)** if `.1sc`). For a short cheat sheet, read **[`010_TEMPLATE_AND_SCRIPTING.md`](010_TEMPLATE_AND_SCRIPTING.md)**. For a specific manual topic, open **`manual/markdown/[Topic].md`** then the linked **`manual/html/[Topic].htm`**.
2. Read the specific **`.bt`** file header comments (geometry, endianness, EOF rules).
3. Online canonical manual (if the local mirror is incomplete): [https://www.sweetscape.com/010editor/manual/](https://www.sweetscape.com/010editor/manual/).

## Repo README

Repository structure and contents: **[`README.md`](README.md)**.
