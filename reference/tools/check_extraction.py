#!/usr/bin/env python3
"""Check an extracted Sanskrit/Vedic book folder (see FORMAT.md).

Usage:  python3 check_extraction.py reference/<book-id> [--max-lines 1000]

Checks
  files      names look like chNN.CC[-lang].md or pNN[-lang].md, in text/
  lines      every line is "ID | text", IDs well formed, unique, file order
  sanskrit   no Latin letters, NFC, no stray characters, no blank text
  languages  each translation file has exactly the Sanskrit file's IDs
  size       under --max-lines (error for part files, warning for a lone
             chapter file, which must not be split)
  toc        every toc.md row has its file, every text file is in toc.md,
             and the verse counts are printed for toc.md

Exit status 1 when there is any error. Warnings do not fail the check.
"""
import argparse
import re
import sys
import unicodedata
from collections import OrderedDict
from pathlib import Path

FILE_RE = re.compile(
    r"^(?:p(?P<p1>\d{2,3})|ch(?P<p2>\d{2,3})\.(?P<c2>\d{2,3}))"
    r"(?:-(?P<lang>[a-z]+))?\.md$")
ID_RE = re.compile(
    r"^(?P<part>\d{2,3})\.(?P<chap>\d{2,3})\."
    r"(?P<verse>P?\d+(?:-\d+)?(?:\.\d+)*)(?P<line>[a-z]?)$")
LATIN = re.compile(r"[A-Za-z]")
ZERO_WIDTH = "​‌‍⁠﻿"
TRANSLATION_MARKS = ("~", "--")

errors, warnings = [], []


def error(where, message):
    errors.append(f"ERROR   {where}: {message}")


def warn(where, message):
    warnings.append(f"warning {where}: {message}")


def read_lines(path):
    raw = path.read_bytes()
    if raw.startswith(b"\xef\xbb\xbf"):
        error(path.name, "has a byte order mark")
    try:
        text = raw.decode("utf-8")
    except UnicodeDecodeError as exc:
        error(path.name, f"not valid UTF-8 ({exc})")
        return []
    if "\r" in text:
        error(path.name, "has CR line ends (use LF)")
    if text and not text.endswith("\n"):
        error(path.name, "does not end with a newline")
    return text.replace("\r", "").split("\n")[:-1] if text else []


def parse_file(path, is_sanskrit):
    """Return a list of (id, text) for the file, reporting problems."""
    rows = []
    seen = set()
    for number, line in enumerate(read_lines(path), start=1):
        where = f"{path.name}:{number}"
        if " | " not in line:
            error(where, "line is not 'ID | text'")
            continue
        line_id, text = line.split(" | ", 1)
        match = ID_RE.match(line_id)
        if not match:
            error(where, f"bad ID '{line_id}' (want PP.CC.V or PP.CC.Vx)")
            continue
        name = FILE_RE.match(path.name)
        part = name.group("p1") or name.group("p2")
        if match.group("part") != part:
            error(where, f"ID part {match.group('part')} not in file name")
        if name.group("c2") and match.group("chap") != name.group("c2"):
            error(where, f"ID chapter {match.group('chap')} not in file name")
        if line_id in seen:
            error(where, f"duplicate ID {line_id}")
        seen.add(line_id)
        if text != text.strip() or "  " in text:
            warn(where, "leading, trailing or double spaces")
        if not text.strip():
            error(where, "empty text")
        if is_sanskrit:
            check_sanskrit_text(where, text)
        rows.append((line_id, text))
    return rows


def check_sanskrit_text(where, text):
    if unicodedata.normalize("NFC", text) != text:
        error(where, "text is not NFC-normalised")
    if LATIN.search(text):
        error(where, "Latin letters in Sanskrit text (IAST or typo?)")
    if "�" in text:
        error(where, "replacement character (broken encoding)")
    if any(c in text for c in ZERO_WIDTH):
        warn(where, "contains zero-width character(s); confirm they are "
                    "in the source")
    if re.search(r"[0-9]", text):
        warn(where, "contains Latin digits (verse numbers belong in the ID)")
    for char in text:
        if unicodedata.category(char) == "Cc":
            error(where, "control character in text")
            break


def verse_key(line_id):
    match = ID_RE.match(line_id)
    return match.group("part"), match.group("chap"), match.group("verse")


def chapter_counts(rows):
    """Distinct verses and lines per (part, chapter)."""
    counts = OrderedDict()
    for line_id, _ in rows:
        part, chap, verse = verse_key(line_id)
        entry = counts.setdefault((part, chap), {"verses": set(), "lines": 0})
        entry["verses"].add(verse)
        entry["lines"] += 1
    return counts


def parse_toc(toc_path):
    """Rows of the chapter tables in toc.md as dicts keyed by column."""
    rows, header = [], None
    for line in toc_path.read_text(encoding="utf-8").splitlines():
        if not line.startswith("|"):
            header = None if not line.strip() else header
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        lowered = [c.lower() for c in cells]
        if "part" in lowered and "chapter" in lowered and "file" in lowered:
            header = lowered
            continue
        if header is None or set("".join(cells)) <= set("-: "):
            continue
        if len(cells) == len(header):
            rows.append(dict(zip(header, cells)))
    return rows


