"""
Generate reference/010editor/manual_md/*.md from manual/*.htm (skip ' (1).htm' dupes).
"""
from __future__ import annotations

import html
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MAN = ROOT / "manual"
OUT = ROOT / "manual_md"


def strip_tags(s: str) -> str:
    s = re.sub(r"<script.*?</script>", "", s, flags=re.I | re.S)
    s = re.sub(r"<style.*?</style>", "", s, flags=re.I | re.S)
    s = re.sub(r"<[^>]+>", " ", s)
    s = html.unescape(s)
    s = re.sub(r"\s+", " ", s).strip()
    return s


def extract(path: Path) -> tuple[str, str, list[tuple[str, str]], list[str]]:
    raw = path.read_text(encoding="utf-8", errors="replace")
    title_m = re.search(r"<title>([^<]*)</title>", raw, re.I)
    title = strip_tags(title_m.group(1)) if title_m else path.stem
    ph_m = re.search(
        r'<div[^>]*class="PageHeader"[^>]*>(.*?)</div>', raw, re.I | re.S
    )
    page_header = strip_tags(ph_m.group(1)) if ph_m else ""
    h2s: list[tuple[str, str]] = []
    for m in re.finditer(
        r'<h2[^>]*(?:id="([^"]*)")?[^>]*>(.*?)</h2>', raw, re.I | re.S
    ):
        hid, htxt = m.group(1) or "", strip_tags(m.group(2))
        if htxt:
            h2s.append((hid, htxt))
    paras: list[str] = []
    bc = re.search(
        r'class="bodycell"[^>]*>(.*?)</tr></table>', raw, re.I | re.S
    )
    if bc:
        for pm in re.finditer(r"<p[^>]*>(.*?)</p>", bc.group(1), re.I | re.S):
            t = strip_tags(pm.group(1))
            if len(t) > 40 and not t.startswith("This is the manual"):
                paras.append(t)
            if len(paras) >= 10:
                break
    return title, page_header, h2s, paras


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    files = sorted(p for p in MAN.glob("*.htm") if " (1)" not in p.name)
    rows: list[tuple[str, str]] = []
    for p in files:
        try:
            title, ph, h2s, paras = extract(p)
        except OSError as e:
            title, ph, h2s, paras = p.stem, str(e), [], []
        stem = p.stem
        md_path = OUT / f"{stem}.md"
        lines: list[str] = [
            f"# {title}",
            "",
            f"**Source:** [`manual/{p.name}`](../manual/{p.name}) "
            "(SweetScape 010 Editor manual mirror).",
            "",
            "## Page header",
            ph or "_(none extracted)_",
            "",
        ]
        if h2s:
            lines.append("## Section headings")
            for hid, htxt in h2s[:50]:
                anchor = f" `{hid}`" if hid else ""
                lines.append(f"- **{htxt}**{anchor}")
            if len(h2s) > 50:
                lines.append(f"- _…and {len(h2s) - 50} more sections_")
            lines.append("")
        if paras:
            lines.append("## Summary (lead paragraphs)")
            for t in paras:
                if len(t) > 2000:
                    t = t[:1997] + "..."
                lines.append(t)
                lines.append("")
        lines.extend(
            [
                "## Notes",
                "Machine-generated for navigation; figures, tables, and full "
                "`<pre>` examples remain in the `.htm`.",
            ]
        )
        md_path.write_text("\n".join(lines), encoding="utf-8")
        rows.append((stem, title))

    idx = OUT / "README.md"
    body = [
        "# 010 Editor manual — Markdown mirrors",
        "",
        f"Generated summaries for **{len(rows)}** canonical `.htm` pages "
        "(duplicate ` (1).htm` copies omitted).",
        "",
        "Each file lists **section headings** and **lead paragraphs**; open the "
        "HTML for complete content.",
        "",
        "## Index",
        "",
    ]
    for stem, title in sorted(rows, key=lambda x: x[0].lower()):
        body.append(f"- [{stem}.md]({stem}.md) — {title}")
    idx.write_text("\n".join(body), encoding="utf-8")
    print(f"wrote {len(rows)} files to {OUT}")


if __name__ == "__main__":
    main()
