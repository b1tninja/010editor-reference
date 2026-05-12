# Local 010 Editor manual mirror

This directory contains **Markdown summaries** for each canonical **`../manual/html/*.htm`** page (SweetScape 010 Editor documentation, as captured in the repo).

## What each `.md` contains

- **Title** and link back to the original **`.htm`**.
- **Page header** text when present.
- **Section headings** (`<h2>`) when the HTML layout matches the extractor.
- **Lead paragraphs** from the main body (truncated for very long pages).
- **Figures, tables, and full `<pre>` blocks** are *not* inlined; open the **`.htm`** for those.

## Regeneration

From the repository root:

```powershell
python tools/gen_manual_md.py
```

Duplicate pages named `Something (1).htm` are skipped; the canonical file is `Something.htm`.

## Master file list

See **[README.md](README.md)** for an alphabetical index of all topics.
