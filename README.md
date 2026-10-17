# सुश्रुतसंहिता — सूत्रस्थान (अध्याय १–५): Recall Quiz

A practice quiz for the book *सुश्रुतसंहिता — सूत्रस्थान (अध्याय १–५)* by Suśruta (SARIT edition). It teaches the
book's ideas as concept cards with question ladders, brings back the
questions you miss sooner (spaced repetition) and keeps your progress in
your browser (and, when you sign in with Google, synced across your
devices). Version 1 has 169 ideas and 1014
questions in 5 units.

The site is served by GitHub Pages from this repository's default branch:
<https://eckko.github.io/sushruta-samhita/>

## What is in this repository

Only the book's own files. All the quiz code comes from the shared
template.

| Path | What it is |
|---|---|
| `index.html` | A tiny loader: shows the favicon and loads the quiz from the template on the CDN |
| `questions.json` | The question bank |
| `images/favicon.png` | The browser-tab and home-screen icon (180x180): the book's name on a plain square (the text has no cover) |
| `images/aids/` | The 80 small diagrams and tables shown on the cards (SVG) |
| `media/` | Empty: this book has no cover or figures, its pictures are the SVGs in `images/aids/` |
| `verse_book.json`, `data/`, `tools/authored/` | The book's own source for the Sanskrit verse cards: settings, the reviewed verse data per chapter and the authored questions; `questions.json` is built from them |
| `book-structure/` | The chapter map the bank was built from |
| `tools/set_template_tag.py` | Moves the book to another template tag |

## How the quiz code is loaded

`index.html` loads `js/boot.js` from one tagged copy of
[`eckko/recall-quiz-site-template`](https://github.com/eckko/recall-quiz-site-template)
on jsDelivr (currently tag `2.2.1`). `boot.js` fetches the template's
page from the same tag and starts it. `questions.json`, `images/` and
`media/` are still read from this site.

To move the book to a newer template, run
`python3 tools/set_template_tag.py NEW_TAG` and commit `index.html`.
Always use an exact tag, never a branch.

## Change the questions

Never change a question's `id`: readers' saved progress is keyed by it.
Every change is a new version branch built with the `quiz-advanced-cdn`
skill. The fields, the checks (`validate_bank.py`) and the style rules are
in the template repository (`README.md`, `ai-context/`, `tools/`).

## Pictures (`media/`)

Pictures are stored as `media/<id>.enc` and open only with the book key,
so they are not freely downloadable from the repository. Without the key
the quiz shows each picture's description text instead.

## Try it on your computer

Run `python3 -m http.server` in this folder and open
<http://localhost:8000/>. It needs an internet connection, because the
code comes from the CDN.


## Source and licence

The Sanskrit text is the SARIT e-text of the Suśrutasaṃhitā (Yamashita and Muroya), licensed CC BY-SA 3.0; credit SARIT. The Sūtrasthāna in it is based on the revised 2nd edition, ed. Yādavaśarman Trivikramātmaja Ācārya (Bombay: Pāṇḍurang Jāvaji, 1931), commentary omitted. The e-text is in IAST; the Devanagari on the cards is converted from it.

The word split, Hindi, English, explanations, diagrams and questions are AI-written and AI-reviewed. They have not yet been checked by a Sanskrit scholar; doubtful readings are marked on the cards.
