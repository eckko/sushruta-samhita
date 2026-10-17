#!/usr/bin/env python3
"""Parse the SARIT TEI file of the Susrutasamhita into line-ID text files.

Usage:  python3 -I parse_sarit.py RAW_XML OUT_DIR

Reads  raw/susrutasamhita.xml  (source S1, IAST, SARIT, CC BY-SA 3.0).
Writes OUT_DIR/text/...      Sanskrit files in Devanagari ("ID | text")
       OUT_DIR/parse.json    structure, line counts, titles (for toc.md)
       OUT_DIR/apparatus.tsv every piece of source apparatus that was taken
                             out of a line, with the line ID (for ISSUES.md)

Nothing is typed from memory: every Sanskrit character comes from the XML.
Edits made to a line (all logged in apparatus.tsv):
  - footnote markers (<ref>), footnote bodies (<note>), <label> removed;
  - ^ marks, {O...} variants, [...] editor remarks and (siglum.xxx)
    references removed;
  - IAST converted to Devanagari; / -> danda, // -> double danda;
  - 'o+a' and 'e+a' written as avagraha; any other '+' (the e-text's
    unresolved sandhi boundary) is kept as '+'.
"""
import copy
import json
import re
import sys
import unicodedata
from collections import OrderedDict, defaultdict
from pathlib import Path

from indic_transliteration import sanscript
from lxml import etree

T = "{http://www.tei-c.org/ns/1.0}"
X = "{http://www.w3.org/XML/1998/namespace}id"
HALF = {"ab": "a", "cd": "b", "ef": "c"}


def squash(text):
    return " ".join(text.split())


def strip_markup(element, notes):
    """Text of an element without label/ref/note; note bodies go to notes."""
    node = copy.deepcopy(element)
    for ref in list(node.iter(T + "ref")):
        # a word broken by a footnote marker: "avata-<ref/>karavira"
        previous = ref.getprevious()
        before = (previous.tail if previous is not None else
                  ref.getparent().text) or ""
        after = ref.tail or ""
        if before.endswith("-") and after[:1].isalpha():
            if previous is not None:
                previous.tail = before[:-1]
            else:
                ref.getparent().text = before[:-1]
    for tag in (T + "label", T + "ref", T + "note"):
        for item in list(node.iter(tag)):
            if tag == T + "note":
                notes.append(squash("".join(item.itertext())))
            tail = item.tail or ""
            previous = item.getprevious()
            if previous is not None:
                previous.tail = (previous.tail or "") + tail
            else:
                item.getparent().text = (item.getparent().text or "") + tail
            item.getparent().remove(item)
    return squash("".join(node.itertext()))


REMOVALS = [
    ("variant {..}", re.compile(r"\{[^}]*\}")),
    ("editor remark [..]", re.compile(r"\[[^\]]*\]")),
    ("reference (siglum.xx)",
     re.compile(r"\((?:ā|a|O|ca|pṛ)\.[^)]*\)|\(pṛ\. ?\d+[^)]*\)")),
    ("mark ^", re.compile(r"\^")),
]


def remove_apparatus(text, line_id, log):
    for kind, pattern in REMOVALS:
        for match in pattern.finditer(text):
            log.append((line_id, kind, match.group()))
        text = pattern.sub("", text)
    return squash(text)


def to_devanagari(text):
    text = unicodedata.normalize("NFC", text)
    text = text.replace("ṁ", "ṃ")
    text = re.sub(r"([oe])\+\+?a", r"\1'", text)    # avagraha
    text = text.replace("+", "⁣")               # keep other '+'
    text = text.replace("//", "||").replace("/", "|")
    out = sanscript.transliterate(text, sanscript.IAST, sanscript.DEVANAGARI)
    out = out.replace("⁣", "+").replace("|", "।").replace("॥", "॥")
    out = out.replace("।।", "॥")
    return squash(unicodedata.normalize("NFC", out))


def split_id(source_id):
    """('45', 'ab') from 'Su.1.45.65ab'-like ids: (part, chap, rest)."""
    match = re.match(r"^Su\.(\d+)\.(\d+)\.(.+)$", source_id)
    return match.group(1), match.group(2), match.group(3)


def verse_and_half(rest):
    """rest like '9ab', '26.1cd', '65a', '132v', '26-27', '8.0'."""
    match = re.match(r"^(\d+(?:-\d+)?(?:\.\d+)*)(ab|cd|ef)?$", rest)
    if match:
        return match.group(1), HALF.get(match.group(2) or "", "")
    match = re.match(r"^(\d+)([a-z])$", rest)          # 65a, 132v
    if match:
        return match.group(1), match.group(2)
    raise ValueError(f"cannot read verse id {rest}")


