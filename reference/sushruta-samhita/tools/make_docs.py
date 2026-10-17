#!/usr/bin/env python3
"""Write STATUS.md and ISSUES.md for the book folder from the extracted files.

Usage:  python3 -I make_docs.py BOOK_DIR PARSE_JSON APPARATUS_TSV NUMBERING_TSV BRANCH DATE

Everything in ISSUES.md is found by script from the text files, the parse
output and the apparatus log; nothing in the Sanskrit files is changed here.
"""
import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

book = Path(sys.argv[1])
parse = json.loads(Path(sys.argv[2]).read_text(encoding="utf-8"))
apparatus = [l.rstrip("\n").split("\t") for l in
             Path(sys.argv[3]).read_text(encoding="utf-8").splitlines()]
numbering = [l.rstrip("\n").split("\t") for l in
             Path(sys.argv[4]).read_text(encoding="utf-8").splitlines()]
branch, date = sys.argv[5], sys.argv[6]


def short(text, size=150):
    text = text.replace("|", "/")
    return text if len(text) <= size else text[:size] + "..."


def chapter_key(line_id):
    part, chap, _ = line_id.split(".", 2)
    return part, chap


# ------------------------------------------------------------ read files
lines = defaultdict(list)           # (part, chap) -> [(id, text)]
for path in sorted((book / "text").glob("*.md")):
    for row in path.read_text(encoding="utf-8").splitlines():
        line_id, text = row.split(" | ", 1)
        lines[chapter_key(line_id)].append((line_id, text))

# ------------------------------------------------------------- ISSUES.md
issues = []
for part in parse["structure"]:
    if part["part"] == "03":
        issues.append(("03", "count",
                       f"This e-text has {len(part['chapters'])} chapters in "
                       "the Sarirasthana; tradition counts 10. The text ends "
                       "at chapter 9 (colophon: dhamaniivyakarana)", "S1",
                       "check the 1938 Bombay edition for a tenth chapter"))
issues.append(("--", "count",
               "185 chapters extracted (46+16+9+40+8+66); tradition counts "
               "186", "S1", "see the Sarirasthana row above"))
for line_id, kind, what in numbering:
    if kind == "missing":
        issues.append((line_id, "missing",
                       "the source has an empty element here (a half-verse "
                       "or whole verse with no text); no line written, the "
                       "letters of the other lines are kept", "S1",
                       "check against the print edition"))
        continue
    issues.append((line_id, "numbering",
                   f"element has no verse number in the source; joined to "
                   f"verse as extra line(s): {short(what, 60)}", "S1",
                   "check against the print edition"))
sub_numbered = [i for rows in lines.values() for i, _ in rows
                if re.search(r"^\d\d\.\d\d\.\d+(-\d+)?\.\d+", i)]
for line_id in sub_numbered:
    issues.append((line_id, "numbering",
                   "source id has a sub-number (verse.N); kept as written "
                   "(FORMAT.md allows .N in the verse part)", "S1",
                   "none unless a later stage wants a flat number"))
raw_text = (book / "raw" / "susrutasamhita.xml").read_text(encoding="utf-8")
letter_ids = []
for match in re.finditer(r'xml:id="Su\.(\d+)\.(\d+)\.(\d+)([a-z])"',
                         raw_text):
    part, chap, verse, letter = match.groups()
    letter_ids.append(f"{int(part):02d}.{int(chap):02d}.{verse}{letter}")
for line_id in letter_ids:
    issues.append((line_id, "numbering",
                   "source id ends in a letter that is not a half-verse "
                   "(ab/cd); kept as the line letter", "S1", "none"))
for line_id, kind, what in apparatus:
    label = {"footnote": ("variant", "footnote of the print edition"),
             "variant {..}": ("variant", "variant reading {..} removed from "
                              "the line"),
             "editor remark [..]": ("variant", "editor remark [..] removed "
                                    "from the line"),
             "reference (siglum.xx)": ("other", "reference (..) removed "
                                       "from the line"),
             "mark ^": ("other", "mark ^ removed from the line")}[kind]
    issues.append((line_id, label[0], f"{label[1]}: {short(what)}",
                   "S1 (apparatus.tsv has the full text)",
                   "decide in review whether the readings matter"))
# possible typos by script
patterns = [
    (r"[ःं][अ-औ]", "visarga/anusvara followed by an independent vowel "
                    "(likely a typing slip in the e-text)"),
    (r"[क-ह];[क-ह]", "semicolon inside a word"),
    (r"\[|\]", "square bracket kept in the text (source brackets one "
               "interpolated verse across two lines)"),
]
for rows in lines.values():
    for line_id, text in rows:
        for pattern, why in patterns:
            if re.search(pattern, text):
                issues.append((line_id, "possible-typo", why, "S1",
                               "check against the print edition"))