def main():
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    parser.add_argument("book_dir", type=Path)
    parser.add_argument("--max-lines", type=int, default=1000)
    args = parser.parse_args()

    book = args.book_dir
    text_dir = book / "text"
    if not text_dir.is_dir():
        error(str(book), "no text/ folder")
    toc_path = book / "toc.md"
    if not toc_path.is_file():
        error(str(book), "no toc.md")
    for name in ("README.md", "FORMAT.md", "STATUS.md", "sources.md",
                 "ISSUES.md"):
        if not (book / name).is_file():
            warn(str(book), f"missing {name}")

    sanskrit, translations = {}, {}
    files = sorted(text_dir.glob("*")) if text_dir.is_dir() else []
    for path in files:
        if path.is_dir():
            continue
        match = FILE_RE.match(path.name)
        if not match:
            error(path.name, "file name does not match chNN.CC[-lang].md "
                             "or pNN[-lang].md")
            continue
        lang = match.group("lang")
        is_sanskrit = lang is None
        rows = parse_file(path, is_sanskrit)
        base = path.name.replace(f"-{lang}", "") if lang else path.name
        if is_sanskrit:
            sanskrit[path.name] = rows
            limit = args.max_lines
            if len(rows) > limit:
                lone = match.group("c2") is not None
                (warn if lone else error)(
                    path.name,
                    f"{len(rows)} lines, over {limit}"
                    + (" (single chapter: keep whole, flag in STATUS.md)"
                       if lone else " (split the part into chapter files)"))
        else:
            translations.setdefault(base, {})[lang] = (path.name, rows)
            if len(rows) > args.max_lines:
                warn(path.name, f"{len(rows)} lines, over {args.max_lines}")

    for base, by_lang in translations.items():
        if base not in sanskrit:
            error(base, "translation file(s) without a Sanskrit file")
            continue
        sa_ids = [i for i, _ in sanskrit[base]]
        for lang, (name, rows) in by_lang.items():
            ids = [i for i, _ in rows]
            if ids != sa_ids:
                extra = [i for i in ids if i not in set(sa_ids)][:3]
                missing = [i for i in sa_ids if i not in set(ids)][:3]
                error(name, f"IDs differ from {base}: {len(rows)} lines vs "
                            f"{len(sa_ids)}; extra {extra}, missing {missing}")
            for line_id, text in rows:
                if text in TRANSLATION_MARKS:
                    continue
                if LATIN.search(text) and lang == "hindi":
                    warn(name, f"{line_id}: Latin letters in Hindi text")

    all_rows = [row for rows in sanskrit.values() for row in rows]
    counts = chapter_counts(all_rows)

    if toc_path.is_file():
        toc_rows = parse_toc(toc_path)
        if not toc_rows:
            error("toc.md", "no chapter table found (columns Part, Chapter, "
                            "File ...)")
        listed = set()
        for row in toc_rows:
            part, chap = row.get("part", ""), row.get("chapter", "")
            file_cell = row.get("file", "")
            listed.add(Path(file_cell).name)
            status = row.get("status", "")
            target = book / file_cell
            if status in ("pending", "blocked"):
                continue
            if not target.is_file():
                error("toc.md", f"{part}.{chap}: file {file_cell} not found")
                continue
            entry = counts.get((part, chap))
            if not entry:
                error("toc.md", f"{part}.{chap}: no lines for this chapter "
                                f"in {file_cell}")
                continue
            extracted = row.get("verses (extracted)", "")
            if extracted.isdigit() and int(extracted) != len(entry["verses"]):
                warn("toc.md", f"{part}.{chap}: toc says {extracted} verses "
                               f"extracted, files have {len(entry['verses'])}")
            trad = row.get("verses (traditional)", "")
            if trad.isdigit() and int(trad) != len(entry["verses"]):
                warn("toc.md", f"{part}.{chap}: {len(entry['verses'])} "
                               f"verses extracted, tradition says {trad} "
                               "(log in ISSUES.md)")
        for name in sanskrit:
            if name not in listed:
                error(name, "Sanskrit file is not listed in toc.md")

    print("Verse counts (paste into toc.md 'Verses (extracted)'):")
    for (part, chap), entry in counts.items():
        print(f"  {part}.{chap}: {len(entry['verses'])} verses, "
              f"{entry['lines']} lines")
    print(f"\n{len(sanskrit)} Sanskrit files, "
          f"{sum(len(v) for v in translations.values())} base files with "
          f"translations, {len(all_rows)} Sanskrit lines")
    for message in warnings:
        print(message)
    for message in errors:
        print(message)
    print(f"\n{len(errors)} errors, {len(warnings)} warnings")
    sys.exit(1 if errors else 0)


if __name__ == "__main__":
    main()
