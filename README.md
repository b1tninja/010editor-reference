# 010editor Reference Material

Standalone repository containing 010editor binary template documentation, user manual, and related tools. Project-agnostic reference material independent of any specific electronics analysis project.

## Structure

```
010editor-reference/
├── 010_TEMPLATE_AND_SCRIPTING.md  # Short cheat sheet (templates + scripts)
├── templates.md                   # Binary Templates (.bt) hub index
├── scripts.md                     # Scripts (.1sc) hub index
├── SKILL.md                       # Agent skill entry point
├── manual/                        # Complete 010editor user manual
│   ├── html/                      # HTML format (original *.htm files)
│   └── markdown/                  # Per-page Markdown summaries
├── tools/                         # Helper scripts
│   └── gen_manual_md.py           # Regenerates manual/markdown from manual/html
└── README.md
```

## Contents

### Hub documentation (repo root)
- `templates.md` — Binary Templates (`.bt`) language and runtime index.
- `scripts.md` — Scripting engine (`.1sc`) index.
- `010_TEMPLATE_AND_SCRIPTING.md` — Short cheat sheet covering both surfaces.
- `SKILL.md` — Entry point for the 010bt agent skill.

### User Manual
- Complete HTML user manual covering all 010editor features
- Markdown versions of all manual pages for easy reading/searching
- ~282 HTML pages and ~143 markdown pages

### Tools
- `gen_manual_md.py` — Regenerates `manual/markdown/*.md` summaries in place from `manual/html/*.htm` (`(1).htm` duplicates are skipped). Re-run after refreshing the HTML mirror; it overwrites existing files rather than creating a parallel directory.

## Source

This material originated from the `reference/010editor/` directory of the [5268ac project](https://github.com/b1tninja/5268ac.git) and has been extracted into this standalone repository for broader applicability.

## Binary Templates

Binary templates (`.bt` files) used with the 010editor are maintained separately in the parent 5268ac project:
- `OpenTL_NAND_inline_2112.bt`
- `Pkgstream_2WIRE_SP.bt`
- `S34ML_NAND_inline_2112.bt`