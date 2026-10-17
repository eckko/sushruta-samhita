# Sushruta Samhita: raw extracted source bank

Stage 1 (extraction) of a pipeline: verify, review, fix, proofread come next. This folder holds the raw text, not a finished edition. Nothing here has been proofread.

Read, in order: FORMAT.md (file and line format), toc.md (structure), STATUS.md (what is done), sources.md (where text came from), ISSUES.md (known doubts).

Contents: all six sthanas (185 chapters) of the SARIT e-text in Devanagari, one line per source line with the source's verse number, no translations yet. `apparatus.tsv` lists footnotes, variants and editor remarks that were taken out of lines. `raw/` has the original XML. `tools/` has the scripts: `parse_sarit.py` (XML to text files), `make_toc.py`, `make_docs.py` (STATUS and ISSUES). Rebuild: `python3 -I tools/parse_sarit.py raw/susrutasamhita.xml OUT`.

Rules for anyone editing here:
- Text lines come only from sources listed in sources.md; never from memory.
- Do not rename files or change line IDs of finished chapters.
- Record every doubt in ISSUES.md; fix text only in a later, explicit proofreading stage.
- Run `python3 reference/tools/check_extraction.py reference/sushruta-samhita` before every commit.
- Branch pattern: `docs/YYYY-MM-DD/version-N`; push new branches only; the owner merges.

How to continue: open STATUS.md, take the first chapter not marked extracted (none now; next is translations or verification), follow the skill `/extract-vedic-book-web` (or the steps in FORMAT.md and sources.md if the skill is not available).
