# FORMAT: how the extracted files are laid out

This file is copied into every book folder as `FORMAT.md`, so any agent can continue the work without the skill. It is the contract between the extraction stage and the later stages (verify, review, fix, proofread, quiz). Do not change it for a book that already has finished chapters.

## 1. Part / chapter / verse mapping

Every book is mapped onto three levels. Use the names the book itself uses and record the mapping in `toc.md`.

| Book | Part | Chapter | Verse |
|---|---|---|---|
| Charaka / Sushruta Samhita | sthāna (01 Sūtrasthāna ...) | adhyāya | verse or prose sūtra |
| Aṣṭāṅga Hṛdaya / Saṅgraha | sthāna | adhyāya | verse or prose |
| Ṛgveda | maṇḍala | sūkta | ṛc |
| Atharvaveda | kāṇḍa | sūkta | mantra |
| Yajurveda (Vājasaneyi) | none (00) | adhyāya | kaṇḍikā / mantra |
| Upaniṣads | none (00) | adhyāya / vallī / khaṇḍa | mantra / verse |
| Bhagavad Gītā | none (00) | adhyāya | verse |
| Purāṇas, Mahābhārata, Rāmāyaṇa | parva / kāṇḍa | adhyāya / sarga | verse |

If a book has no part level, use part `00`. If there is a level deeper than verse (a pāda), it is a line suffix (below). If a book has an extra level between part and chapter (for example a vallī), fold it into the chapter number and record the mapping in `toc.md`.

Numbers are zero-padded to 2 digits, or 3 digits when any part of the book has more than 99 chapters (decide once, for the whole book).

## 2. Files

```
text/ch01.02.md           Sanskrit, part 01 chapter 02
text/ch01.02-hindi.md     Hindi, same lines
text/ch01.02-english.md   English, same lines
text/p01.md               Sanskrit, a whole part in one file (chapters in order)
text/p01-hindi.md         and so on
```

- Chapter files and part files are chosen per part by size: if all chapters of a part together are under 1000 lines, one `pNN.md` file; otherwise one `chNN.CC.md` file per chapter in that part. Record the choice in the `File` column of `toc.md`.
- Every file is under 1000 lines. A chapter is never split across files. If one chapter is over 1000 lines it stays whole, is flagged in `STATUS.md`, and the owner decides.
- Text is UTF-8, NFC-normalised, LF line ends, one final newline, no BOM.
- Language suffix is lower case English: `-hindi`, `-english`, `-marathi`, `-commentary` is NOT allowed here (commentaries are a different stage).

## 3. Lines

Every line of every file is:

```
ID | text
```

`ID` is `PP.CC.V` or `PP.CC.Vx`, then a single space, a vertical bar, a single space, then the text.

- `PP` part, `CC` chapter, as in the file name.
- `V` is the verse number **as the source numbers it** (`3`, `12`, `3-4` when the source joins two verses, `8.1` when the source sub-numbers a passage; the sub-number form is an extension added for this book, the checker accepts it). Unnumbered prose paragraphs get `P1`, `P2`, ... in order. If the source has no numbers at all, count verses from 1 and note it in `sources.md`.
- `x` is a line letter (`a`, `b`, `c`, ...) when the verse is written on several lines in the source. Keep the source's own line breaks. A verse on one line has no letter.
- The ID never changes after the chapter is finished: later stages key on it.

Example (Sanskrit):

```
01.01.1 | अथातो दीर्घञ्जीवितीयमध्यायं व्याख्यास्यामः ॥
01.01.2 | इति ह स्माह भगवानात्रेयः ॥
01.01.3a | दीर्घं जीवितमन्विच्छन्भरद्वाज उपागमत्
01.01.3b | इन्द्रमुग्रतपा बुद्ध्वा शरण्यममरेश्वरम् ॥
```

(Illustration of the format only; the real text always comes from a source file.)

Same lines in the Hindi file:

```
01.01.1 | अब हम दीर्घञ्जीवितीय अध्याय की व्याख्या करेंगे।
01.01.2 | ऐसा भगवान आत्रेय ने कहा।
01.01.3a | दीर्घ जीवन की इच्छा से भरद्वाज इन्द्र के पास गए ...
01.01.3b | ~
```

### Text rules (Sanskrit files)

- Devanāgarī only: no Latin letters, no IAST. Keep the source's dandas (`।`, `॥`) and its sandhi and spelling exactly. Do not fix anything; doubts go to `ISSUES.md`.
- Keep verse numbers out of the text (they live in the ID). Remove a trailing `॥ ३ ॥`-style number but keep the closing `॥`.
- No empty lines, no headings, no comments inside text files. Chapter titles live in `toc.md`.
- Zero-width joiner/non-joiner characters are kept only if the source has them on purpose; the checker counts them so a reviewer can look.

### Translation files

- Exactly the Sanskrit file's IDs, in the same order, so line counts are equal.
- A translation written per verse goes on the verse's first line; later lines of that verse carry `~`.
- `~` also means: this line continues the sentence above.
- `--` means the translation source has nothing for this line.
- A translation never has lines the Sanskrit lacks. If the translation source has extra lines (a verse the Sanskrit edition omits), log it in `ISSUES.md` and leave it out.

## 4. Other files in the book folder

| File | Purpose |
|---|---|
| `README.md` | what the folder is, how to continue, rules (template in templates.md) |
| `FORMAT.md` | this file |
| `toc.md` | book structure, names, purposes, verse counts, file per chapter |
| `STATUS.md` | per-chapter progress ledger |
| `sources.md` | every source used: edition, licence, URL, how fetched, quality |
| `ISSUES.md` | every doubt, keyed by line ID |
| `raw/` | original source files, only if small and licence allows (otherwise URL plus checksum in `sources.md`) |
| `tools/` | parsers written for this book |

## 5. Suggestions beyond the original brief (kept simple)

- `ID | text` on every line is the one addition to "pure text" files. It lets a script prove that Sanskrit, Hindi and English line up, and lets the next stages point at a verse. Strip it with `cut -d'|' -f2-` if pure text is ever needed.
- Part-level files are named `pNN.md` and chapter-level `chNN.CC.md`, so a name never reads as both.
- Keeping all text files in one `text/` folder keeps the three languages next to each other when sorted.
