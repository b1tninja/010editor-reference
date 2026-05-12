# 010 Editor — Binary Templates (engine index)

This document is the **hub for the Binary Template language** (`.bt` files): execution model, syntax family, variable semantics, attributes, APIs, and links into **per-page Markdown summaries** of the local SweetScape manual mirror.

| Resource | Role |
|----------|------|
| **[manual_md/README.md](manual_md/README.md)** | Alphabetical index of **all** mirrored manual topics → `[Topic].md`. |
| **[manual_md/MANUAL_MIRROR.md](manual_md/MANUAL_MIRROR.md)** | How summaries are generated from **`manual/*.htm`**, and how to regenerate them. |
| **[010_TEMPLATE_AND_SCRIPTING.md](010_TEMPLATE_AND_SCRIPTING.md)** | Shorter agent-oriented cheat sheet (patterns, pitfalls, `Read*` vs `FTell`). |
| **Official manual** | [https://www.sweetscape.com/010editor/manual/](https://www.sweetscape.com/010editor/manual/) |

---

## 1. What a Binary Template is

A **Binary Template** is a text file with extension **`.bt`**. When run, 010 Editor **parses the current file into variables** that appear in the **Template Results** tree. The template is **compiled**, then executed **top to bottom** like an interpreter—there is **no `main` function**.

- Each **declaration** maps the next bytes at the **current read position** to a variable (unless repositioned with attributes or `FSeek`).
- **Reading** a variable reads bytes from disk; **assigning** writes them back.
- **`struct` / `union` bodies may contain `if`, `for`, `while`, etc.**—this is *not* ANSI C; it is the template data-description language.

Sources: [IntroTempScripts.md](manual_md/IntroTempScripts.md), [IntroTemplates.md](manual_md/IntroTemplates.md), [DataEngine.md](manual_md/DataEngine.md).

---

## 2. Template engine capabilities (capability matrix)

| Capability | Description | Primary manual topics |
|------------|-------------|------------------------|
| **Declarative layout** | `typedef`, `struct`, primitive arrays, nested structs. | [Structs.md](manual_md/Structs.md), [DataTypes.md](manual_md/DataTypes.md) |
| **Control flow in layout** | Conditional and repeated declarations depend on prior fields. | [ControlStatements.md](manual_md/ControlStatements.md) |
| **Template-only variables** | `local` variables not mapped to the file (optional visibility in Results). | [TemplateVariables.md](manual_md/TemplateVariables.md) |
| **Repositioning** | `FSeek`, `FSkip`, `FTell`; peek with `ReadByte`/`ReadUInt`/… **without** advancing the template cursor. | [FuncIO.md](manual_md/FuncIO.md), [TemplateVariables.md](manual_md/TemplateVariables.md) |
| **Absolute / relative placement** | Attributes `pos`, `localpos` (v16+ for some attribute forms—see HTML). | [TemplateVariables.md](manual_md/TemplateVariables.md) |
| **Endian control** | `BigEndian()`, `LittleEndian()` and per-file endian. | [FuncIO.md](manual_md/FuncIO.md), [ByteOrdering.md](manual_md/ByteOrdering.md) |
| **Display & UX** | `format=`, `fgcolor`, `bgcolor`, `style`, `comment`, `name`, `open`, `hidden`, `edit`, `warn`. | [TemplateVariables.md](manual_md/TemplateVariables.md) |
| **Custom serialization** | `read=` / `write=` on typedefs and structs (custom **string** view in Results). | [CustomVariables.md](manual_md/CustomVariables.md) |
| **Inline attributes (v12+)** | `Str(...)`, expressions, `this`, `value` for write. | [TemplateVariables.md](manual_md/TemplateVariables.md), [CustomVariables.md](manual_md/CustomVariables.md) |
| **On-demand / sized blocks** | `size=` for lazy or fixed-skip structures (large files). | [OnDemand.md](manual_md/OnDemand.md) |
| **Optimized arrays** | Duplicates, `optimize=`, memory/performance tradeoffs. | [ArraysDuplicates.md](manual_md/ArraysDuplicates.md) |
| **Bitfields** | Packed bits, optional auto checkboxes, padding modes. | [Bitfields.md](manual_md/Bitfields.md), [FuncIO.md](manual_md/FuncIO.md) |
| **Disassembly columns** | `disasm=` metadata in templates. | [DisassemblerTemplates.md](manual_md/DisassemblerTemplates.md) |
| **Repository & UI** | Installing/running templates from the app. | [MenuTemplates.md](manual_md/MenuTemplates.md), [OptionsTemplates.md](manual_md/OptionsTemplates.md), [RepositoryDialog.md](manual_md/RepositoryDialog.md), [Running.md](manual_md/Running.md) |
| **Compiler diagnostics** | Warnings, empty structs, etc. | [OptionsCompiling.md](manual_md/OptionsCompiling.md), [TemplateLimitations.md](manual_md/TemplateLimitations.md) |
| **Syntax highlighting for `.bt`** | Writing template syntaxes (advanced). | [WritingSyntaxes.md](manual_md/WritingSyntaxes.md), [WritingTreesitter.md](manual_md/WritingTreesitter.md), [Syntax.md](manual_md/Syntax.md), [Treesitter.md](manual_md/Treesitter.md) |

---

## 3. Language surface (shared with scripts)

Templates and scripts share a **C-like** expression and control-flow language. The manual splits **variable declaration rules** (template vs script) but shares:

| Topic | Purpose |
|-------|---------|
| [Expressions.md](manual_md/Expressions.md) | Operators, literals, casts, `this`, scoping in attributes. |
| [DataTypes.md](manual_md/DataTypes.md) | Primitive types, typedefs, enums. |
| [Structs.md](manual_md/Structs.md) | Aggregates; template structs may contain control flow. |
| [ArraysStrings.md](manual_md/ArraysStrings.md) | Strings and character arrays. |
| [ArraysDuplicates.md](manual_md/ArraysDuplicates.md) | Arrays, duplicate runs, optimization. |
| [ControlStatements.md](manual_md/ControlStatements.md) | `if`/`else`, `for`, `while`, `switch`, `break`, `continue` — note **`goto` unsupported**. |
| [Functions.md](manual_md/Functions.md) | Declaring and calling functions; `&` reference parameters for custom attribute functions. |
| [Sizeof.md](manual_md/Sizeof.md) | `sizeof` (limited for non-simple structs); **`startof(var)`** file address in **local coordinates**. |
| [Preprocessor.md](manual_md/Preprocessor.md) | `#define`, `#ifdef`, … — **`#if` unsupported**; macro limitations per manual. |
| [Includes.md](manual_md/Includes.md) | Including shared headers. |
| [TemplateLimitations.md](manual_md/TemplateLimitations.md) | **No `*` pointers**, no multi-dimensional arrays, etc. |

---

## 4. Template variable declaration (deep link)

The authoritative reference for **what can appear after a variable** in angle brackets is:

**[TemplateVariables.md](manual_md/TemplateVariables.md)** — sections include:

- **Special attributes** — `format`, colors, `style`, `comment`, `name`, `open`, `hidden`, `read`, `write`, `size`, `edit`, `pos`, `localpos`, `optimize`, `disasm`, `warn`, endian, etc. (exact availability by version is versioned in the HTML).
- **Attribute functions and inline expressions** — function vs `(expression)` forms.
- **Positioning** — `FTell`/`FSeek` equivalence vs `pos` / `localpos`.
- **Local vs file-backed** — `local` keyword.
- **Variable editors** — `edit=check|color|flags|none`.
- **Local vs file coordinates** — processes / custom start addresses; `AddressFileToLocal` / `AddressLocalToFile` in [FuncInterface.md](manual_md/FuncInterface.md).

---

## 5. Custom variables (`read=` / `write=`)

**[CustomVariables.md](manual_md/CustomVariables.md)** covers:

- typedef-level **`read=`** and optional **`write=`** turning any type into a **string display** (and optional round-trip edit).
- **Struct read** functions `string Fn(MYSTRUCT &s)` for one-line summaries.
- **Array read/write** patterns; inline `this[0]`… in v12+.
- **Error behavior** — runtime errors show `(error)` until the template is fixed.

---

## 6. Runtime library (templates + scripts)

All of these function catalogs apply **both** to templates and scripts:

| Manual | Typical use in templates |
|--------|---------------------------|
| [FuncIO.md](manual_md/FuncIO.md) | `FileSize`, `FTell`, `FSeek`, `ReadUByte`, `ReadUInt`, `BigEndian`, bitfield helpers, binary conversion. |
| [FuncString.md](manual_md/FuncString.md) | `SPrintf`, `Str`, parsing, `SScanf`. |
| [FuncMath.md](manual_md/FuncMath.md) | Math helpers. |
| [FuncInterface.md](manual_md/FuncInterface.md) | Editor/UI: carets, selections, dialogs, address mapping, file tabs. |
| [FuncTools.md](manual_md/FuncTools.md) | Higher-level tools (checksums, etc.—see HTML index). |

---

## 7. Template-specific manual pages (curated list)

These pages are **most directly** about templates, template UI, or template syntax infrastructure:

| Markdown | Topic |
|----------|--------|
| [IntroTemplates.md](manual_md/IntroTemplates.md) | Topic list for writing templates. |
| [IntroTempScripts.md](manual_md/IntroTempScripts.md) | Templates vs scripts; first example struct. |
| [TemplateVariables.md](manual_md/TemplateVariables.md) | Declaring template variables and attributes. |
| [TemplateResults.md](manual_md/TemplateResults.md) | Working with the Template Results panel. |
| [TemplateLimitations.md](manual_md/TemplateLimitations.md) | Non-ANSI restrictions. |
| [CustomVariables.md](manual_md/CustomVariables.md) | `read=` / `write=`. |
| [OnDemand.md](manual_md/OnDemand.md) | On-demand / `size=` structures. |
| [DisassemblerTemplates.md](manual_md/DisassemblerTemplates.md) | Disassembly in templates. |
| [MenuTemplates.md](manual_md/MenuTemplates.md) | Templates menu. |
| [OptionsTemplates.md](manual_md/OptionsTemplates.md) | Template options (auto-run, etc.). |
| [OptionsCompiling.md](manual_md/OptionsCompiling.md) | Compiler / warning options. |
| [WritingSyntaxes.md](manual_md/WritingSyntaxes.md) | Writing template syntax highlighters. |
| [WritingTreesitter.md](manual_md/WritingTreesitter.md) | Tree-sitter syntax definitions. |
| [EditingWithScripts.md](manual_md/EditingWithScripts.md) | Scripts modifying template variables. |

---

## 8. Scripts touch-points (templates only as consumer)

| Markdown | Why templates care |
|----------|-------------------|
| [Running.md](manual_md/Running.md) | How templates and scripts are executed from the UI. |
| [Debug.md](manual_md/Debug.md) | Debugger for template/script development. |
| [ScriptDLL.md](manual_md/ScriptDLL.md) | External DLL functions (available to **both**). |

For **script-first** topics, see **[scripts.md](scripts.md)**.

---

## 9. Full manual mirror index

Every mirrored `.htm` page has a sibling **`manual_md/[Stem].md`** file. The complete list (141 topics) is:

**[manual_md/README.md](manual_md/README.md)**

That list includes **hex editor**, **find/replace**, **printing**, **options**, **menus**, etc. Those pages are not template-language core, but they document the **environment** in which templates run.

---

## 10. Examples in this repository

| Template | Demonstrates |
|----------|----------------|
| [Pkgstream_2WIRE_SP.bt](Pkgstream_2WIRE_SP.bt) | `BigEndian`, `while` + peek loop, conditional `if (length)`, `local string` + `read=`, zero-byte postfix struct. |
| [OpenTL_NAND_inline_2112.bt](OpenTL_NAND_inline_2112.bt), [S34ML_NAND_inline_2112.bt](S34ML_NAND_inline_2112.bt) | `<size=2112>` on-demand pages, bitfield checkboxes, struct `read=` summaries, `ReadUByte(startof(...)+offset)` spare hints. |

---

## 11. Regenerating `manual_md/*.md`

```powershell
Set-Location D:\electronics\5268ac
python reference\010editor\tools\gen_manual_md.py
```

---

## 12. Copyright

010 Editor and the manual text are **Copyright SweetScape Software**. The HTML mirror and derived Markdown summaries exist in this repo for **offline engineering reference** only.
