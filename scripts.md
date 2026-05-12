# 010 Editor — Scripts (engine index)

This document is the **hub for the 010 scripting engine** (`.1sc` files): role vs templates, automation surfaces, declaration rules, shared language, runtime libraries, debugger, and links into **per-page Markdown summaries** of the local manual mirror.

| Resource | Role |
|----------|------|
| **[manual_md/README.md](manual_md/README.md)** | Alphabetical index of **all** mirrored manual topics → `[Topic].md`. |
| **[manual_md/MANUAL_MIRROR.md](manual_md/MANUAL_MIRROR.md)** | How summaries are generated from **`manual/*.htm`**, and how to regenerate them. |
| **[010_TEMPLATE_AND_SCRIPTING.md](010_TEMPLATE_AND_SCRIPTING.md)** | Cross-cutting notes where templates and scripts overlap (`Read*`, `FSeek`, etc.). |
| **Official manual** | [https://www.sweetscape.com/010editor/manual/](https://www.sweetscape.com/010editor/manual/) |

---

## 1. What a script is

010 Editor **scripts** are text files with extension **`.1sc`**. They use a **C-like** syntax very close to Binary Templates, but they are used to:

- **Automate editing** of the current file or other files.
- **Drive the application** (dialogs, windows, batch operations).
- **Modify variables** instantiated by a Binary Template (see [EditingWithScripts.md](manual_md/EditingWithScripts.md)).
- Implement **macros**, **checksums**, **compare**, **find in files**, and other tool-style workflows.

Scripts execute **from the first line downward**; there is **no required `main` function**.

Source: [IntroScripts.md](manual_md/IntroScripts.md), [IntroTempScripts.md](manual_md/IntroTempScripts.md).

---

## 2. Script engine capabilities (capability matrix)

| Capability | Description | Primary manual topics |
|------------|-------------|------------------------|
| **File I/O & cursor** | Read/write bytes, seek, query size, endian control. | [FuncIO.md](manual_md/FuncIO.md) |
| **String & parsing** | `SPrintf`, `Str`, `SScanf`, regex helpers (see HTML). | [FuncString.md](manual_md/FuncString.md) |
| **Math** | Floating-point and integer helpers. | [FuncMath.md](manual_md/FuncMath.md) |
| **UI / editor integration** | Caret, selection, tabs, dialogs, progress, file list. | [FuncInterface.md](manual_md/FuncInterface.md) |
| **Tool-style operations** | Compare, histograms, checksums—see function index in HTML. | [FuncTools.md](manual_md/FuncTools.md) |
| **Template interop** | Assign to template variables after a template run. | [EditingWithScripts.md](manual_md/EditingWithScripts.md) |
| **Automation hooks** | Run on startup, shutdown, file open, or from Scripts menu. | [IntroScripts.md](manual_md/IntroScripts.md), [OptionsScripts.md](manual_md/OptionsScripts.md) |
| **External code** | Load and call functions from DLLs. | [ScriptDLL.md](manual_md/ScriptDLL.md) |
| **Debugger** | Breakpoints, stepping, watches for scripts/templates. | [Debug.md](manual_md/Debug.md), [MenuDebug.md](manual_md/MenuDebug.md) |
| **Repository** | Download community scripts from the repository UI. | [RepositoryIntro.md](manual_md/RepositoryIntro.md), [RepositoryDialog.md](manual_md/RepositoryDialog.md) |
| **Execution UI** | Running and compiling from menus. | [MenuScripts.md](manual_md/MenuScripts.md), [Running.md](manual_md/Running.md) |

---

## 3. Script variable declaration

Scripts use **different declaration rules** than templates (no automatic byte-mapping for ordinary locals/globals in the same way). The dedicated topic is:

**[ScriptVariables.md](manual_md/ScriptVariables.md)**

Templates use **[TemplateVariables.md](manual_md/TemplateVariables.md)** instead—compare the two when porting snippets between `.bt` and `.1sc`.

---

## 4. Shared language (scripts + templates)

Scripts and templates share the same **expression**, **control-flow**, **type**, and **function** substrate:

| Topic | Purpose |
|-------|---------|
| [Expressions.md](manual_md/Expressions.md) | Operators, literals, casts. |
| [DataTypes.md](manual_md/DataTypes.md) | Types, typedefs, enums. |
| [Structs.md](manual_md/Structs.md) | Structs and unions (script structs follow C more closely than template layout structs). |
| [ArraysStrings.md](manual_md/ArraysStrings.md) | Strings and arrays. |
| [ArraysDuplicates.md](manual_md/ArraysDuplicates.md) | Arrays and optimization (more template-centric but referenced from shared docs). |
| [ControlStatements.md](manual_md/ControlStatements.md) | Branching and loops — **`goto` unsupported**. |
| [Functions.md](manual_md/Functions.md) | User-defined functions. |
| [Sizeof.md](manual_md/Sizeof.md) | `sizeof` / `startof` (especially relevant when a script manipulates template-backed variables). |
| [Preprocessor.md](manual_md/Preprocessor.md) | Conditional compilation includes—see limitations. |
| [Includes.md](manual_md/Includes.md) | Shared headers across scripts/templates. |
| [TemplateLimitations.md](manual_md/TemplateLimitations.md) | Listed as **Binary Templates and Scripts** limitations in the manual (non-ANSI deltas). |

---

## 5. Runtime library (shared catalogs)

The five function manuals apply **equally** to scripts and templates:

- **[FuncIO.md](manual_md/FuncIO.md)** — file I/O, `Read*`, `Write*`, endian, bitfield helpers.
- **[FuncString.md](manual_md/FuncString.md)** — string building and parsing.
- **[FuncMath.md](manual_md/FuncMath.md)** — math helpers.
- **[FuncInterface.md](manual_md/FuncInterface.md)** — editor and UI integration.
- **[FuncTools.md](manual_md/FuncTools.md)** — tool-style helpers.

---

## 6. Script-first manual pages (curated list)

| Markdown | Topic |
|----------|--------|
| [IntroScripts.md](manual_md/IntroScripts.md) | Writing scripts — topic list and automation overview. |
| [ScriptVariables.md](manual_md/ScriptVariables.md) | Declaring script variables. |
| [MenuScripts.md](manual_md/MenuScripts.md) | Scripts menu reference. |
| [OptionsScripts.md](manual_md/OptionsScripts.md) | Script options (hooks, menu integration, etc.). |
| [ScriptDLL.md](manual_md/ScriptDLL.md) | External DLL functions. |
| [EditingWithScripts.md](manual_md/EditingWithScripts.md) | Editing template-defined variables from scripts. |

---

## 7. Templates vs scripts (quick comparison)

| Aspect | Binary Template (`.bt`) | Script (`.1sc`) |
|--------|-------------------------|-----------------|
| **Primary goal** | Parse file → **variables** in Template Results | **Automate** edits, tools, UI |
| **Declaration default** | Variables **map to file bytes** at the read cursor | Variables behave more like **normal program state** (see ScriptVariables) |
| **`local` keyword** | Not displayed / not file-backed (unless shown via option) | Script `local` semantics per manual |
| **Custom `read=`/`write=`** | Central to rich Template Results | Same function libraries; different typical use |
| **Running** | Templates menu / auto-run on open | Scripts menu / hooks / batch |

See [IntroTempScripts.md](manual_md/IntroTempScripts.md) for the narrative introduction.

---

## 8. Debugger, menus, and global options (scripts context)

| Markdown | Role |
|----------|------|
| [Debug.md](manual_md/Debug.md) | Debugger features for scripts and templates. |
| [MenuDebug.md](manual_md/MenuDebug.md) | Debug menu entries. |
| [Running.md](manual_md/Running.md) | Running templates **and** scripts. |
| [OptionsScripts.md](manual_md/OptionsScripts.md) | Global script-related preferences. |

Other **Menu\*** and **Options\*** pages document the host application (see full index below).

---

## 9. Full manual mirror index

Every mirrored `.htm` page has a sibling **`manual_md/[Stem].md`** summary:

**[manual_md/README.md](manual_md/README.md)**

Use it when you need **Find**, **Replace**, **Projects**, **Hex editor options**, etc.—those features are often orchestrated **from scripts** via [FuncInterface.md](manual_md/FuncInterface.md) even though they are not “language syntax” topics.

---

## 10. Regenerating `manual_md/*.md`

```powershell
Set-Location D:\electronics\5268ac
python reference\010editor\tools\gen_manual_md.py
```

---

## 11. Copyright

010 Editor and the manual text are **Copyright SweetScape Software**. The HTML mirror and derived Markdown summaries exist in this repo for **offline engineering reference** only.