def chapter_units(chapter, log, issues):
    """List of [verse, letter, text, source_ids] for one chapter."""
    units = []
    previous_verse = None
    for element in chapter:
        if element.tag not in (T + "ab", T + "p", T + "lg"):
            continue
        notes = []
        source_id = element.get(X)
        lines = []          # (text, line_source_id)
        if element.tag == T + "lg":
            for l in element.findall(T + "l"):
                lines.append((strip_markup(l, notes), l.get(X)))
            if not source_id:
                source_id = next((l_id for _, l_id in lines if l_id), None)
            if not source_id:
                label = element.find(".//" + T + "label")
                if label is not None:
                    source_id = squash("".join(label.itertext()))
        else:
            lines.append((strip_markup(element, notes), source_id))
        if not source_id:
            source_id = None
        # decide verse and letters
        entries = []
        if source_id:
            _, _, rest = split_id(source_id)
            verse, half = verse_and_half(rest)
            if element.tag == T + "lg" and all(i for _, i in lines):
                # every half-line carries its own id
                for text, line_id in lines:
                    v, letter = verse_and_half(split_id(line_id)[2])
                    entries.append([v, letter, text, line_id])
            elif element.tag == T + "lg":
                for number, (text, _) in enumerate(lines):
                    letter = (chr(ord("a") + number)
                              if len(lines) > 1 else half)
                    entries.append([verse, letter, text, source_id])
            else:
                entries.append([verse, half, lines[0][0], source_id])
        else:
            # unnumbered: continues the previous verse (logged)
            if previous_verse is None:
                raise ValueError("unnumbered element at chapter start")
            earlier = [u for u in units if u[0] == previous_verse]
            if earlier and earlier[0][1] == "" and len(earlier) == 1:
                earlier[0][1] = "a"
            used = {u[1] for u in earlier}
            letter = "a"
            for number, (text, _) in enumerate(lines):
                while letter in used:
                    letter = chr(ord(letter) + 1)
                entries.append([previous_verse, letter, text, None])
                used.add(letter)
            issues.append((previous_verse, "unnumbered",
                           squash(" ".join(t for t, _ in lines))[:60]))
        for verse, letter, text, line_id in entries:
            units.append([verse, letter, text, line_id])
        previous_verse = entries[0][0]
        for note in notes:
            log.append((entries[0][0], "footnote", note))
    return units


def main():
    raw, out = Path(sys.argv[1]), Path(sys.argv[2])
    root = etree.parse(str(raw)).getroot()
    body = root.find(".//" + T + "body")
    (out / "text").mkdir(parents=True, exist_ok=True)
    structure = []
    apparatus = []
    issues = []
    all_rows = OrderedDict()
    for part_number, sthana in enumerate(body.findall(T + "div"), start=1):
        part = f"{part_number:02d}"
        head = squash("".join(sthana.find(T + "head").itertext()))
        chapters = []
        for chapter in sthana.findall(T + "div"):
            number = int(chapter.get("n"))
            chap = f"{number:02d}"
            apparatus_log, unnumbered = [], []
            units = chapter_units(chapter, apparatus_log, unnumbered)
            rows = []
            for verse, letter, text, source_id in units:
                line_id = f"{part}.{chap}.{verse}{letter}"
                label = f"{part}.{chap}.{verse}{letter}"
                clean = remove_apparatus(text, label, apparatus)
                devanagari = to_devanagari(clean)
                if not devanagari:
                    # empty element in the source: no line is written
                    unnumbered.append((f"{verse}{letter}", "missing",
                                       "source element is empty"))
                    continue
                rows.append((line_id, devanagari, source_id or ""))
            for verse, kind, what in apparatus_log:
                apparatus.append((f"{part}.{chap}.{verse}", kind, what))
            for verse, kind, what in unnumbered:
                issues.append((f"{part}.{chap}.{verse}", kind, what))
            trailer = chapter.find(T + "trailer")
            colophon = (squash("".join(trailer.itertext()))
                        if trailer is not None else "")
            first = next((e for e in chapter if e.tag in
                          (T + "ab", T + "p", T + "lg")), None)
            opening = squash("".join(first.itertext())) if first is not None else ""
            chapters.append({"part": part, "chapter": chap,
                             "head": squash("".join(
                                 chapter.find(T + "head").itertext())),
                             "colophon": colophon, "opening": opening,
                             "lines": len(rows)})
            all_rows[(part, chap)] = rows
        structure.append({"part": part, "head": head, "chapters": chapters})
    # layout: whole-part files when a part is under 1000 lines
    layout = {}
    for part in structure:
        total = sum(c["lines"] for c in part["chapters"])
        layout[part["part"]] = {"lines": total,
                                "file": "part" if total < 1000 else "chapter"}
    for part in structure:
        mode = layout[part["part"]]["file"]
        if mode == "part":
            rows = [r for c in part["chapters"]
                    for r in all_rows[(c["part"], c["chapter"])]]
            write(out / "text" / f"p{part['part']}.md", rows)
        else:
            for c in part["chapters"]:
                write(out / "text" / f"ch{c['part']}.{c['chapter']}.md",
                      all_rows[(c["part"], c["chapter"])])
    (out / "parse.json").write_text(json.dumps(
        {"structure": structure, "layout": layout}, ensure_ascii=False,
        indent=1), encoding="utf-8")
    with open(out / "apparatus.tsv", "w", encoding="utf-8") as handle:
        for line_id, kind, what in apparatus:
            handle.write(f"{line_id}\t{kind}\t{what}\n")
    with open(out / "numbering.tsv", "w", encoding="utf-8") as handle:
        for line_id, kind, what in issues:
            handle.write(f"{line_id}\t{kind}\t{what}\n")
    print(json.dumps(layout))
    print("apparatus pieces", len(apparatus), "numbering notes", len(issues))


def write(path, rows):
    text = "".join(f"{line_id} | {text}\n" for line_id, text, _ in rows)
    path.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
