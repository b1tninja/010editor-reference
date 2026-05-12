# 010editor Reference Material

Standalone repository containing 010editor binary template documentation, user manual, and related tools. Project-agnostic reference material independent of any specific electronics analysis project.

## Structure

```
010editor-reference/
├── documentation/          # Template and scripting documentation
│   ├── 010_TEMPLATE_AND_SCRIPTING.md
│   ├── scripts.md
│   └── templates.md
├── manual/                 # Complete 010editor user manual
│   ├── *.htm               # HTML format (original)
│   └── markdown/           # Markdown equivalents
├── tools/                  # Helper scripts
│   └── gen_manual_md.py    # Script to generate markdown from HTML
└── README.md
```

## Contents

### Documentation
- Template usage guides and scripting references
- API documentation for binary template development

### User Manual
- Complete HTML user manual covering all 010editor features
- Markdown versions of all manual pages for easy reading/searching
- ~282 HTML pages and ~143 markdown pages

### Tools
- `gen_manual_md.py` — Utility for converting HTML manual to markdown format

## Source

This material originated from the `reference/010editor/` directory of the [5268ac project](https://github.com/b1tninja/5268ac.git) and has been extracted into this standalone repository for broader applicability.

## Binary Templates

Binary templates (`.bt` files) used with the 010editor are maintained separately in the parent 5268ac project:
- `OpenTL_NAND_inline_2112.bt`
- `Pkgstream_2WIRE_SP.bt`
- `S34ML_NAND_inline_2112.bt`