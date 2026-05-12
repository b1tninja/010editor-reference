# 010 Editor — Binary Templates (engine index)

This document is the **hub for the Binary Template language** (`.bt` files): execution model, syntax family, variable semantics, attributes, APIs, and links into **per-page Markdown summaries** of the local SweetScape manual mirror.

| Resource | Role |
|----------|------|
| **[manual/markdown/README.md](manual/markdown/README.md)** | Alphabetical index of **all** mirrored manual topics → `[Topic].md`. |
| **[manual/markdown/MANUAL_MIRROR.md](manual/markdown/MANUAL_MIRROR.md)** | How summaries are generated from **`manual/html/*.htm`**, and how to regenerate them. |
| **[010_TEMPLATE_AND_SCRIPTING.md](010_TEMPLATE_AND_SCRIPTING.md)** | Shorter agent-oriented cheat sheet (patterns, pitfalls, `Read*` vs `FTell`). |
| **Official manual** | [https://www.sweetscape.com/010editor/manual/](https://www.sweetscape.com/010editor/manual/) |

---

## 1. What a Binary Template is

A **Binary Template** is a text file with extension **`.bt`**. When run, 010 Editor **parses the current file into variables** that appear in the **Template Results** tree. The template is **compiled**, then executed **top to bottom** like an interpreter—there is **no `main` function**.

- Each **declaration** maps the next bytes at the **current read position** to a variable (unless repositioned with attributes or `FSeek`).
- **Reading** a variable reads bytes from disk; **assigning** writes them back.
- **`struct` / `union` bodies may contain `if`, `for`, `while`, etc.**—this is *not* ANSI C; it is the template data-description language.

Sources: [IntroTempScripts.md](manual/markdown/IntroTempScripts.md), [IntroTemplates.md](manual/markdown/IntroTemplates.md), [DataEngine.md](manual/markdown/DataEngine.md).

---

## 2. Template engine capabilities (capability matrix)

| Capability | Description | Primary manual topics |
|------------|-------------|------------------------|
| **Declarative layout** | `typedef`, `struct`, primitive arrays, nested structs. | [Structs.md](manual/markdown/Structs.md), [DataTypes.md](manual/markdown/DataTypes.md) |
| **Control flow in layout** | Conditional and repeated declarations depend on prior fields. | [ControlStatements.md](manual/markdown/ControlStatements.md) |
| **Template-only variables** | `local` variables not mapped to the file (optional visibility in Results). | [TemplateVariables.md](manual/markdown/TemplateVariables.md) |
| **Repositioning** | `FSeek`, `FSkip`, `FTell`; peek with `ReadByte`/`ReadUInt`/… **without** advancing the template cursor. | [FuncIO.md](manual/markdown/FuncIO.md), [TemplateVariables.md](manual/markdown/TemplateVariables.md) |
| **Absolute / relative placement** | Attributes `pos`, `localpos` (v16+ for some attribute forms—see HTML). | [TemplateVariables.md](manual/markdown/TemplateVariables.md) |
| **Endian control** | `BigEndian()`, `LittleEndian()` and per-file endian. | [FuncIO.md](manual/markdown/FuncIO.md), [ByteOrdering.md](manual/markdown/ByteOrdering.md) |
| **Display & UX** | `format=`, `fgcolor`, `bgcolor`, `style`, `comment`, `name`, `open`, `hidden`, `edit`, `warn`. | [TemplateVariables.md](manual/markdown/TemplateVariables.md) |
| **Custom serialization** | `read=` / `write=` on typedefs and structs (custom **string** view in Results). | [CustomVariables.md](manual/markdown/CustomVariables.md) |
| **Inline attributes (v12+)** | `Str(...)`, expressions, `this`, `value` for write. | [TemplateVariables.md](manual/markdown/TemplateVariables.md), [CustomVariables.md](manual/markdown/CustomVariables.md) |
| **On-demand / sized blocks** | `size=` for lazy or fixed-skip structures (large files). | [OnDemand.md](manual/markdown/OnDemand.md) |
| **Optimized arrays** | Duplicates, `optimize=`, memory/performance tradeoffs. | [ArraysDuplicates.md](manual/markdown/ArraysDuplicates.md) |
| **Bitfields** | Packed bits, optional auto checkboxes, padding modes. | [Bitfields.md](manual/markdown/Bitfields.md), [FuncIO.md](manual/markdown/FuncIO.md) |
| **Disassembly columns** | `disasm=` metadata in templates. | [DisassemblerTemplates.md](manual/markdown/DisassemblerTemplates.md) |
| **Repository & UI** | Installing/running templates from the app. | [MenuTemplates.md](manual/markdown/MenuTemplates.md), [OptionsTemplates.md](manual/markdown/OptionsTemplates.md), [RepositoryDialog.md](manual/markdown/RepositoryDialog.md), [Running.md](manual/markdown/Running.md) |
| **Compiler diagnostics** | Warnings, empty structs, etc. | [OptionsCompiling.md](manual/markdown/OptionsCompiling.md), [TemplateLimitations.md](manual/markdown/TemplateLimitations.md) |
| **Syntax highlighting for `.bt`** | Writing template syntaxes (advanced). | [WritingSyntaxes.md](manual/markdown/WritingSyntaxes.md), [WritingTreesitter.md](manual/markdown/WritingTreesitter.md), [Syntax.md](manual/markdown/Syntax.md), [Treesitter.md](manual/markdown/Treesitter.md) |

---

## 3. Language surface (shared with scripts)

Templates and scripts share a **C-like** expression and control-flow language. The manual splits **variable declaration rules** (template vs script) but shares:

| Topic | Purpose |
|-------|---------|
| [Expressions.md](manual/markdown/Expressions.md) | Operators, literals, casts, `this`, scoping in attributes. |
| [DataTypes.md](manual/markdown/DataTypes.md) | Primitive types, typedefs, enums. |
| [Structs.md](manual/markdown/Structs.md) | Aggregates; template structs may contain control flow. |
| [ArraysStrings.md](manual/markdown/ArraysStrings.md) | Strings and character arrays. |
| [ArraysDuplicates.md](manual/markdown/ArraysDuplicates.md) | Arrays, duplicate runs, optimization. |
| [ControlStatements.md](manual/markdown/ControlStatements.md) | `if`/`else`, `for`, `while`, `switch`, `break`, `continue` — note **`goto` unsupported**. |
| [Functions.md](manual/markdown/Functions.md) | Declaring and calling functions; `&` reference parameters for custom attribute functions. |
| [Sizeof.md](manual/markdown/Sizeof.md) | `sizeof` (limited for non-simple structs); **`startof(var)`** file address in **local coordinates**. |
| [Preprocessor.md](manual/markdown/Preprocessor.md) | `#define`, `#ifdef`, … — **`#if` unsupported**; macro limitations per manual. |
| [Includes.md](manual/markdown/Includes.md) | Including shared headers. |
| [TemplateLimitations.md](manual/markdown/TemplateLimitations.md) | **No `*` pointers**, no multi-dimensional arrays, etc. |

---

## 4. Template variable declaration (deep link)

The authoritative reference for **what can appear after a variable** in angle brackets is:

**[TemplateVariables.md](manual/markdown/TemplateVariables.md)** — sections include:

- **Special attributes** — `format`, colors, `style`, `comment`, `name`, `open`, `hidden`, `read`, `write`, `size`, `edit`, `pos`, `localpos`, `optimize`, `disasm`, `warn`, endian, etc. (exact availability by version is versioned in the HTML).
- **Attribute functions and inline expressions** — function vs `(expression)` forms.
- **Positioning** — `FTell`/`FSeek` equivalence vs `pos` / `localpos`.
- **Local vs file-backed** — `local` keyword.
- **Variable editors** — `edit=check|color|flags|none`.
- **Local vs file coordinates** — processes / custom start addresses; `AddressFileToLocal` / `AddressLocalToFile` in [FuncInterface.md](manual/markdown/FuncInterface.md).

---

## 5. Custom variables (`read=` / `write=`)

**[CustomVariables.md](manual/markdown/CustomVariables.md)** covers:

- typedef-level **`read=`** and optional **`write=`** turning any type into a **string display** (and optional round-trip edit).
- **Struct read** functions `string Fn(MYSTRUCT &s)` for one-line summaries.
- **Array read/write** patterns; inline `this[0]`… in v12+.
- **Error behavior** — runtime errors show `(error)` until the template is fixed.

---

## 6. Runtime library (templates + scripts)

All of these function catalogs apply **both** to templates and scripts:

| Manual | Typical use in templates |
|--------|---------------------------|
| [FuncIO.md](manual/markdown/FuncIO.md) | `FileSize`, `FTell`, `FSeek`, `ReadUByte`, `ReadUInt`, `BigEndian`, bitfield helpers, binary conversion. |
| [FuncString.md](manual/markdown/FuncString.md) | `SPrintf`, `Str`, parsing, `SScanf`. |
| [FuncMath.md](manual/markdown/FuncMath.md) | Math helpers. |
| [FuncInterface.md](manual/markdown/FuncInterface.md) | Editor/UI: carets, selections, dialogs, address mapping, file tabs. |
| [FuncTools.md](manual/markdown/FuncTools.md) | Higher-level tools (checksums, etc.—see HTML index). |

---

## 7. Template-specific manual pages (curated list)

These pages are **most directly** about templates, template UI, or template syntax infrastructure:

| Markdown | Topic |
|----------|--------|
| [IntroTemplates.md](manual/markdown/IntroTemplates.md) | Topic list for writing templates. |
| [IntroTempScripts.md](manual/markdown/IntroTempScripts.md) | Templates vs scripts; first example struct. |
| [TemplateVariables.md](manual/markdown/TemplateVariables.md) | Declaring template variables and attributes. |
| [TemplateResults.md](manual/markdown/TemplateResults.md) | Working with the Template Results panel. |
| [TemplateLimitations.md](manual/markdown/TemplateLimitations.md) | Non-ANSI restrictions. |
| [CustomVariables.md](manual/markdown/CustomVariables.md) | `read=` / `write=`. |
| [OnDemand.md](manual/markdown/OnDemand.md) | On-demand / `size=` structures. |
| [DisassemblerTemplates.md](manual/markdown/DisassemblerTemplates.md) | Disassembly in templates. |
| [MenuTemplates.md](manual/markdown/MenuTemplates.md) | Templates menu. |
| [OptionsTemplates.md](manual/markdown/OptionsTemplates.md) | Template options (auto-run, etc.). |
| [OptionsCompiling.md](manual/markdown/OptionsCompiling.md) | Compiler / warning options. |
| [WritingSyntaxes.md](manual/markdown/WritingSyntaxes.md) | Writing template syntax highlighters. |
| [WritingTreesitter.md](manual/markdown/WritingTreesitter.md) | Tree-sitter syntax definitions. |
| [EditingWithScripts.md](manual/markdown/EditingWithScripts.md) | Scripts modifying template variables. |

---

## 8. Scripts touch-points (templates only as consumer)

| Markdown | Why templates care |
|----------|-------------------|
| [Running.md](manual/markdown/Running.md) | How templates and scripts are executed from the UI. |
| [Debug.md](manual/markdown/Debug.md) | Debugger for template/script development. |
| [ScriptDLL.md](manual/markdown/ScriptDLL.md) | External DLL functions (available to **both**). |

For **script-first** topics, see **[scripts.md](scripts.md)**.

---

## 9. Full manual mirror index

Every mirrored `.htm` page has a sibling **`manual/markdown/[Stem].md`** file. The complete list (141 topics) is:

**[manual/markdown/README.md](manual/markdown/README.md)**

That list includes **hex editor**, **find/replace**, **printing**, **options**, **menus**, etc. Those pages are not template-language core, but they document the **environment** in which templates run.

---

## 10. Examples in this repository

| Template | Demonstrates |
|----------|----------------|
| [Pkgstream_2WIRE_SP.bt](Pkgstream_2WIRE_SP.bt) | `BigEndian`, `while` + peek loop, conditional `if (length)`, `local string` + `read=`, zero-byte postfix struct. |
| [OpenTL_NAND_inline_2112.bt](OpenTL_NAND_inline_2112.bt), [S34ML_NAND_inline_2112.bt](S34ML_NAND_inline_2112.bt) | `<size=2112>` on-demand pages, bitfield checkboxes, struct `read=` summaries, `ReadUByte(startof(...)+offset)` spare hints. |

---

## 11. Regenerating `manual/markdown/*.md`

```powershell
Set-Location D:\electronics\010editor-reference
python tools\gen_manual_md.py
```

---

## 12. Copyright

010 Editor and the manual text are **Copyright SweetScape Software**. The HTML mirror and derived Markdown summaries exist in this repo for **offline engineering reference** only.
