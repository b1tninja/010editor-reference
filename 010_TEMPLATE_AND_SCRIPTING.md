# 010 Editor: Binary Templates (`.bt`) and Scripts (`.1sc`)

Agent-oriented summary derived from the **SweetScape 010 Editor** manual pages mirrored under [`manual/`](manual/) (HTML sources are `.htm`; some copies are suffixed ` (1).htm`). Canonical online manual: [https://www.sweetscape.com/010editor/manual/](https://www.sweetscape.com/010editor/manual/). Copyright and trademarks belong to SweetScape Software.

**Broader indexes:** [templates.md](templates.md) (template engine hub), [scripts.md](scripts.md) (script engine hub), and the full per-page mirror **[manual/markdown/README.md](manual/markdown/README.md)**.

Use this document when designing or editing templates such as [`Pkgstream_2WIRE_SP.bt`](Pkgstream_2WIRE_SP.bt), [`S34ML_NAND_inline_2112.bt`](S34ML_NAND_inline_2112.bt), and [`OpenTL_NAND_inline_2112.bt`](OpenTL_NAND_inline_2112.bt).

---

## 1. What templates and scripts are

| Artifact | Extension | Role |
|----------|-----------|------|
| **Binary Template** | `.bt` | Parses the **current file** into a hierarchy of **variables** mapped to byte ranges. Shown in **Template Results**. Executed top-to-bottom like an interpreter (after compile). |
| **Script** | `.1sc` | Same C-like syntax family; used to **edit** files, drive the UI, automate tasks, or **modify variables** produced by a template. No `main` required. |

Templates declare variables in order; each declaration consumes bytes at the **current read position** (see `FTell` / `FSeek`). **Read** functions (`ReadByte`, `ReadUInt`, `ReadUByte`, …) read at an address **without** advancing that position (manual: *I/O Functions*).

Reference pages: [IntroTempScripts.htm](manual/html/IntroTempScripts.htm), [IntroTemplates.htm](manual/html/IntroTemplates.htm), [IntroScripts.htm](manual/html/IntroScripts.htm).

---

## 2. Execution model (templates)

1. Template is **compiled**, then **run** from the first line downward.
2. **Control flow** (`if`, `for`, `while`, etc.) can appear **inside** `struct` / `typedef` bodies (unlike plain C structs).
3. Accessing a variable reads from the file; assigning writes back.
4. **Local coordinates**: addresses for `FTell`, `FSeek`, `Read*`, and `startof()` are normally **0 .. FileSize()-1** (exceptions: processes, custom hex start address). See [TemplateVariables.htm — Local Coordinates](manual/html/TemplateVariables.htm).

---

## 3. Manual map: template syntax topics

From [Writing Templates](manual/html/IntroTemplates.htm):

- [Expressions.htm](manual/html/Expressions.htm)
- [Declaring Template Variables](manual/html/TemplateVariables.htm)
- [Data Types, Typedefs, and Enums](manual/html/DataTypes.htm)
- [Structs and Unions](manual/html/Structs.htm)
- [Arrays, Duplicates, and Optimizing](manual/html/ArraysDuplicates.htm)
- [Strings](manual/html/ArraysStrings.htm)
- [Control Statements](manual/html/ControlStatements.htm)
- [Functions](manual/html/Functions.htm)
- [Special Keywords](manual/html/Sizeof.htm) (`sizeof`, **`startof`**)
- [Preprocessor](manual/html/Preprocessor.htm)
- [Includes](manual/html/Includes.htm)
- [Bitfields](manual/html/Bitfields.htm)
- [Editing Variables with Scripts](manual/html/EditingWithScripts.htm)
- [Custom Variables](manual/html/CustomVariables.htm) (`read=` / `write=`)
- [On-Demand Structures](manual/html/OnDemand.htm)
- [External (DLL) Functions](manual/html/ScriptDLL.htm)
- [Limitations](manual/html/TemplateLimitations.htm)

**Function reference** (templates and scripts): [FuncInterface.htm](manual/html/FuncInterface.htm), [FuncIO.htm](manual/html/FuncIO.htm), [FuncString.htm](manual/html/FuncString.htm), [FuncMath.htm](manual/html/FuncMath.htm), [FuncTools.htm](manual/html/FuncTools.htm).

---

## 4. Template variables: positioning and attributes

### 4.1 Default placement

Each variable is placed at the **current file position**; the position then advances by the variable’s size. Query with **`FTell()`**; move with **`FSeek(int64 pos)`** or **`FSkip`**. To read without declaring a variable, use **`ReadUByte` / `ReadUInt` / …** at an explicit offset (they do **not** move the template read position).

Source: [TemplateVariables.htm — Positioning Variables](manual/html/TemplateVariables.htm).

### 4.2 `pos` / `localpos`

- **`<pos=expr>`** — place the variable at an absolute **local** address; does **not** advance the current position (equivalent to save `FTell`, `FSeek`, declare, restore).
- **`<localpos=expr>`** — offset relative to **`startof`** the current struct/union.

### 4.3 `startof`

**`startof(variable)`** returns the **local** starting byte address of the bytes mapped to that variable. Use for “header begins at …”, “payload starts at `startof(tlv) + 8`”, etc.

Source: [Sizeof.htm — startof](manual/html/Sizeof.htm).

### 4.4 Other common attributes

From [TemplateVariables.htm](manual/html/TemplateVariables.htm):

- **`<comment="...">`**, **`<name=...>`** — Template Results display; name/comment can be functions (v4+), inline expressions (v12+).
- **`<open=true|false|suppress>`** — default expand/collapse in Template Results.
- **`<hidden=true>`** — hide from Template Results (typedefs supported).
- **`<warn=false>`** — suppress specific warnings (e.g. empty struct).
- **`local`** keyword — variable not mapped to file; can show in Template Results if **Show Local Variables** is enabled.

---

## 5. Custom display: `read=` and `write=`

[Custom Variables.htm](manual/html/CustomVariables.htm):

- Attach **`read=FunctionName`** (and optionally **`write=FunctionName`**) to a **`typedef`** or struct via **`&lt;read=...&gt;`**.
- **Read** function signature: **`string Name(Type v)`** or **`string Name(Type &v)`** for structs.
- **Write** function: **`void Name(Type &v, string s)`**; may return **`int`** with 0 / -1 for error handling.
- **`typedef` must appear before** the read/write functions in the source file (manual).
- Runtime errors in read show **`(error)`** and the read is not retried until the template is fixed and re-run.
- **v12+**: **inline** read/write inside attributes using **`Str(...)`** (like `SPrintf` but returns string), **`this`**, and for write **`value`** (the string from the UI).

**Struct read=**: use **`string Fn(MYSTRUCT &s)`** to show a one-line summary in Template Results without expanding the struct (ZIP example in manual).

**`optimize=false`**: use on **`local string`** (or similar) variables whose **`read=`** only **displays** derived text and must **not** be optimized away (common for “hint” rows).

---

## 6. Endianness

- Files have an endian mode (status bar **LIT** / **BIG**). [ByteOrdering.htm](manual/html/ByteOrdering.htm).
- In templates/scripts, **`BigEndian()`** / **`LittleEndian()`** force subsequent reads/writes for variables (see [FuncIO.htm](manual/html/FuncIO.htm)).

---

## 7. Limitations vs ANSI C

From [TemplateLimitations.htm](manual/html/TemplateLimitations.htm):

- No **`*` pointers**; **`&`** only in custom function parameters (per Functions topic).
- **`#if`** not supported; **`#define` macros** (function-like) not supported as in C.
- No **multi-dimensional arrays**; use structs containing arrays.
- **`goto`** not supported.

---

## 8. Scripts (`.1sc`): capabilities

From [IntroScripts.htm](manual/html/IntroScripts.htm):

- Automate editing, disk operations, comparisons, checksums, find-in-files, etc.
- Run from **Scripts** menu or automation hooks (**startup**, **shutdown**, **file open**, menu entries — see **Script Options** in manual).
- Same core syntax topics as templates (expressions, types, control flow, functions) plus **[Declaring Script Variables](manual/html/ScriptVariables.htm)** instead of template variable declaration rules.
- **Debugger** for templates and scripts: [Debug.htm](manual/html/Debug.htm).

---

## 9. Patterns that work well in repo templates

### 9.1 Conditional layout

Use **`if (condition) { ... } else if ... else { ... }`** around declarations. Avoid relying on **file-scope** statements that **assign** to a non-local variable purely to skip bytes; the compiler may reject **“Could not assign to a non-local variable”** — prefer **`FSeek` / `FSkip`** or **`if`-guarded** declarations (see `Pkgstream_2WIRE_SP.bt`).

### 9.2 Peeking ahead in a loop

Typical idiom: save **`tlv_start = FTell()`**, **`ReadUInt(tlv_start)`** for type/length, validate, **`FSeek(tlv_start)`**, then instantiate a **`struct`** so the struct owns the parse.

### 9.3 Zero-length arrays

Declaring **`ubyte payload[0]`** can warn; use **`if (len > 0) ubyte payload[len];`** when length may be zero.

### 9.4 Hint-only struct members

A struct whose only job is **`local string hint <read=HintFn, optimize=false, comment="analysis">`** gives a zero-width **analysis row** in Template Results. If the tool rejects an all-**`local`** struct, add a **`ubyte anchor[0]`** or **`&lt;warn=false&gt;`** empty member per manual/workarounds.

### 9.5 String building

Prefer **`SPrintf`** into **`string`** buffers, or **`string x = x + fragment`**, rather than deeply nested ternaries (older 010 builds). **`Str`** is available v12+ for inline attributes.

---

## 10. Local manual index (this repo)

| Topic | File |
|--------|------|
| Templates vs scripts overview | [IntroTempScripts.htm](manual/html/IntroTempScripts.htm) |
| Writing templates (topic list) | [IntroTemplates.htm](manual/html/IntroTemplates.htm) |
| Writing scripts | [IntroScripts.htm](manual/html/IntroScripts.htm) |
| Template variables / attributes | [TemplateVariables.htm](manual/html/TemplateVariables.htm) |
| Custom read/write | [CustomVariables.htm](manual/html/CustomVariables.htm) |
| `startof` / `sizeof` | [Sizeof.htm](manual/html/Sizeof.htm) |
| I/O (`FTell`, `FSeek`, `Read*`, `BigEndian`, `FileSize`) | [FuncIO.htm](manual/html/FuncIO.htm) |
| Limitations | [TemplateLimitations.htm](manual/html/TemplateLimitations.htm) |
| Template Results UI | [TemplateResults.htm](manual/html/TemplateResults.htm) |

---

## 11. Disclaimer

This markdown is a **condensed guide** for automation authors; it does not replace the full manual. Always verify against the official pages or the `.htm` copies shipped in [`manual/`](manual/).
