# Issues: sushruta-samhita

Nothing in the Sanskrit files was changed because of an issue. Row kinds follow templates in the skill. `variant` and `other` rows for removed apparatus carry the removed text (cut at 150 characters); the whole text is in `apparatus.tsv`.

Conventions that apply to every line (not repeated as rows):

- `+` in a line is the e-text's own sandhi-boundary sign. `o+a` and `e+a` are written with an avagraha; every other `+` is kept as `+` (about 900 places, mostly a+a, a+aa).
- The e-text writes the daṇḍa as `/` and the double daṇḍa as `//`; they are written as । and ॥. Where the source has no space before it, there is none.
- Lead-in lines such as `bhavati cātra` ("on this ...") are kept as their own lines.
- Chapter colophons (`iti suśrutasaṃhitāyāṃ ...`) and chapter heads are not in the text files; the colophon wording is in `parse.json`-derived chapter names in `toc.md`.
- Source typos such as `indrādaḥaṃ` (01.01.20) are kept; the pattern scan below lists the ones a script can see.

| Line ID | Kind | What | Source(s) | Suggested check |
|---|---|---|---|---|
| -- | count | 185 chapters extracted (46+16+9+40+8+66); tradition counts 186 | S1 | see the Sarirasthana row above |
| 03 | count | This e-text has 9 chapters in the Sarirasthana; tradition counts 10. The text ends at chapter 9 (colophon: dhamaniivyakarana) | S1 | check the 1938 Bombay edition for a tenth chapter |
| 01.06.12 | missing | the source has an empty element here (a half-verse or whole verse with no text); no line written, the letters of the other lines are kept | S1 | check against the print edition |
| 05.08.89b | missing | the source has an empty element here (a half-verse or whole verse with no text); no line written, the letters of the other lines are kept | S1 | check against the print edition |
| 06.40.16b | missing | the source has an empty element here (a half-verse or whole verse with no text); no line written, the letters of the other lines are kept | S1 | check against the print edition |
| 06.51.12c | missing | the source has an empty element here (a half-verse or whole verse with no text); no line written, the letters of the other lines are kept | S1 | check against the print edition |
| 06.52.47c | missing | the source has an empty element here (a half-verse or whole verse with no text); no line written, the letters of the other lines are kept | S1 | check against the print edition |
| 06.57.3c | missing | the source has an empty element here (a half-verse or whole verse with no text); no line written, the letters of the other lines are kept | S1 | check against the print edition |
| 06.66.3c | missing | the source has an empty element here (a half-verse or whole verse with no text); no line written, the letters of the other lines are kept | S1 | check against the print edition |
| 01.01.25.1 | numbering | source id has a sub-number (verse.N); kept as written (FORMAT.md allows .N in the verse part) | S1 | none unless a later stage wants a flat number |
| 01.01.25.2 | numbering | source id has a sub-number (verse.N); kept as written (FORMAT.md allows .N in the verse part) | S1 | none unless a later stage wants a flat number |
| 01.01.25.3 | numbering | source id has a sub-number (verse.N); kept as written (FORMAT.md allows .N in the verse part) | S1 | none unless a later stage wants a flat number |
| 01.01.25.4 | numbering | source id has a sub-number (verse.N); kept as written (FORMAT.md allows .N in the verse part) | S1 | none unless a later stage wants a flat number |
| 01.01.8.0 | numbering | source id has a sub-number (verse.N); kept as written (FORMAT.md allows .N in the verse part) | S1 | none unless a later stage wants a flat number |
| 01.01.8.1 | numbering | source id has a sub-number (verse.N); kept as written (FORMAT.md allows .N in the verse part) | S1 | none unless a later stage wants a flat number |
| 01.01.8.2 | numbering | source id has a sub-number (verse.N); kept as written (FORMAT.md allows .N in the verse part) | S1 | none unless a later stage wants a flat number |
| 01.01.8.3 | numbering | source id has a sub-number (verse.N); kept as written (FORMAT.md allows .N in the verse part) | S1 | none unless a later stage wants a flat number |
| 01.01.8.4 | numbering | source id has a sub-number (verse.N); kept as written (FORMAT.md allows .N in the verse part) | S1 | none unless a later stage wants a flat number |
| 01.01.8.5 | numbering | source id has a sub-number (verse.N); kept as written (FORMAT.md allows .N in the verse part) | S1 | none unless a later stage wants a flat number |
| 01.01.8.6 | numbering | source id has a sub-number (verse.N); kept as written (FORMAT.md allows .N in the verse part) | S1 | none unless a later stage wants a flat number |
| 01.01.8.7 | numbering | source id has a sub-number (verse.N); kept as written (FORMAT.md allows .N in the verse part) | S1 | none unless a later stage wants a flat number |
| 01.01.8.8 | numbering | source id has a sub-number (verse.N); kept as written (FORMAT.md allows .N in the verse part) | S1 | none unless a later stage wants a flat number |
| 01.15.4.1 | numbering | source id has a sub-number (verse.N); kept as written (FORMAT.md allows .N in the verse part) | S1 | none unless a later stage wants a flat number |
| 01.15.4.2 | numbering | source id has a sub-number (verse.N); kept as written (FORMAT.md allows .N in the verse part) | S1 | none unless a later stage wants a flat number |
| 01.15.4.3 | numbering | source id has a sub-number (verse.N); kept as written (FORMAT.md allows .N in the verse part) | S1 | none unless a later stage wants a flat number |
| 01.16.16.1a | numbering | source id has a sub-number (verse.N); kept as written (FORMAT.md allows .N in the verse part) | S1 | none unless a later stage wants a flat number |
| 01.16.16.1b | numbering | source id has a sub-number (verse.N); kept as written (FORMAT.md allows .N in the verse part) | S1 | none unless a later stage wants a flat number |
| 01.16.26.10a | numbering | source id has a sub-number (verse.N); kept as written (FORMAT.md allows .N in the verse part) | S1 | none unless a later stage wants a flat number |
| 01.16.26.10b | numbering | source id has a sub-number (verse.N); kept as written (FORMAT.md allows .N in the verse part) | S1 | none unless a later stage wants a flat number |
| 01.16.26.11a | numbering | source id has a sub-number (verse.N); kept as written (FORMAT.md allows .N in the verse part) | S1 | none unless a later stage wants a flat number |
| 01.16.26.11b | numbering | source id has a sub-number (verse.N); kept as written (FORMAT.md allows .N in the verse part) | S1 | none unless a later stage wants a flat number |
| 01.16.26.12a | numbering | source id has a sub-number (verse.N); kept as written (FORMAT.md allows .N in the verse part) | S1 | none unless a later stage wants a flat number |
| 01.16.26.12b | numbering | source id has a sub-number (verse.N); kept as written (FORMAT.md allows .N in the verse part) | S1 | none unless a later stage wants a flat number |
| 01.16.26.13a | numbering | source id has a sub-number (verse.N); kept as written (FORMAT.md allows .N in the verse part) | S1 | none unless a later stage wants a flat number |
| 01.16.26.13b | numbering | source id has a sub-number (verse.N); kept as written (FORMAT.md allows .N in the verse part) | S1 | none unless a later stage wants a flat number |
| 01.16.26.14a | numbering | source id has a sub-number (verse.N); kept as written (FORMAT.md allows .N in the verse part) | S1 | none unless a later stage wants a flat number |
| 01.16.26.14b | numbering | source id has a sub-number (verse.N); kept as written (FORMAT.md allows .N in the verse part) | S1 | none unless a later stage wants a flat number |
| 01.16.26.15a | numbering | source id has a sub-number (verse.N); kept as written (FORMAT.md allows .N in the verse part) | S1 | none unless a later stage wants a flat number |
| 01.16.26.15b | numbering | source id has a sub-number (verse.N); kept as written (FORMAT.md allows .N in the verse part) | S1 | none unless a later stage wants a flat number |
| 01.16.26.15c | numbering | source id has a sub-number (verse.N); kept as written (FORMAT.md allows .N in the verse part) | S1 | none unless a later stage wants a flat number |
| 01.16.26.16a | numbering | source id has a sub-number (verse.N); kept as written (FORMAT.md allows .N in the verse part) | S1 | none unless a later stage wants a flat number |
| 01.16.26.16b | numbering | source id has a sub-number (verse.N); kept as written (FORMAT.md allows .N in the verse part) | S1 | none unless a later stage wants a flat number |
| 01.16.26.17a | numbering | source id has a sub-number (verse.N); kept as written (FORMAT.md allows .N in the verse part) | S1 | none unless a later stage wants a flat number |
| 01.16.26.17b | numbering | source id has a sub-number (verse.N); kept as written (FORMAT.md allows .N in the verse part) | S1 | none unless a later stage wants a flat number |
| 01.16.26.18a | numbering | source id has a sub-number (verse.N); kept as written (FORMAT.md allows .N in the verse part) | S1 | none unless a later stage wants a flat number |
| 01.16.26.18b | numbering | source id has a sub-number (verse.N); kept as written (FORMAT.md allows .N in the verse part) | S1 | none unless a later stage wants a flat number |
| 01.16.26.19a | numbering | source id has a sub-number (verse.N); kept as written (FORMAT.md allows .N in the verse part) | S1 | none unless a later stage wants a flat number |
| 01.16.26.19b | numbering | source id has a sub-number (verse.N); kept as written (FORMAT.md allows .N in the verse part) | S1 | none unless a later stage wants a flat number |
| 01.16.26.1a | numbering | source id has a sub-number (verse.N); kept as written (FORMAT.md allows .N in the verse part) | S1 | none unless a later stage wants a flat number |
| 01.16.26.1b | numbering | source id has a sub-number (verse.N); kept as written (FORMAT.md allows .N in the verse part) | S1 | none unless a later stage wants a flat number |
| 01.16.26.2a | numbering | source id has a sub-number (verse.N); kept as written (FORMAT.md allows .N in the verse part) | S1 | none unless a later stage wants a flat number |
| 01.16.26.2b | numbering | source id has a sub-number (verse.N); kept as written (FORMAT.md allows .N in the verse part) | S1 | none unless a later stage wants a flat number |
| 01.16.26.3a | numbering | source id has a sub-number (verse.N); kept as written (FORMAT.md allows .N in the verse part) | S1 | none unless a later stage wants a flat number |
| 01.16.26.3b | numbering | source id has a sub-number (verse.N); kept as written (FORMAT.md allows .N in the verse part) | S1 | none unless a later stage wants a flat number |
| 01.16.26.4a | numbering | source id has a sub-number (verse.N); kept as written (FORMAT.md allows .N in the verse part) | S1 | none unless a later stage wants a flat number |
| 01.16.26.4b | numbering | source id has a sub-number (verse.N); kept as written (FORMAT.md allows .N in the verse part) | S1 | none unless a later stage wants a flat number |
| 01.16.26.5a | numbering | source id has a sub-number (verse.N); kept as written (FORMAT.md allows .N in the verse part) | S1 | none unless a later stage wants a flat number |
| 01.16.26.5b | numbering | source id has a sub-number (verse.N); kept as written (FORMAT.md allows .N in the verse part) | S1 | none unless a later stage wants a flat number |
| 01.16.26.6a | numbering | source id has a sub-number (verse.N); kept as written (FORMAT.md allows .N in the verse part) | S1 | none unless a later stage wants a flat number |
| 01.16.26.6b | numbering | source id has a sub-number (verse.N); kept as written (FORMAT.md allows .N in the verse part) | S1 | none unless a later stage wants a flat number |
| 01.16.26.7a | numbering | source id has a sub-number (verse.N); kept as written (FORMAT.md allows .N in the verse part) | S1 | none unless a later stage wants a flat number |
| 01.16.26.7b | numbering | source id has a sub-number (verse.N); kept as written (FORMAT.md allows .N in the verse part) | S1 | none unless a later stage wants a flat number |
| 01.16.26.8a | numbering | source id has a sub-number (verse.N); kept as written (FORMAT.md allows .N in the verse part) | S1 | none unless a later stage wants a flat number |
| 01.16.26.8b | numbering | source id has a sub-number (verse.N); kept as written (FORMAT.md allows .N in the verse part) | S1 | none unless a later stage wants a flat number |
| 01.16.26.9a | numbering | source id has a sub-number (verse.N); kept as written (FORMAT.md allows .N in the verse part) | S1 | none unless a later stage wants a flat number |
| 01.16.26.9b | numbering | source id has a sub-number (verse.N); kept as written (FORMAT.md allows .N in the verse part) | S1 | none unless a later stage wants a flat number |
| 01.41.4.1 | numbering | source id has a sub-number (verse.N); kept as written (FORMAT.md allows .N in the verse part) | S1 | none unless a later stage wants a flat number |
| 01.41.4.2 | numbering | source id has a sub-number (verse.N); kept as written (FORMAT.md allows .N in the verse part) | S1 | none unless a later stage wants a flat number |
| 01.41.4.3 | numbering | source id has a sub-number (verse.N); kept as written (FORMAT.md allows .N in the verse part) | S1 | none unless a later stage wants a flat number |
| 01.41.4.4 | numbering | source id has a sub-number (verse.N); kept as written (FORMAT.md allows .N in the verse part) | S1 | none unless a later stage wants a flat number |
| 01.41.4.5 | numbering | source id has a sub-number (verse.N); kept as written (FORMAT.md allows .N in the verse part) | S1 | none unless a later stage wants a flat number |
| 01.42.10.1 | numbering | source id has a sub-number (verse.N); kept as written (FORMAT.md allows .N in the verse part) | S1 | none unless a later stage wants a flat number |
| 01.42.10.2 | numbering | source id has a sub-number (verse.N); kept as written (FORMAT.md allows .N in the verse part) | S1 | none unless a later stage wants a flat number |
| 01.42.10.3 | numbering | source id has a sub-number (verse.N); kept as written (FORMAT.md allows .N in the verse part) | S1 | none unless a later stage wants a flat number |
| 01.42.10.4 | numbering | source id has a sub-number (verse.N); kept as written (FORMAT.md allows .N in the verse part) | S1 | none unless a later stage wants a flat number |
| 01.42.10.5 | numbering | source id has a sub-number (verse.N); kept as written (FORMAT.md allows .N in the verse part) | S1 | none unless a later stage wants a flat number |
| 01.42.10.6 | numbering | source id has a sub-number (verse.N); kept as written (FORMAT.md allows .N in the verse part) | S1 | none unless a later stage wants a flat number |
| 01.42.8.1 | numbering | source id has a sub-number (verse.N); kept as written (FORMAT.md allows .N in the verse part) | S1 | none unless a later stage wants a flat number |
| 01.42.8.2 | numbering | source id has a sub-number (verse.N); kept as written (FORMAT.md allows .N in the verse part) | S1 | none unless a later stage wants a flat number |
| 01.42.8.3 | numbering | source id has a sub-number (verse.N); kept as written (FORMAT.md allows .N in the verse part) | S1 | none unless a later stage wants a flat number |
| 01.43.3.1a | numbering | source id has a sub-number (verse.N); kept as written (FORMAT.md allows .N in the verse part) | S1 | none unless a later stage wants a flat number |
| 01.43.3.1b | numbering | source id has a sub-number (verse.N); kept as written (FORMAT.md allows .N in the verse part) | S1 | none unless a later stage wants a flat number |
| 01.43.3.2a | numbering | source id has a sub-number (verse.N); kept as written (FORMAT.md allows .N in the verse part) | S1 | none unless a later stage wants a flat number |
| 01.43.3.2b | numbering | source id has a sub-number (verse.N); kept as written (FORMAT.md allows .N in the verse part) | S1 | none unless a later stage wants a flat number |
| 01.45.112a | numbering | source id ends in a letter that is not a half-verse (ab/cd); kept as the line letter | S1 | none |
| 01.45.132v | numbering | source id ends in a letter that is not a half-verse (ab/cd); kept as the line letter | S1 | none |
| 01.45.148v | numbering | source id ends in a letter that is not a half-verse (ab/cd); kept as the line letter | S1 | none |
| 01.45.217v | numbering | source id ends in a letter that is not a half-verse (ab/cd); kept as the line letter | S1 | none |
| 01.45.65a | numbering | source id ends in a letter that is not a half-verse (ab/cd); kept as the line letter | S1 | none |
| 01.45.84a | numbering | source id ends in a letter that is not a half-verse (ab/cd); kept as the line letter | S1 | none |
| 01.45.96a | numbering | source id ends in a letter that is not a half-verse (ab/cd); kept as the line letter | S1 | none |
| 01.46.138v | numbering | source id ends in a letter that is not a half-verse (ab/cd); kept as the line letter | S1 | none |
| 01.46.139v | numbering | source id ends in a letter that is not a half-verse (ab/cd); kept as the line letter | S1 | none |
| 01.46.281v | numbering | source id ends in a letter that is not a half-verse (ab/cd); kept as the line letter | S1 | none |
| 03.05.50 | numbering | element has no verse number in the source; joined to verse as extra line(s): na śakyaścakṣuṣā draṣṭuṁ dehe sūkṣmatamo vibhuḥ/ dṛśyate jñā | S1 | check against the print edition |
| 05.02.3 | numbering | element has no verse number in the source; joined to verse as extra line(s): daśādhiṣṭhānamādyaṃ tu dvitīyaṃ ṣoḍaśāśrayam// | S1 | check against the print edition |
| 06.39.50.1a | numbering | source id has a sub-number (verse.N); kept as written (FORMAT.md allows .N in the verse part) | S1 | none unless a later stage wants a flat number |
| 06.39.50.1b | numbering | source id has a sub-number (verse.N); kept as written (FORMAT.md allows .N in the verse part) | S1 | none unless a later stage wants a flat number |
| 06.39.50.1c | numbering | source id has a sub-number (verse.N); kept as written (FORMAT.md allows .N in the verse part) | S1 | none unless a later stage wants a flat number |
| 06.39.50.2a | numbering | source id has a sub-number (verse.N); kept as written (FORMAT.md allows .N in the verse part) | S1 | none unless a later stage wants a flat number |
| 06.39.50.2b | numbering | source id has a sub-number (verse.N); kept as written (FORMAT.md allows .N in the verse part) | S1 | none unless a later stage wants a flat number |
| 06.39.50.3a | numbering | source id has a sub-number (verse.N); kept as written (FORMAT.md allows .N in the verse part) | S1 | none unless a later stage wants a flat number |
| 06.39.50.3b | numbering | source id has a sub-number (verse.N); kept as written (FORMAT.md allows .N in the verse part) | S1 | none unless a later stage wants a flat number |
| 01.01.20 | possible-typo | visarga/anusvara followed by an independent vowel (likely a typing slip in the e-text) | S1 | check against the print edition |
| 01.02.3 | possible-typo | visarga/anusvara followed by an independent vowel (likely a typing slip in the e-text) | S1 | check against the print edition |
| 01.04.4b | possible-typo | visarga/anusvara followed by an independent vowel (likely a typing slip in the e-text) | S1 | check against the print edition |
| 01.05.31a | possible-typo | square bracket kept in the text (source brackets one interpolated verse across two lines) | S1 | check against the print edition |
| 01.05.31b | possible-typo | square bracket kept in the text (source brackets one interpolated verse across two lines) | S1 | check against the print edition |
| 01.23.3 | possible-typo | visarga/anusvara followed by an independent vowel (likely a typing slip in the e-text) | S1 | check against the print edition |
| 01.39.14b | possible-typo | visarga/anusvara followed by an independent vowel (likely a typing slip in the e-text) | S1 | check against the print edition |
| 01.46.134a | possible-typo | visarga/anusvara followed by an independent vowel (likely a typing slip in the e-text) | S1 | check against the print edition |
| 03.06.25 | possible-typo | visarga/anusvara followed by an independent vowel (likely a typing slip in the e-text) | S1 | check against the print edition |
| 04.06.4 | possible-typo | visarga/anusvara followed by an independent vowel (likely a typing slip in the e-text) | S1 | check against the print edition |
| 04.07.33 | possible-typo | visarga/anusvara followed by an independent vowel (likely a typing slip in the e-text) | S1 | check against the print edition |
| 04.31.8 | possible-typo | visarga/anusvara followed by an independent vowel (likely a typing slip in the e-text) | S1 | check against the print edition |
| 04.37.88 | possible-typo | visarga/anusvara followed by an independent vowel (likely a typing slip in the e-text) | S1 | check against the print edition |
| 06.38.22b | possible-typo | visarga/anusvara followed by an independent vowel (likely a typing slip in the e-text) | S1 | check against the print edition |
| 06.39.102a | possible-typo | visarga/anusvara followed by an independent vowel (likely a typing slip in the e-text) | S1 | check against the print edition |
| 06.39.30b | possible-typo | visarga/anusvara followed by an independent vowel (likely a typing slip in the e-text) | S1 | check against the print edition |
| 01.01.3 | variant | footnote of the print edition: karavīra | S1 (apparatus.tsv has the full text) | decide in review whether the readings matter |
| 01.01.8.3 | variant | variant reading {..} removed from the line: {O.atīsāra} | S1 (apparatus.tsv has the full text) | decide in review whether the readings matter |
| 01.06.34a | variant | variant reading {..} removed from the line: {O.-t} | S1 (apparatus.tsv has the full text) | decide in review whether the readings matter |
| 01.25.1 | variant | variant reading {..} removed from the line: {O.?} | S1 (apparatus.tsv has the full text) | decide in review whether the readings matter |
| 01.35.12 | variant | variant reading {..} removed from the line: {O.pañca} | S1 (apparatus.tsv has the full text) | decide in review whether the readings matter |
| 01.38.24 | variant | variant reading {..} removed from the line: {O.?} | S1 (apparatus.tsv has the full text) | decide in review whether the readings matter |
| 01.38.24 | variant | variant reading {..} removed from the line: {O.u} | S1 (apparatus.tsv has the full text) | decide in review whether the readings matter |
| 01.39.10 | variant | variant reading {..} removed from the line: {??} | S1 (apparatus.tsv has the full text) | decide in review whether the readings matter |
| 01.40.10 | variant | variant reading {..} removed from the line: {O.vyāṇy} | S1 (apparatus.tsv has the full text) | decide in review whether the readings matter |
| 01.42.10.6 | variant | variant reading {..} removed from the line: {ṃ.6} | S1 (apparatus.tsv has the full text) | decide in review whether the readings matter |
| 01.42.8 | variant | variant reading {..} removed from the line: {ṃ.4} | S1 (apparatus.tsv has the full text) | decide in review whether the readings matter |
| 01.42.9 | variant | variant reading {..} removed from the line: {O.ā} | S1 (apparatus.tsv has the full text) | decide in review whether the readings matter |
| 01.46.42b | variant | variant reading {..} removed from the line: {ṃ.-} | S1 (apparatus.tsv has the full text) | decide in review whether the readings matter |
| 01.46.452b | variant | variant reading {..} removed from the line: {O.pātreṣu} | S1 (apparatus.tsv has the full text) | decide in review whether the readings matter |
| 03.01.22 | variant | footnote of the print edition: 'svatantraparatantrataḥ'iti pā+ | S1 (apparatus.tsv has the full text) | decide in review whether the readings matter |
| 03.01.3 | variant | footnote of the print edition: 'anekeṣāṁ'iti pā+ | S1 (apparatus.tsv has the full text) | decide in review whether the readings matter |
| 03.01.7 | variant | footnote of the print edition: 'adhidaivatamatha'iti pā+ | S1 (apparatus.tsv has the full text) | decide in review whether the readings matter |
| 03.01.7 | variant | footnote of the print edition: 'vacaso+agniḥ'iti pā+ | S1 (apparatus.tsv has the full text) | decide in review whether the readings matter |
| 03.01.9 | variant | footnote of the print edition: 'ubhāvapyaparau'iti pā+ | S1 (apparatus.tsv has the full text) | decide in review whether the readings matter |
| 03.02.1 | variant | footnote of the print edition: 'śukraśoṇitaśuddhināma'iti pā+ | S1 (apparatus.tsv has the full text) | decide in review whether the readings matter |
| 03.02.10 | variant | editor remark [..] removed from the line: [asyāgre+asnehādiśca kramaḥ kāryaḥ ṣaṭsvetāsu vijānatā' ityadhikaḥ pāṭhaḥ kvacidupalabhyate'] | S1 (apparatus.tsv has the full text) | decide in review whether the readings matter |
| 03.02.14 | variant | editor remark [..] removed from the line: ['durgandhe pūyasaṅkāśe'iti pā+] | S1 (apparatus.tsv has the full text) | decide in review whether the readings matter |
| 03.02.16 | variant | footnote of the print edition: 'doṣāṇāṁ'iti pā+ | S1 (apparatus.tsv has the full text) | decide in review whether the readings matter |
| 03.02.18 | variant | editor remark [..] removed from the line: ['vijānīyāduktaṁ lakṣaṇalakṣitam'iti pā+] | S1 (apparatus.tsv has the full text) | decide in review whether the readings matter |
| 03.02.23 | variant | footnote of the print edition: 'athāpyatra'iti pā+ | S1 (apparatus.tsv has the full text) | decide in review whether the readings matter |
| 03.02.25 | variant | footnote of the print edition: 'ahatavāsasamalaṅkṛtāṁ'iti pā+ | S1 (apparatus.tsv has the full text) | decide in review whether the readings matter |
| 03.02.28 | variant | footnote of the print edition: 'āsvāsya'iti pā+ | S1 (apparatus.tsv has the full text) | decide in review whether the readings matter |
| 03.02.3 | variant | editor remark [..] removed from the line: ['kuṇapagandhi'iti pā+] | S1 (apparatus.tsv has the full text) | decide in review whether the readings matter |
| 03.02.31 | variant | footnote of the print edition: 'vimucyate prāṇaiḥ'iti pā+ | S1 (apparatus.tsv has the full text) | decide in review whether the readings matter |
| 03.02.31 | variant | footnote of the print edition: 'tadvadetat'iti pā+ | S1 (apparatus.tsv has the full text) | decide in review whether the readings matter |
| 03.02.32 | variant | editor remark [..] removed from the line: [asyāgre+avāme duhitṛkāmāyai' ityadhikaṁ pathyate kvacitpustake/] | S1 (apparatus.tsv has the full text) | decide in review whether the readings matter |
| 03.02.34 | variant | footnote of the print edition: 'mahāsattvā+'iti pā+ | S1 (apparatus.tsv has the full text) | decide in review whether the readings matter |
| 03.02.4 | variant | editor remark [..] removed from the line: [ayaṁ pāṭho hastalikhitapustake nopalabhayate] | S1 (apparatus.tsv has the full text) | decide in review whether the readings matter |
| 03.02.8 | variant | footnote of the print edition: '+aśmabhitsiddhaṁ'iti pā+ | S1 (apparatus.tsv has the full text) | decide in review whether the readings matter |
| 03.03.16 | variant | footnote of the print edition: 'prabhṛtyeva'iti pā+ | S1 (apparatus.tsv has the full text) | decide in review whether the readings matter |
| 03.03.16 | variant | footnote of the print edition: 'yānāvarohaṇaṁ'iti pā+ | S1 (apparatus.tsv has the full text) | decide in review whether the readings matter |
| 03.03.25 | variant | footnote of the print edition: 'dhāvanātmakam'iti pā+ | S1 (apparatus.tsv has the full text) | decide in review whether the readings matter |
| 03.03.26 | variant | footnote of the print edition: 'nirvikāratvātprakṛtibhāvānupapatteḥ'iti pā+ | S1 (apparatus.tsv has the full text) | decide in review whether the readings matter |
| 03.03.30 | variant | editor remark [..] removed from the line: ['nairṛtabhāgadheyatvāt'iti pā+] | S1 (apparatus.tsv has the full text) | decide in review whether the readings matter |
| 03.03.30 | variant | footnote of the print edition: 'asthiraṁ bhavati'iti pā+ | S1 (apparatus.tsv has the full text) | decide in review whether the readings matter |
| 03.03.31 | variant | editor remark [..] removed from the line: ['asañjātāṅgapratyaṅgavibhāgaṁ tu garbhe niṣekāt prabhṛti'iti pā+] | S1 (apparatus.tsv has the full text) | decide in review whether the readings matter |
| 03.03.32 | variant | footnote of the print edition: 'dehendriyāṇām'iti pā+ | S1 (apparatus.tsv has the full text) | decide in review whether the readings matter |
| 03.03.34 | variant | footnote of the print edition: 'vidy?āt'iti pā+ | S1 (apparatus.tsv has the full text) | decide in review whether the readings matter |
| 03.04.10 | variant | footnote of the print edition: 'sravati'iti pā+ | S1 (apparatus.tsv has the full text) | decide in review whether the readings matter |
| 03.04.11 | variant | footnote of the print edition: 'kṣīramāsravet'iti pā+ | S1 (apparatus.tsv has the full text) | decide in review whether the readings matter |
| 03.04.11 | variant | footnote of the print edition: 'pratiricyate'iti pā+ | S1 (apparatus.tsv has the full text) | decide in review whether the readings matter |
| 03.04.12 | variant | editor remark [..] removed from the line: ['tadeva ca śirasi kapālapraticchannaṁ mastiṣkākhyaṁ mastuluṅgākhyaṁ ca' ityaṣṭāṅgasaṁgrahe+adhikaḥ pāṭhaḥ/ 'medo nāma---sāndrasarpistulyaḥ snehadhātu... | S1 (apparatus.tsv has the full text) | decide in review whether the readings matter |
| 03.04.18 | variant | editor remark [..] removed from the line: ['ṣaṣṭhī pittadharā nāma pakvāmāśayamadhyasthā/ sā hyantaragneradhiṣṭhānatayā++āmāśayāt pakvāśayonmukhamannaṁ balena vidhārya pittatejasā śoṣayati pac... | S1 (apparatus.tsv has the full text) | decide in review whether the readings matter |
| 03.04.21 | variant | footnote of the print edition: 'guḍaścekṣarase'iti pā+ | S1 (apparatus.tsv has the full text) | decide in review whether the readings matter |
| 03.04.22 | variant | editor remark [..] removed from the line: ['dvyaṅgule dakṣiṇe pārśve bastidvārasya cāpyadhaḥ/ mūtrasrotaḥpathācchukraṁ puruṣasya pravartata' ityatra+advyaṅgule dakṣiṇe vāma' ityeva sādhīyān pā... | S1 (apparatus.tsv has the full text) | decide in review whether the readings matter |
| 03.04.25 | variant | footnote of the print edition: 'udānavāyorādhāraḥ phupphusaḥ procyate budhauḥ'iti śārṅgadharaḥ | S1 (apparatus.tsv has the full text) | decide in review whether the readings matter |
| 03.04.28 | variant | editor remark [..] removed from the line: ['tatrāsya mathyamānasya dhmāyamānasya rukmavat/ jihvā saṁjāyate saumī yayā vedayate rasān' iti pā+] | S1 (apparatus.tsv has the full text) | decide in review whether the readings matter |
| 03.04.29 | variant | editor remark [..] removed from the line: [vai+ paṁ+ hariprapannaśarmaṇā tu ayaṁ pāṭho+anyathā paṭhito vyākhyātaśca,+amedaḥ sa snehamādāya sirāsnāyutvamapyatha/ sirāṇāṁ tu mṛduḥ pākaḥ snāyūnāṁ... | S1 (apparatus.tsv has the full text) | decide in review whether the readings matter |
| 03.04.31 | variant | editor remark [..] removed from the line: [yattu+ahṛdayasyādho vāmataḥ plīhā phusphusaśca, dakṣiṇato yakṛt kloma ca' iti sauśrutaḥ pāṭhaḥ tatra pramāda eva darīdṛśyate,+ahṛdayasyādho vāmataḥ p... | S1 (apparatus.tsv has the full text) | decide in review whether the readings matter |
| 03.04.31 | variant | footnote of the print edition: 'tasya vāmataḥ'iti pā+ | S1 (apparatus.tsv has the full text) | decide in review whether the readings matter |
| 03.04.33 | variant | footnote of the print edition: 'saṁbhavati'iti pā+ | S1 (apparatus.tsv has the full text) | decide in review whether the readings matter |
| 03.04.37 | variant | editor remark [..] removed from the line: ['vaiguṇye'iti pā+] | S1 (apparatus.tsv has the full text) | decide in review whether the readings matter |
| 03.04.38 | variant | editor remark [..] removed from the line: ['gauravajvarāgnidaurbalyāni'iti pā+] | S1 (apparatus.tsv has the full text) | decide in review whether the readings matter |
| 03.04.4 | variant | editor remark [..] removed from the line: ['śukraśoṇitasya'iti keṣuciddhastalikhitapustakeṣu nopalabhyate/] | S1 (apparatus.tsv has the full text) | decide in review whether the readings matter |
| 03.04.4 | variant | editor remark [..] removed from the line: ['śarīre ṣaṭ tvacaḥ;-----'(ca.śā.a.7.sū.5)/ 'ṣaṣṭhī tu prāṇadharā' iti āṣṭāṅgasaṁgrahe pāṭhaḥ/ 'tvaco nāma---sarvadehāvaraṇarūpā bhūmiḥ sparśanevdriya... | S1 (apparatus.tsv has the full text) | decide in review whether the readings matter |
| 03.04.41 | variant | editor remark [..] removed from the line: [ayamardhaślokaḥ keṣucitpustakeṣu nopalabhyate/] | S1 (apparatus.tsv has the full text) | decide in review whether the readings matter |
| 03.04.47 | variant | editor remark [..] removed from the line: ['vamennidrātiyoge tu kuryāt'iti pā+] | S1 (apparatus.tsv has the full text) | decide in review whether the readings matter |
| 03.04.49 | variant | footnote of the print edition: 'yasyaite'iti pā+/ | S1 (apparatus.tsv has the full text) | decide in review whether the readings matter |
| 03.04.5 | variant | footnote of the print edition: 'bhavanti'iti pā+ | S1 (apparatus.tsv has the full text) | decide in review whether the readings matter |
| 03.04.53 | variant | footnote of the print edition: 'prāṇakoṣṭhānileritam'iti pā+ | S1 (apparatus.tsv has the full text) | decide in review whether the readings matter |
| 03.04.55 | variant | footnote of the print edition: 'gātraṁ manyate naraḥ'iti pā+ | S1 (apparatus.tsv has the full text) | decide in review whether the readings matter |
| 03.04.6 | variant | editor remark [..] removed from the line: ['bhavanti cātra'iti pā+] | S1 (apparatus.tsv has the full text) | decide in review whether the readings matter |
| 03.04.60 | variant | footnote of the print edition: 'kathaṁ ca na'iti pā+ | S1 (apparatus.tsv has the full text) | decide in review whether the readings matter |
| 03.04.64 | variant | editor remark [..] removed from the line: ['atirūkṣaśmaśrunakhakeśaḥ'iti pā+] | S1 (apparatus.tsv has the full text) | decide in review whether the readings matter |
| 03.04.64 | variant | footnote of the print edition: 'krodhī'iti pā+ | S1 (apparatus.tsv has the full text) | decide in review whether the readings matter |
| 03.04.65 | variant | footnote of the print edition: 'viyadapi'iti pā+ | S1 (apparatus.tsv has the full text) | decide in review whether the readings matter |
| 03.04.66 | variant | footnote of the print edition: 'mārutaprakṛtirasthirasattvaḥ'iti pā+ | S1 (apparatus.tsv has the full text) | decide in review whether the readings matter |
| 03.04.7 | variant | editor remark [..] removed from the line: ['asyāgre'+adhātvāśayāntare+annasya yaḥ kledastvadhiṣṭhati/ dehoṣmaṇā vipakvastu sā kaletyabhidhīyate' ityadhikaṁ paṭhyate kvacitpustake/] | S1 (apparatus.tsv has the full text) | decide in review whether the readings matter |
| 03.04.78 | variant | footnote of the print edition: 'vā+anyathābhāvaḥ'iti pā+ | S1 (apparatus.tsv has the full text) | decide in review whether the readings matter |
| 03.04.8 | variant | editor remark [..] removed from the line: ['māṁsagatānāṁ'iti hārāṇacandrasaṁmataḥ pāṭhaḥ/ 'māṁsasirāsnāyudhamanīsrotasāṁ' iti vai.paṁ.hariprapannasaṁmataḥ pāṭhaḥ/ viśeṣavivaraṇaṁ tu rasayogasā... | S1 (apparatus.tsv has the full text) | decide in review whether the readings matter |
| 03.04.86 | variant | footnote of the print edition: 'rāgamohabhayadveṣairvarjito yamasattvavān' pā+ | S1 (apparatus.tsv has the full text) | decide in review whether the readings matter |
| 03.04.90 | variant | editor remark [..] removed from the line: ['abaddhakāmasevī'iti pā+] | S1 (apparatus.tsv has the full text) | decide in review whether the readings matter |
| 03.04.92 | variant | footnote of the print edition: 'bhṛśamātraṁ tamaścāpi'iti pā+ | S1 (apparatus.tsv has the full text) | decide in review whether the readings matter |
| 03.05.11 | variant | editor remark [..] removed from the line: ['nitambaḥ'iti pā+/hārāṇacandrastu+abimbaḥ'iti paṭhitvā+abimbaḥ sacchidraṁ trikāsthi ucyate'iti vyākhyānayati/] | S1 (apparatus.tsv has the full text) | decide in review whether the readings matter |
| 03.05.11 | variant | editor remark [..] removed from the line: ['ūruvakṣo+akṣapiṇḍādigatānāṁ ca mūrdhā'iti hārāṇacandraḥ paṭhati/+amūrdhoruvakṣo+akṣapiṇḍādīnāṁ ca'iti pā+] | S1 (apparatus.tsv has the full text) | decide in review whether the readings matter |
| 03.05.11 | variant | footnote of the print edition: 'saṁbandhanīnāṁ'iti pā+ | S1 (apparatus.tsv has the full text) | decide in review whether the readings matter |
| 03.05.15 | variant | footnote of the print edition: 'sīvanyaḥ'iti pā+ | S1 (apparatus.tsv has the full text) | decide in review whether the readings matter |
| 03.05.17 | variant | editor remark [..] removed from the line: [vāgbhaṭastu "gulphajānuvaṁkṣaṇamaṇibandhakūrparakskṣāsu ekaikaḥ, trike ekaḥ, pañca śirasi" ityaṣṭādaśa sīmantānāḥ; saṁghātāṁstu caturdaśaiva//] | S1 (apparatus.tsv has the full text) | decide in review whether the readings matter |
| 03.05.17 | variant | footnote of the print edition: 'sīmantāstu khalvaṣṭādaśakeṣām'iti pā+ | S1 (apparatus.tsv has the full text) | decide in review whether the readings matter |
| 03.05.18 | variant | footnote of the print edition: 'ṣaṣṭyadhi(?)kāni'iti pā+ | S1 (apparatus.tsv has the full text) | decide in review whether the readings matter |
| 03.05.19 | variant | editor remark [..] removed from the line: [pratipārśva dvādaśa paśukāḥ, dvādaśa sthālakāni, dvādaśa sthālakārbudānīti militvā ṣaṭtriṁśadasthīni jñeyāni/] | S1 (apparatus.tsv has the full text) | decide in review whether the readings matter |
| 03.05.19 | variant | editor remark [..] removed from the line: [aṣṭāvurasīti uraḥphalake ṣaṭ, akṣakasaṁjñe dve; iti militvā+aṣṭāvurasyasthīni jñeyāni/] | S1 (apparatus.tsv has the full text) | decide in review whether the readings matter |
| 03.05.19 | variant | editor remark [..] removed from the line: ['dve akṣakasaṁjñe' iti pā+] | S1 (apparatus.tsv has the full text) | decide in review whether the readings matter |
| 03.05.19 | variant | editor remark [..] removed from the line: [atra+akaṇṭhanāḍyāṁ trīṇi, ekaṁ hanau, dantā dvātriṁśat, nāsāyāṁ nava, tāluni dve, gaṇḍayordve, śaṅkhayordve, karṇayoḥ ṣaṭ, ṣaṭ śirasi' iti pāṭho rasa... | S1 (apparatus.tsv has the full text) | decide in review whether the readings matter |
| 03.05.19 | variant | footnote of the print edition: 'bhagagudanitambeṣu'iti pā+ | S1 (apparatus.tsv has the full text) | decide in review whether the readings matter |
| 03.05.20 | variant | editor remark [..] removed from the line: ['pāṇipādapārśvapṛṣṭhodaroraḥsu valayāni' iti pāṭhastu na samīcīnaḥ, ṭīkāyāmuktena bhojavacanena saha virodhāt pratyakṣavirodhācca/] | S1 (apparatus.tsv has the full text) | decide in review whether the readings matter |
| 03.05.24 | variant | editor remark [..] removed from the line: ['ceṣṭāvantaḥ sandhayo dvividhāḥ---bahuceṣṭā alpaceṣṭāśceti kṛtvā/ tatra śākhāsu adho hanukoṭyośca bahuceṣṭāḥ, pṛṣṭhavaṁśādiṣvalpaceṣṭāḥ, anyatra puna... | S1 (apparatus.tsv has the full text) | decide in review whether the readings matter |
| 03.05.26 | variant | editor remark [..] removed from the line: [kecittvatra+anāḍīṣu phupphusaklomanibaddhāsu'iti paṭhanti/+atrayaḥ kaṇṭhe, trayaḥ kaṇṭhanāḍyāṁ, hṛdayaklomanibaddhāsu nāḍīṣvaṣṭādaśa'iti pā+] | S1 (apparatus.tsv has the full text) | decide in review whether the readings matter |
| 03.05.26 | variant | editor remark [..] removed from the line: ['nāsāyāṁ pañca, dvau dvāveva dvayornetrayorbhavataḥ, dvau vartmamaṇḍalajau netrāśrayau'iti pā+] | S1 (apparatus.tsv has the full text) | decide in review whether the readings matter |
| 03.05.27 | variant | editor remark [..] removed from the line: ['tatra korā nāma sandhayo bahuveṣṭāḥ, uttānakoragarbheṣvasthiprānteṣu utsedhavatāmasthibhāgānāṁ sandhānarūpāḥ/ udūkhalā nāma sandhayo+api bahuceṣṭāḥ,... | S1 (apparatus.tsv has the full text) | decide in review whether the readings matter |
| 03.05.27 | variant | footnote of the print edition: 'aṁsapīṭhagudapādanitambeṣu' iti pā+ | S1 (apparatus.tsv has the full text) | decide in review whether the readings matter |
| 03.05.27 | variant | footnote of the print edition: 'hanvoḥ'iti pā+ | S1 (apparatus.tsv has the full text) | decide in review whether the readings matter |
| 03.05.29 | variant | editor remark [..] removed from the line: [asyāgre+amahāsnāyostu kaṇḍareti saṁjñā'ityadhikaṁ paṭhyate kvacitpustake] | S1 (apparatus.tsv has the full text) | decide in review whether the readings matter |
| 03.05.29 | variant | footnote of the print edition: 'ṣaṭ ṣaṭ' iti pā+ | S1 (apparatus.tsv has the full text) | decide in review whether the readings matter |
| 03.05.3 | variant | footnote of the print edition: 'hastapādajihvāghrāṇakarṇādibhiḥ'iti pā+ | S1 (apparatus.tsv has the full text) | decide in review whether the readings matter |
| 03.05.37 | variant | editor remark [..] removed from the line: ['ṣaṭ śirasi'iti pā+] | S1 (apparatus.tsv has the full text) | decide in review whether the readings matter |
| 03.05.37 | variant | footnote of the print edition: 'hanusamākhye'iti hārāṇacandrasaṁmataḥ pāṭhaḥ | S1 (apparatus.tsv has the full text) | decide in review whether the readings matter |
| 03.05.37 | variant | footnote of the print edition: 'jihvāyāṁ dve'iti pā+ | S1 (apparatus.tsv has the full text) | decide in review whether the readings matter |
| 03.05.37 | variant | footnote of the print edition: 'catasro netrayoḥ'iti pā+ | S1 (apparatus.tsv has the full text) | decide in review whether the readings matter |
| 03.05.39 | variant | editor remark [..] removed from the line: ['atra+abastipakvāśayamadhye garbhāśayaḥ'iti pāṭhe bhavitumarhati,+aśarīre tathaiva darśanādanyathā pratyakṣavirodhācca' iti pratyakṣaśārīropoddhāte(p... | S1 (apparatus.tsv has the full text) | decide in review whether the readings matter |
| 03.05.39 | variant | footnote of the print edition: 'bhagāpatyapathe'iti pā+ | S1 (apparatus.tsv has the full text) | decide in review whether the readings matter |
| 03.05.39 | variant | footnote of the print edition: 'śukrārtavapraveśinyo garbhāśaye tisra eva'iti pā+ | S1 (apparatus.tsv has the full text) | decide in review whether the readings matter |
| 03.05.4 | variant | editor remark [..] removed from the line: ['vakṣyante'iti pā+] | S1 (apparatus.tsv has the full text) | decide in review whether the readings matter |
| 03.05.41 | variant | footnote of the print edition: 'lakṣaṇamuṣkayoḥ/ strīṇāmāśritya'iti pā+ | S1 (apparatus.tsv has the full text) | decide in review whether the readings matter |
| 03.05.46 | variant | footnote of the print edition: 'naiva'iti pā+ | S1 (apparatus.tsv has the full text) | decide in review whether the readings matter |
| 03.05.47 | variant | footnote of the print edition: 'jñānamicchatā śalyajīvinā'iti pā+ | S1 (apparatus.tsv has the full text) | decide in review whether the readings matter |
| 03.05.47 | variant | footnote of the print edition: 'tāvat'iti pā+ | S1 (apparatus.tsv has the full text) | decide in review whether the readings matter |
| 03.05.48 | variant | footnote of the print edition: 'samāgataṁ dvayaṁ tattu'iti pā+ | S1 (apparatus.tsv has the full text) | decide in review whether the readings matter |
| 03.05.49 | variant | editor remark [..] removed from the line: ['+balvaja+'iti pā+] | S1 (apparatus.tsv has the full text) | decide in review whether the readings matter |
| 03.05.5 | variant | footnote of the print edition: 'saṁkhyeyāni'iti pā+ | S1 (apparatus.tsv has the full text) | decide in review whether the readings matter |
| 03.05.5 | variant | footnote of the print edition: 'yogavāhīni'iti pā+ | S1 (apparatus.tsv has the full text) | decide in review whether the readings matter |
| 03.05.50a | variant | editor remark [..] removed from the line: [ayaṁ pāṭho hastalikhitapustake nopalabhyate/] | S1 (apparatus.tsv has the full text) | decide in review whether the readings matter |
| 03.05.6 | variant | editor remark [..] removed from the line: [dvikānyantrāṇīti sūkṣmasthūlabhedena/] | S1 (apparatus.tsv has the full text) | decide in review whether the readings matter |
| 03.05.6 | variant | editor remark [..] removed from the line: [ayaṁ pāṭho hastalikhitapustake nopalabhyate/ hārāṇacandrapaṭhitatvādasmābhiḥ paṭhitaḥ/] | S1 (apparatus.tsv has the full text) | decide in review whether the readings matter |
| 03.06.10 | variant | editor remark [..] removed from the line: ['pārśvagau'iti+apārśvayoḥ'iti ca pā+] | S1 (apparatus.tsv has the full text) | decide in review whether the readings matter |
| 03.06.16 | variant | editor remark [..] removed from the line: [ayaṁ pāṭhaḥ keṣucitpustakeṣu nopalabhayate] | S1 (apparatus.tsv has the full text) | decide in review whether the readings matter |
| 03.06.16 | variant | footnote of the print edition: 'viśeṣeṇa'iti pā+ | S1 (apparatus.tsv has the full text) | decide in review whether the readings matter |
| 03.06.17 | variant | footnote of the print edition: 'samavṛddhānāṁ'iti pā+ | S1 (apparatus.tsv has the full text) | decide in review whether the readings matter |
| 03.06.17 | variant | footnote of the print edition: 'ca'iti pā+ | S1 (apparatus.tsv has the full text) | decide in review whether the readings matter |
| 03.06.17 | variant | footnote of the print edition: 'viśalyaghnāni'iti pā+ | S1 (apparatus.tsv has the full text) | decide in review whether the readings matter |
| 03.06.17 | variant | footnote of the print edition: 'yataścaivamato'iti pā+ | S1 (apparatus.tsv has the full text) | decide in review whether the readings matter |
| 03.06.18 | variant | footnote of the print edition: 'pratiyāpayanti'iti pā+ | S1 (apparatus.tsv has the full text) | decide in review whether the readings matter |
| 03.06.22 | variant | editor remark [..] removed from the line: ['viśalyaprāṇaharamante viddhaṁ kleśayati kālāntareṇa ca rujāṁ karoti' iti pā+] | S1 (apparatus.tsv has the full text) | decide in review whether the readings matter |
| 03.06.24 | variant | editor remark [..] removed from the line: [atra+amāma'iti hastalikhitapustake nopalabhyate, evamagre+api/] | S1 (apparatus.tsv has the full text) | decide in review whether the readings matter |
| 03.06.24 | variant | editor remark [..] removed from the line: ['madhyamāṅgulīmānupūrvyeṇa jaṅghorvoḥ'iti pā+] | S1 (apparatus.tsv has the full text) | decide in review whether the readings matter |
| 03.06.24 | variant | editor remark [..] removed from the line: ['lohitakṣayeṇa maraṇaṁ pakṣāghāto vā'iti pā+] | S1 (apparatus.tsv has the full text) | decide in review whether the readings matter |
| 03.06.24 | variant | footnote of the print edition: 'kṣipramiti marma'iti pā+ | S1 (apparatus.tsv has the full text) | decide in review whether the readings matter |
| 03.06.24 | variant | footnote of the print edition: 'jānusandherubhayatastryaṅgule'iti pā+ | S1 (apparatus.tsv has the full text) | decide in review whether the readings matter |
| 03.06.24 | variant | footnote of the print edition: 'ūrumadhye lohitākhyaṁ'iti pā+ | S1 (apparatus.tsv has the full text) | decide in review whether the readings matter |
| 03.06.25 | variant | editor remark [..] removed from the line: ['marmasdhānānyanuvyākhyāsyāmaḥ'iti pā+] | S1 (apparatus.tsv has the full text) | decide in review whether the readings matter |
| 03.06.25 | variant | editor remark [..] removed from the line: ['stanacūcukayormadhye stanarohitau'iti pā+] | S1 (apparatus.tsv has the full text) | decide in review whether the readings matter |
| 03.06.25 | variant | editor remark [..] removed from the line: [stanamūlalakṣaṇe+astanayorūrdhvaṁ'iti / stanarohitalakṣaṇe ca+astanacūcukayoradhastāt'iti ca rasayogasāgarasyopoddhāte(pṛ.158) ca saṁśodhitaḥ pāṭhaḥ/... | S1 (apparatus.tsv has the full text) | decide in review whether the readings matter |
| 03.06.25 | variant | footnote of the print edition: 'marmaṇī'iti hastalikhitapustake nopalabhyate / | S1 (apparatus.tsv has the full text) | decide in review whether the readings matter |
| 03.06.26 | variant | footnote of the print edition: 'anuvyākhyāsyāmaḥ'iti pā+ | S1 (apparatus.tsv has the full text) | decide in review whether the readings matter |
| 03.06.26 | variant | footnote of the print edition: 'nāma marmaṇī'iti hastalikhitapustake na paṭhyate/ | S1 (apparatus.tsv has the full text) | decide in review whether the readings matter |
| 03.06.26 | variant | footnote of the print edition: 'hīnadehaśca'iti pā+ | S1 (apparatus.tsv has the full text) | decide in review whether the readings matter |
| 03.06.26 | variant | footnote of the print edition: 'nāma marmaṇī'itihastalikhitapustake nopalabhyate/ | S1 (apparatus.tsv has the full text) | decide in review whether the readings matter |
| 03.06.26 | variant | footnote of the print edition: 'bṛhatī'iti pā+ | S1 (apparatus.tsv has the full text) | decide in review whether the readings matter |
| 03.06.26 | variant | footnote of the print edition: 'svāpaḥ śoṣo vā'iti pā+ | S1 (apparatus.tsv has the full text) | decide in review whether the readings matter |
| 03.06.27 | variant | editor remark [..] removed from the line: ['bhruvorantopari'iti pā+] | S1 (apparatus.tsv has the full text) | decide in review whether the readings matter |
| 03.06.27 | variant | footnote of the print edition: 'nāma vyatyayena'iti pā+ | S1 (apparatus.tsv has the full text) | decide in review whether the readings matter |
| 03.06.27 | variant | footnote of the print edition: 'catasraścatasraḥ'iti pā+ | S1 (apparatus.tsv has the full text) | decide in review whether the readings matter |
| 03.06.27 | variant | footnote of the print edition: 'śṛṅgāṭakasaṁjñaścaturdhā, tatrāpi'iti pā+ | S1 (apparatus.tsv has the full text) | decide in review whether the readings matter |
| 03.06.27 | variant | footnote of the print edition: 'sadyomaraṇaṁ'iti pā+ | S1 (apparatus.tsv has the full text) | decide in review whether the readings matter |
| 03.06.32 | variant | editor remark [..] removed from the line: ['ivāyudhanipātanikṛttamūlāḥ'iti pā+] | S1 (apparatus.tsv has the full text) | decide in review whether the readings matter |
| 03.06.35 | variant | footnote of the print edition: 'aśeṣaṁ'iti pā+ | S1 (apparatus.tsv has the full text) | decide in review whether the readings matter |
| 03.06.35 | variant | footnote of the print edition: 'marmasu kṛtā'iti pā+ | S1 (apparatus.tsv has the full text) | decide in review whether the readings matter |
| 03.06.6 | variant | footnote of the print edition: '+stanarohitāpastambhāvapalāpau ceti'iti pā+ | S1 (apparatus.tsv has the full text) | decide in review whether the readings matter |
| 03.06.7 | variant | editor remark [..] removed from the line: ['ime sirāmarmaṇī,'grīvāyāṁ ṣoḍaśa avyadhyāḥ' ityatra ḍalhaṇenaiva vidhurayoḥ ṣoḍaśasaṁkhyāyāmeva parigaṇanaṁ kṛtaṁ, snāyumarmasu gaṇanaṁ tu pratisaṁs... | S1 (apparatus.tsv has the full text) | decide in review whether the readings matter |
| 03.06.9 | variant | footnote of the print edition: 'sadyoharāṇi'iti pā+ | S1 (apparatus.tsv has the full text) | decide in review whether the readings matter |
| 03.07.1 | variant | footnote of the print edition: 'sirāvarṇavibhaktiśārīraṁ' iti pā+ | S1 (apparatus.tsv has the full text) | decide in review whether the readings matter |
| 03.07.17 | variant | footnote of the print edition: 'doṣāṇāmucchritānāṁ'iti pā+ | S1 (apparatus.tsv has the full text) | decide in review whether the readings matter |
| 03.07.22 | variant | footnote of the print edition: 'lohitākṣasaṁjñaikā'iti pā+ | S1 (apparatus.tsv has the full text) | decide in review whether the readings matter |
| 03.07.22 | variant | footnote of the print edition: 'pṛṣṭhe'iti na paṭhyate keṣucitpustakeṣu | S1 (apparatus.tsv has the full text) | decide in review whether the readings matter |
| 03.07.22 | variant | footnote of the print edition: 'tatrāṣṭapañcāśat'iti pā+ | S1 (apparatus.tsv has the full text) | decide in review whether the readings matter |
| 03.07.22 | variant | footnote of the print edition: 'ṣaṭtriṁśadubhayornetrayoḥ'iti pā+ | S1 (apparatus.tsv has the full text) | decide in review whether the readings matter |
| 03.07.4 | variant | editor remark [..] removed from the line: ['pravartante' iti pā+] | S1 (apparatus.tsv has the full text) | decide in review whether the readings matter |
| 03.07.7 | variant | footnote of the print edition: 'vātavāhinīnāṁ' iti pā+ | S1 (apparatus.tsv has the full text) | decide in review whether the readings matter |
| 03.08.14 | variant | footnote of the print edition: 'vihatasya' iti pā+ | S1 (apparatus.tsv has the full text) | decide in review whether the readings matter |
| 03.08.14 | variant | footnote of the print edition: 'hyaparedyuḥ' iti pā+ | S1 (apparatus.tsv has the full text) | decide in review whether the readings matter |
| 03.08.15 | variant | footnote of the print edition: 'niḥsrutaṁ' iti pā+ | S1 (apparatus.tsv has the full text) | decide in review whether the readings matter |
| 03.08.17 | variant | editor remark [..] removed from the line: ['kenacidatrāvabāhuko+api paṭhyate, tatra samīcīnaṁ, pratikāravidhāvasya vyadhena jihāsitatvāt'iti hārāṇacandraḥ/+acippa'iti kvacinna paṭhyate/] | S1 (apparatus.tsv has the full text) | decide in review whether the readings matter |
| 03.08.17 | variant | editor remark [..] removed from the line: ['atra+ayakṛddāsye kaphodare ca' ityanākaraḥ pāṭhaḥ, kaphodare sirāvyadhasyānupayogāt'iti hārāṇacandraḥ] | S1 (apparatus.tsv has the full text) | decide in review whether the readings matter |
| 03.08.17 | variant | editor remark [..] removed from the line: ['aho guroraśrutasuśrutaḥ kaścit mūtravṛddhyāṁ dakodare ca doṣodakāvasecanārthaṁ vidhitsite vyadhane eva sirāvyadhau manyamāno+atra+avṛṣaṇayoḥ pārśve ... | S1 (apparatus.tsv has the full text) | decide in review whether the readings matter |
| 03.08.17 | variant | editor remark [..] removed from the line: [asyāgra+aetāmeva kaphodare vāmapārśve'ityadhikaṁ paṭhyate kvacitpustake] | S1 (apparatus.tsv has the full text) | decide in review whether the readings matter |
| 03.08.17 | variant | footnote of the print edition: 'yakṛddālye'iti pā+ | S1 (apparatus.tsv has the full text) | decide in review whether the readings matter |
| 03.08.18 | variant | footnote of the print edition: 'anteviddhā'iti pā+ | S1 (apparatus.tsv has the full text) | decide in review whether the readings matter |
| 03.08.19 | variant | footnote of the print edition: 'na vyaktamasṛk'iti pā+ | S1 (apparatus.tsv has the full text) | decide in review whether the readings matter |
| 03.08.19 | variant | footnote of the print edition: 'atipravṛttaśoṇitā'iti pā+ | S1 (apparatus.tsv has the full text) | decide in review whether the readings matter |
| 03.08.19 | variant | footnote of the print edition: 'vicchinnā'iti pāṭhāntaram | S1 (apparatus.tsv has the full text) | decide in review whether the readings matter |
| 03.08.24 | variant | editor remark [..] removed from the line: ['+divāsvapnavyāyāma+'iti pā+] | S1 (apparatus.tsv has the full text) | decide in review whether the readings matter |
| 03.08.6 | variant | editor remark [..] removed from the line: ['pratipītaṁ' iti pā+] | S1 (apparatus.tsv has the full text) | decide in review whether the readings matter |
| 03.08.6 | variant | editor remark [..] removed from the line: ['yathoktaṁ śastraṁ gṛhītvā' iti pāṭhāntaram/] | S1 (apparatus.tsv has the full text) | decide in review whether the readings matter |
| 03.08.8 | variant | editor remark [..] removed from the line: ['sakthnorākuñcitayorupari kurparasandhidvayaṁ niveśya' iti pā+] | S1 (apparatus.tsv has the full text) | decide in review whether the readings matter |
| 03.08.8 | variant | editor remark [..] removed from the line: ['yantraṁ pīḍayoti'+apṛṣṭhamadhye ca pīḍayet' iti pā+] | S1 (apparatus.tsv has the full text) | decide in review whether the readings matter |
| 03.08.8 | variant | editor remark [..] removed from the line: ['hastābhyāṁ vā prapīḍya gulphaṁ' iti pā+] | S1 (apparatus.tsv has the full text) | decide in review whether the readings matter |
| 03.08.8 | variant | footnote of the print edition: 'karmapuruṣasya mukhaṁ vāyunā pūrayet' iti pā+ | S1 (apparatus.tsv has the full text) | decide in review whether the readings matter |
| 03.08.8 | variant | footnote of the print edition: 'bandhopāyān' iti pā+ | S1 (apparatus.tsv has the full text) | decide in review whether the readings matter |
| 03.08.9 | variant | footnote of the print edition: 'ato+anyathā+ardhayavamātraṁ' iti pā+ | S1 (apparatus.tsv has the full text) | decide in review whether the readings matter |
| 03.09.10 | variant | editor remark [..] removed from the line: ['bhavataścātra'iti hastalikhitapustakeṣu nopalabhyate/] | S1 (apparatus.tsv has the full text) | decide in review whether the readings matter |
| 03.09.12 | variant | footnote of the print edition: 'prāṇavāhinyaśca' iti pā+ | S1 (apparatus.tsv has the full text) | decide in review whether the readings matter |
| 03.09.12 | variant | footnote of the print edition: 'pipāsā+asadhyā śyāvāṅgatā' iti pā+ | S1 (apparatus.tsv has the full text) | decide in review whether the readings matter |
| 03.09.12 | variant | footnote of the print edition: 'śoṇitātigamanaṁ' iti pā+ | S1 (apparatus.tsv has the full text) | decide in review whether the readings matter |
| 03.09.12 | variant | footnote of the print edition: 'vā+aprasekaśca' iti pā+ | S1 (apparatus.tsv has the full text) | decide in review whether the readings matter |
| 03.09.6 | variant | footnote of the print edition: 'yathātatham'iti pā+ | S1 (apparatus.tsv has the full text) | decide in review whether the readings matter |
| 03.09.7 | variant | editor remark [..] removed from the line: ['tā eva raktamabhivahanti'iti pā+] | S1 (apparatus.tsv has the full text) | decide in review whether the readings matter |
| 03.09.7 | variant | footnote of the print edition: 'cordhvaṁgatānāṁ tiryaggatānāṁ'iti pā+ | S1 (apparatus.tsv has the full text) | decide in review whether the readings matter |
| 03.09.7 | variant | footnote of the print edition: 'trividhā'iti pāṭhāntaram | S1 (apparatus.tsv has the full text) | decide in review whether the readings matter |
| 03.09.7 | variant | footnote of the print edition: 'visṛjataḥ'iti keṣucitpustakeṣu nopalabhyate | S1 (apparatus.tsv has the full text) | decide in review whether the readings matter |
| 03.09.9 | variant | editor remark [..] removed from the line: ['cāpi saṁtaparyanti'iti pā+] | S1 (apparatus.tsv has the full text) | decide in review whether the readings matter |
| 01.05.17 | other | reference (..) removed from the line: (ā.jya) | S1 (apparatus.tsv has the full text) | decide in review whether the readings matter |
| 01.07.10 | other | reference (..) removed from the line: (ā.ndī) | S1 (apparatus.tsv has the full text) | decide in review whether the readings matter |
| 01.07.21b | other | reference (..) removed from the line: (ā.śā) | S1 (apparatus.tsv has the full text) | decide in review whether the readings matter |
| 01.07.22a | other | reference (..) removed from the line: (ā.vi) | S1 (apparatus.tsv has the full text) | decide in review whether the readings matter |
| 01.07.22b | other | reference (..) removed from the line: (ā.vi) | S1 (apparatus.tsv has the full text) | decide in review whether the readings matter |
| 01.09.4 | other | reference (..) removed from the line: (ā.so) | S1 (apparatus.tsv has the full text) | decide in review whether the readings matter |
| 01.11.5 | other | reference (..) removed from the line: (ā.pā) | S1 (apparatus.tsv has the full text) | decide in review whether the readings matter |
| 01.11.9 | other | reference (..) removed from the line: (ā.tti) | S1 (apparatus.tsv has the full text) | decide in review whether the readings matter |
| 01.12.16 | other | reference (..) removed from the line: (ā.naṁ) | S1 (apparatus.tsv has the full text) | decide in review whether the readings matter |
| 01.13.21 | other | reference (..) removed from the line: (ā.raktamado) | S1 (apparatus.tsv has the full text) | decide in review whether the readings matter |
| 01.14.18 | other | reference (..) removed from the line: (ā.naiva cā) | S1 (apparatus.tsv has the full text) | decide in review whether the readings matter |
| 01.14.18 | other | reference (..) removed from the line: (ā.jñā) | S1 (apparatus.tsv has the full text) | decide in review whether the readings matter |
| 01.15.26-27 | other | reference (..) removed from the line: (O.kriyā) | S1 (apparatus.tsv has the full text) | decide in review whether the readings matter |
| 01.15.9 | other | reference (..) removed from the line: (ā.tā) | S1 (apparatus.tsv has the full text) | decide in review whether the readings matter |
| 01.17.10 | other | reference (..) removed from the line: (ā.dī) | S1 (apparatus.tsv has the full text) | decide in review whether the readings matter |
| 01.17.17a | other | reference (..) removed from the line: (ā.yvī) | S1 (apparatus.tsv has the full text) | decide in review whether the readings matter |
| 01.18.12 | other | reference (..) removed from the line: (ā.ddhi) | S1 (apparatus.tsv has the full text) | decide in review whether the readings matter |
| 01.18.17 | other | reference (..) removed from the line: (ā.mu) | S1 (apparatus.tsv has the full text) | decide in review whether the readings matter |
| 01.19.29 | other | reference (..) removed from the line: (ā.ṅga) | S1 (apparatus.tsv has the full text) | decide in review whether the readings matter |
| 01.19.35b | other | mark ^ removed from the line: ^ | S1 (apparatus.tsv has the full text) | decide in review whether the readings matter |
| 01.23.12 | other | reference (..) removed from the line: (ā.kṣīṇamāṃsānāṃ ca) | S1 (apparatus.tsv has the full text) | decide in review whether the readings matter |
| 01.27.5 | other | reference (..) removed from the line: (ā.pā) | S1 (apparatus.tsv has the full text) | decide in review whether the readings matter |
| 01.29.15b | other | mark ^ removed from the line: ^ | S1 (apparatus.tsv has the full text) | decide in review whether the readings matter |
| 01.29.36b | other | mark ^ removed from the line: ^ | S1 (apparatus.tsv has the full text) | decide in review whether the readings matter |
| 01.29.63b | other | reference (..) removed from the line: (ā.vā) | S1 (apparatus.tsv has the full text) | decide in review whether the readings matter |
| 01.34.5b | other | mark ^ removed from the line: ^ | S1 (apparatus.tsv has the full text) | decide in review whether the readings matter |
| 01.35.11b | other | mark ^ removed from the line: ^ | S1 (apparatus.tsv has the full text) | decide in review whether the readings matter |
| 01.36.7 | other | reference (..) removed from the line: (ā.sarvāṇyeva sakṣīrāṇi vīryavanti ) | S1 (apparatus.tsv has the full text) | decide in review whether the readings matter |
| 01.36.7 | other | reference (..) removed from the line: (ā.na) | S1 (apparatus.tsv has the full text) | decide in review whether the readings matter |
| 01.37.10b | other | mark ^ removed from the line: ^ | S1 (apparatus.tsv has the full text) | decide in review whether the readings matter |
| 01.38.6 | other | reference (..) removed from the line: (ā.rṅge) | S1 (apparatus.tsv has the full text) | decide in review whether the readings matter |
| 01.39.8 | other | reference (..) removed from the line: (ā.da) | S1 (apparatus.tsv has the full text) | decide in review whether the readings matter |
| 01.40.20b | other | reference (..) removed from the line: (ā.dā) | S1 (apparatus.tsv has the full text) | decide in review whether the readings matter |
| 01.41.4.3 | other | reference (..) removed from the line: (ā.guṇa) | S1 (apparatus.tsv has the full text) | decide in review whether the readings matter |
| 01.42.5 | other | reference (..) removed from the line: (ā.yu) | S1 (apparatus.tsv has the full text) | decide in review whether the readings matter |
| 01.44.38b | other | reference (..) removed from the line: (ā.tra) | S1 (apparatus.tsv has the full text) | decide in review whether the readings matter |
| 01.45.160 | other | reference (..) removed from the line: (ā.kṛmi) | S1 (apparatus.tsv has the full text) | decide in review whether the readings matter |
| 01.45.181b | other | reference (..) removed from the line: (ā.kka) | S1 (apparatus.tsv has the full text) | decide in review whether the readings matter |
| 01.46 | other | chapter has 1032 lines, over 1000; kept whole in ch01.46.md | S1 | owner decides |
| 01.46.249 | other | reference (..) removed from the line: (ā.ndī) | S1 (apparatus.tsv has the full text) | decide in review whether the readings matter |
| 01.46.290 | other | reference (..) removed from the line: (ā.ca) | S1 (apparatus.tsv has the full text) | decide in review whether the readings matter |
| 01.46.313 | other | reference (..) removed from the line: (ā.atha lavaṇāni) | S1 (apparatus.tsv has the full text) | decide in review whether the readings matter |
| 01.46.378a | other | reference (..) removed from the line: (ā.khā) | S1 (apparatus.tsv has the full text) | decide in review whether the readings matter |
| 01.46.428b | other | reference (..) removed from the line: (ā.bha) | S1 (apparatus.tsv has the full text) | decide in review whether the readings matter |
| 01.46.445b | other | reference (..) removed from the line: (ā.nvi) | S1 (apparatus.tsv has the full text) | decide in review whether the readings matter |
| 01.46.471b | other | reference (..) removed from the line: (ā.vi) | S1 (apparatus.tsv has the full text) | decide in review whether the readings matter |
| 01.46.491a | other | reference (..) removed from the line: (ā.tya) | S1 (apparatus.tsv has the full text) | decide in review whether the readings matter |
| 01.46.501b | other | reference (..) removed from the line: (ā.ba) | S1 (apparatus.tsv has the full text) | decide in review whether the readings matter |
| 01.46.510a | other | reference (..) removed from the line: (ā.traṃ) | S1 (apparatus.tsv has the full text) | decide in review whether the readings matter |