long_chapters = []
for part in parse["structure"]:
    if parse["layout"][part["part"]]["file"] == "chapter":
        for chapter in part["chapters"]:
            if chapter["lines"] > 1000:
                long_chapters.append((part["part"], chapter["chapter"],
                                      chapter["lines"]))
for part, chap, count in long_chapters:
    issues.append((f"{part}.{chap}", "other",
                   f"chapter has {count} lines, over 1000; kept whole in "
                   f"ch{part}.{chap}.md", "S1", "owner decides"))
order = {"count": 0, "order": 1, "missing": 2, "numbering": 3,
         "possible-typo": 4, "variant": 5, "other": 6}
issues.sort(key=lambda r: (order[r[1]], r[0]))
out = ["# Issues: sushruta-samhita", "",
       "Nothing in the Sanskrit files was changed because of an issue. "
       "Row kinds follow templates in the skill. `variant` and `other` rows "
       "for removed apparatus carry the removed text (cut at 150 "
       "characters); the whole text is in `apparatus.tsv`.", "",
       "Conventions that apply to every line (not repeated as rows):", "",
       "- `+` in a line is the e-text's own sandhi-boundary sign. `o+a` and "
       "`e+a` are written with an avagraha; every other `+` is kept as `+` "
       "(about 900 places, mostly a+a, a+aa).",
       "- The e-text writes the daṇḍa as `/` and the double daṇḍa as `//`; "
       "they are written as । and ॥. Where the source has no space before "
       "it, there is none.",
       "- Lead-in lines such as `bhavati cātra` (\"on this ...\") are kept "
       "as their own lines.",
       "- Chapter colophons (`iti suśrutasaṃhitāyāṃ ...`) and chapter "
       "heads are not in the text files; the colophon wording is in "
       "`parse.json`-derived chapter names in `toc.md`.",
       "- Source typos such as `indrādaḥaṃ` (01.01.20) are kept; the "
       "pattern scan below lists the ones a script can see.", "",
       "| Line ID | Kind | What | Source(s) | Suggested check |",
       "|---|---|---|---|---|"]
for line_id, kind, what, source, check in issues:
    out.append(f"| {line_id} | {kind} | {what} | {source} | {check} |")
(book / "ISSUES.md").write_text("\n".join(out) + "\n", encoding="utf-8")

# ------------------------------------------------------------- STATUS.md
app_count = Counter()
for line_id, _, _ in apparatus:
    app_count[chapter_key(line_id)] += 1
issue_count = Counter(chapter_key(i[0]) for i in issues if "." in i[0]
                      and i[0] != "--" and len(i[0].split(".")) >= 3)
compared = {("01", f"{n:02d}") for n in range(1, 6)}
rows = ["| Part | Chapter | Sanskrit lines | Source | Hindi | English | "
        "Check | Notes |", "|---|---|---|---|---|---|---|---|"]
for part in parse["structure"]:
    for chapter in part["chapters"]:
        key = (part["part"], chapter["chapter"])
        notes = []
        if app_count[key]:
            notes.append(f"{app_count[key]} apparatus piece(s) removed")
        if key in compared:
            notes.append("compared with earlier quiz data: same text")
        if chapter["lines"] > 1000:
            notes.append("over 1000 lines, kept whole")
        rows.append(f"| {key[0]} | {key[1]} | {len(lines[key])} | S1 | -- | "
                    f"-- | CHECK | {'; '.join(notes)} |")
status = [
    "# Status: sushruta-samhita", "",
    f"Updated: {date} on branch {branch}. Base source: S1 (SARIT). All 185 "
    "chapters extracted (Sanskrit only; no Hindi or English source could be "
    "fetched, see sources.md).", ""] + rows + [
    "", "## Next",
    "- Hindi and English: no downloadable translation was reachable. "
    "Candidates are in sources.md; the owner can download one and attach "
    "it.",
    "- Verify against a second edition or scan (commentary-free print), "
    "starting with the lines in ISSUES.md (typos, variants).",
    "- Decide what to do with the removed apparatus in `apparatus.tsv` "
    "(variant readings, editor remarks).",
    "- Quiz stage: the existing quiz covers Sutrasthana 1 to 5 only.", ""]
(book / "STATUS.md").write_text("\n".join(status), encoding="utf-8")
print(len(issues), "issues rows")
