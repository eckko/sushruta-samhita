#!/usr/bin/env python3
"""Build toc.md from parse.json and the extracted text files.

Usage:  python3 -I make_toc.py BOOK_DIR PARSE_JSON GLOSSES_JSON

Chapter names come from the text itself: the opening formula
"athato <title> adhyayam vyakhyasyamah" of each chapter (IAST in the raw
file), converted to Devanagari. The English name is the title written in
plain Latin letters (no diacritics). Purpose lines are glosses of the title
and are marked (inferred).
"""
import json
import re
import sys
import unicodedata
from pathlib import Path

from indic_transliteration import sanscript

PART_INFO = {
    "01": ("सूत्रस्थान", "Sutrasthana (Section on Fundamentals)"),
    "02": ("निदानस्थान", "Nidanasthana (Section on Diagnosis)"),
    "03": ("शारीरस्थान", "Sharirasthana (Section on the Body)"),
    "04": ("चिकित्सास्थान", "Chikitsasthana (Section on Treatment)"),
    "05": ("कल्पस्थान", "Kalpasthana (Section on Antidotes and Preparations)"),
    "06": ("उत्तरतन्त्र", "Uttaratantra (Concluding Section)"),
}
FORMULA = re.compile(
    r"^Su\.\S+\s+(?:athā(?:to|taḥ|ta)\+?\s*)(.+?)\s*"
    r"(?:madhyāyaṃ|madhyāyaṁ|madhyāyam|adhyāyaṃ|adhyāyaṁ|dhyāyaṃ)?\s*"
    r"vyākhyā\S*")


def title_of(opening):
    opening = re.sub(r"\{[^}]*\}", "", opening)
    match = FORMULA.match(opening.replace("†", "").replace("+", ""))
    return match.group(1).strip() if match else None


def latin(title):
    plain = "".join(c for c in unicodedata.normalize("NFD", title)
                    if not unicodedata.combining(c))
    plain = plain.replace("ṃ", "m").replace("ṁ", "m")
    return plain[:1].upper() + plain[1:]


def main():
    book, parse_path, gloss_path = map(Path, sys.argv[1:4])
    parse = json.loads(parse_path.read_text(encoding="utf-8"))
    glosses = (json.loads(gloss_path.read_text(encoding="utf-8"))
               if gloss_path.is_file() else {})
    purposes = glosses.get("purposes", {})
    part_purposes = glosses.get("parts", {})
    lines = []
    total_chapters = total_verses = 0
    tables = []
    for part in parse["structure"]:
        pnum = part["part"]
        mode = parse["layout"][pnum]["file"]
        sa, en = PART_INFO[pnum]
        rows = []
        for ch in part["chapters"]:
            chap = ch["chapter"]
            path = (book / "text" / (f"p{pnum}.md" if mode == "part"
                                     else f"ch{pnum}.{chap}.md"))
            verses = set()
            for row in path.read_text(encoding="utf-8").splitlines():
                line_id = row.split(" | ", 1)[0]
                p, c, v = line_id.split(".", 2)
                if p == pnum and c == chap:
                    verses.add(re.sub(r"[a-z]$", "", v))
            total_chapters += 1
            total_verses += len(verses)
            title = title_of(ch["opening"])
            if title:
                iast = title
                deva = sanscript.transliterate(
                    unicodedata.normalize("NFC", title.replace("ṁ", "ṃ")),
                    sanscript.IAST, sanscript.DEVANAGARI)
                english = latin(title)
            else:
                deva = english = "(title not found in opening formula)"
            purpose = purposes.get(f"{pnum}.{chap}", "(inferred) to be added")
            rows.append(
                f"| {pnum} | {chap} | {deva} | {english} | {purpose} | "
                f"{len(verses)} | unknown | "
                f"text/{path.name} | extracted |")
        tables.append((pnum, sa, en, part_purposes.get(pnum, ""), rows,
                       sum(1 for _ in part["chapters"])))
    head = [
        "# Sushruta Samhita (सुश्रुतसंहिता)", "",
        "- Author / compiler: Suśruta (teacher: Dhanvantari, king of Kashi, "
        "named in the opening of the text)",
        "- Subject and purpose of the book: the classical Sanskrit text of "
        "surgery and medicine; chapter 1 opens with the sages asking "
        "Dhanvantari to teach Ayurveda, and he agrees to teach it with "
        "surgery (śalya) as its base (stated in the text, 01.01.3 to "
        "01.01.11)",
        "- Base edition: Yādavaśarman Trivikramātmaja Ācārya, Bombay: "
        "Pāṇḍurang Jāvaji, 1931 (Sūtrasthāna, revised 2nd ed.) and 1938 "
        "(later sthānas); SARIT e-text by Tsutomu Yamashita and Yasutaka "
        "Muroya, commentary omitted (source S1 in sources.md)",
        "- Mapping: part = sthāna (01 Sūtra to 06 Uttara), chapter = "
        "adhyāya, verse = verse or prose sūtra as numbered in the source "
        "(`Su.S.C.V`); see FORMAT.md",
        f"- Totals: 6 parts, {total_chapters} chapters, {total_verses} "
        "verses (distinct verse numbers) extracted (traditional: 186 "
        "chapters; this e-text has 185, Śārīrasthāna ends at chapter 9)",
        "",
        "Layout: Sūtrasthāna, Cikitsāsthāna, Kalpasthāna and Uttaratantra "
        "have one file per chapter; Nidānasthāna and Śārīrasthāna are each "
        "under 1000 lines and are one file per part (`p02.md`, `p03.md`). "
        "Chapter 01.46 has 1032 lines and is kept whole.", "",
        "Chapter names are read from each chapter's opening formula "
        "(\"athāto ... adhyāyaṃ vyākhyāsyāmaḥ\") by script and converted to "
        "Devanagari; they are not checked against another edition. "
        "Purpose lines are glosses of the title and are marked (inferred).",
        ""]
    for pnum, sa, en, purpose, rows, count in tables:
        head += [f"## Part {pnum}: {sa} ({en})", "",
                 f"Purpose: {purpose or '(inferred) to be added'}", "",
                 "| Part | Chapter | Sanskrit name | English name | Purpose | "
                 "Verses (extracted) | Verses (traditional) | File | "
                 "Status |",
                 "|---|---|---|---|---|---|---|---|---|"]
        head += rows
        head.append("")
    (book / "toc.md").write_text("\n".join(head), encoding="utf-8")
    print(total_chapters, total_verses)


if __name__ == "__main__":
    main()
