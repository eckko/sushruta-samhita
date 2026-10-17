# Sources: sushruta-samhita

| ID | Name | URL | Edition / editor / year | Script | Licence | Covers | Fetched how | Quality note | Role |
|---|---|---|---|---|---|---|---|---|---|
| S1 | SARIT Susrutasamhita (Yamashita, Muroya) | https://github.com/sarit/sarit-data (data/susrutasamhita.xml, repo commit 92079353eeec801b7f13758832ae3669ab461ebf) | Yadavasarman Trivikramatmaja Acarya, Bombay: Pandurang Javaji, 1931 (Sutrasthana, revised 2nd ed.) and 1938; commentary omitted | IAST (TEI XML) | CC BY-SA 3.0, credit SARIT | all 6 sthanas, 185 chapters (Sarirasthana has 9) | git treeless clone through the session proxy; sha256 eb6d03c18eab86f8aa9bffe2854012337d839524f34d0dcba7e297e9fe7aa85d; copy in raw/ | typed text with footnote and editor apparatus mixed in (see ISSUES.md); a few typing slips | primary |

Cross-check made: chapters 01.01 to 01.05 compared with the earlier reviewed quiz data of this repo (data/chapterN_verses.json, built from the same S1): same text apart from lead-in lines that the quiz data leaves out.

Not reachable from the shell (403 or blocked): GRETIL, archive.org, sanskritdocuments.org. No second Sanskrit text and no Hindi or English translation could be fetched.

Candidates for the owner to download and attach if wanted: an English translation of the Susruta Samhita (Bhishagratna, 1907 to 1916, public domain in many countries, on archive.org, for example item englishtranslati01susruoft); other Sanskrit editions with Dalhana's commentary are not needed at this stage.

Conversion notes: IAST to Devanagari with indic_transliteration (sanscript IAST to DEVANAGARI) after these rules, all in tools/parse_sarit.py: nasal dot variant to the standard one, `o+a`/`e+a` to avagraha, other `+` kept, `/` and `//` to daṇḍa and double daṇḍa; removed apparatus is logged in apparatus.tsv.
