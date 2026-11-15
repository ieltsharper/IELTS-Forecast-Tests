# Forecast CB tests: how to type up a test

Source: the books "IELTS Reading Computer 2025 Vol 1" and "IELTS Listening Computer 2025 Vol 1" (Naugh Milk IELTS),
10 tests each, **scanned (image only)**, plus their answer books. One authoring file per test and skill:

- Reading: `src/reading/test-N.json` (3 passages, questions 1-40, answer key, answer-book notes)
- Listening: `src/listening/test-N.json` (4 sections, questions 1-40, answer key, transcript)

Do not touch other tests' files, `data/`, `assets/` or anything else outside your own file(s) and your own `img/` crops.

## Source material (all pages are pictures; OCR is only a draft)

- Page pictures, 200 dpi (1653x2339), PNG: `D:/HarperSites/_scratch/forecast-cb/<tag>/pNNN.png`, NNN = PDF page number:
  `rq` = Reading question book, `ra` = Reading answer book, `lq` = Listening question book, `la` = Listening answer book + transcript.
- OCR draft text: `python -X utf8 -I D:/HarperSites/IELTS-Forecast-Tests/_generator/ocr_draft.py <tag> FIRST LAST`
  (watermark/footer lines removed). It has many small errors, DROPS words, scrambles columns, tables and the key. **Look at every
  page picture** (Read tool on the PNG) and compare line by line.
- Page map (PDF pages):

| Test | Reading questions `rq` | Reading answers `ra` (key table first, then explanations) | Listening questions `lq` | Listening answers `la`: key page, then transcript |
|---|---|---|---|---|
| 1 | P1 3-6, P2 7-10, P3 11-14 | 3-11 | 3-9 | key 3, transcript 4-14 |
| 2 | P1 15-17, P2 18-20, P3 21-24 | 12-20 | 10-15 | key 15, transcript 16-26 |
| 3 | P1 25-27, P2 28-31, P3 32-36 | 21-29 | 16-22 | key 27, transcript 28-38 |
| 4 | P1 37-40, P2 41-44, P3 45-48 | 30-37 | 23-27 | key 39, transcript 40-52 |
| 5 | P1 49-52, P2 53-55, P3 56-59 | 38-43 | 28-33 | key 53, transcript 54-66 |
| 6 | P1 60-62, P2 63-66, P3 67-70 | 44-53 | 34-39 | key 67, transcript 68-78 |
| 7 | P1 71-73, P2 74-77, P3 78-81 | 54-63 | 40-45 | key 79, transcript 80-87 |
| 8 | P1 82-84, P2 85-88, P3 89-92 | 64-73 | 46-50 | key 88, transcript 89-101 |
| 9 | P1 93-97, P2 98-102, P3 103-106 | 74-80 | 51-55 | key 102, transcript 103-114 |
| 10 | P1 107-109, P2 110-112, P3 113-115 | 81-88 | 56-60 | key 115, transcript 116-128 |

  (Pages 1-2 of each book are the cover and contents; the contents list every passage / section title.)
  The first page of a test in `ra`/`la` is the answer-key table: **read the key from the PICTURE** (the OCR scrambles it).

## Faithfulness rules (the owner's rules)

1. Keep the book's own wording, spelling and (British) style, even odd phrasing or typos. Do not correct, paraphrase, shorten or
   explain. Where the book looks wrong (answer not among the options, a number missing, a key that does not fit the question),
   keep it and list it in your report.
2. Fix OCR mistakes (`thcorics` → `theories`, `l` for `I`, `rn` for `m`, `11m` for `I'm`), restore words the OCR dropped (check the
   first word of paragraphs: drop caps are often lost), italics (`*Odyssey*`), paragraph breaks, headings, numbers/dates exactly as
   printed. Join words hyphenated only by line breaks (`magnet-` / `ism` → `magnetism`); keep real hyphens.
3. Typographic quotes as printed: ’ for the apostrophe, “ ” for double quotes.
4. Drop only: the "NAUGH MILK IELTS / Contact Zalo" watermark, the footer ("Naugh Milk Ielts 078.426.7174", British Council / IELTS logos)
   and page numbers; and in Reading the corner labels "TEST N" / "READING PASSAGE N" (the builder writes its own).
5. Question numbers must be exactly 1-40 across the test (Reading: usually 1-13, 14-26, 27-40; Listening: 1-10, 11-20, 21-30, 31-40).
6. Answers come from the key page (read the picture). `True/False/Not Given` and `Yes/No/Not Given` are normalised to capitals by the
   converter. Keep the key's spelling. Alternatives in the key (`/`, `or`, brackets like `(the) water`) are given as a list (first = the
   one displayed): `["2000 floods", "2000 flooding"]`; a single answer that happens to contain a comma stays one string.
   An optional word is written `"(the) water supply"`. Do NOT invent extra accepted answers; report suspected ones instead.
7. A map / plan / diagram / picture that cannot be typed is cut from the page with
   `python -X utf8 -I _generator/crop.py <tag> PAGE x0 y0 x1 y1 t3-p2-map` (fractions 0-1 of the page; look at the result in `img/`
   with the Read tool and adjust until the whole picture and nothing else (no watermark-only margins) is in). Show it with
   `[[img:t3-p2-map]]` as its own paragraph (in `intro` for a labelling group, or inside `content`). Tables, notes, forms and
   flow-charts MUST be typed, not pictures (flow-chart: one paragraph per box in reading order, a `↓` paragraph between boxes).
   Name crops `t<test>-...` so tests never clash.

8. **Scan junk.** The Reading scans carry stray junk tokens inside the text (e.g. "ede", "atego", "bremaining", "bine al", "You" in the
   middle of a sentence, or a few letters glued to a word). They are not the book's words: remove them and keep the real word, as the key
   and the answer book show it (Test 1: "collects chemicals", not "bine alchemicals"). Mention each one in your report.
9. If the key disagrees with the printed question or passage (otherwise), keep both as printed and list it in your report.
10. Quotes: ’ for apostrophes everywhere (questions, passages, notes). For quotation marks use “ ” where the picture shows double quotes
    and ‘ ’ where it shows single quotes (British books often print 'like this'). In the Listening transcript follow the machine's
    straight apostrophes as ’ too (one rule: always typographic). Round "(laughs)" brackets stay as printed.
11. Word limit: put the printed limit line only in `intro` (verbatim) AND set `limit` for the marking; the builder shows it once.
12. A narrator turn that crosses a section boundary is split between the two sections (the "Now turn to Section N" part goes to the
    section that ends).
13. Two quotes in one note: join them with `” “` inside `quote`. `title` (optional) on a group overrides the "Questions a–b" heading.
14. Pages 7-14 of `rq` for Test 1 are 1700x2200, other books may differ: when cropping use fractions, not pixels.

## Reading file: `src/reading/test-N.json`

```json
{ "test": 1,
  "passages": [ { "n": 1, "title": "…", "head": ["optional line above the title"], "standfirst": "optional line under title",
                  "paragraphs": [ {"l": "A", "t": "text with *italic* **bold** __underline__"}, {"sub": "Section heading"}, "plain paragraph" ],
                  "footnotes": ["optional glossary line"],
                  "groups": [ … ] } ],
  "notes": { "1": {"quote": "…", "explanation": "…"} } }
```

`{"l": "A", …}` for lettered paragraphs/sections (also when the book prints "Section A"); plain strings when the passage has no letters.
Keep the subtitle/intro line under the title (e.g. "Drama student … took part in") as `standfirst`. If a box or picture sits inside the
passage text, crop it and describe it in your report.

`notes` (the answer book `ra`, per question, only where the book gives it): `quote` = the evidence text the book quotes (without the
outer quotation marks, in English, exactly as printed, "…" ellipses kept), `explanation` = the explanation text as printed (usually
Vietnamese, after "Giải thích:"; for some tests English, after "Explanation"/"Dẫn chứng"; keep every Vietnamese accent and tone mark
exactly; a list of strings = several paragraphs). Questions the book does not explain are simply left out. For a heading question the book
may give the heading and a paragraph analysis: put the analysis in `explanation`. For a "choose TWO/THREE letters" group, one note on the
group's first question number. Do not put the answer letter/word itself in `quote`.

## Listening file: `src/listening/test-N.json`

```json
{ "test": 1, "audio": "audio/test-01.mp3",
  "sections": [ { "n": 1, "title": "International Student Travel Agency Enquiry Form",
                  "context": ["optional printed lead-in line(s) above the questions, e.g. 'You will hear …'"],
                  "groups": [ … ],
                  "transcript": [ {"s": "Speaker 1", "t": "what this speaker said in one turn"}, "a line without a speaker" ] } ] }
```

Section titles are in the contents page (`lq` p2 / `la` p2-3) and on the key page. Group types are the same as for Reading (below);
Listening uses `gap` (form, notes, table, flow-chart, sentences), `mcq`, `multi`, `short`, `match` (match to a lettered list, "Choose six
answers from the box"), `grid` (map / plan labelling: letters only, picture in `intro`) and sometimes `bank`.

**Transcript** (`la` pages after the key): type the whole transcript of the section: every spoken word, one entry per speaker turn,
`"s"` = the speaker label as printed in the picture ("Speaker 2"; the narrator is whatever label the book gives). The machine
transcript prints `00:14:24,255 --> 00:14:35,675 [Speaker 6]` before each turn: drop the timestamps and arrows, keep the label.
Join the book's wrapped lines into one paragraph per turn. Spelling-out like "D-E-L-A-W-A double R" stays as printed. Divide the
transcript between the four sections by the narrator's announcements ("Now turn to Section 2", "That is the end of Section 1"); the
text before the first Section 1 announcement belongs to Section 1. Keep bracketed sounds like [laughs]. Do not "fix" the machine's
wrong words if they are what the book prints, but do fix OCR mistakes (`11m` is the OCR of `I'm`).

## Question groups (`groups`): always `"range": [first, last]` and `"intro": ["line", …]` (the printed instructions, verbatim, one string per paragraph)

| type | extra fields |
|---|---|
| `tfng` / `ynng` | `items: {"8": "statement"}`, `answers: {"8": "True"}` |
| `short` | `items: {"6": "question"}`, `limit: {"words": 2, "number": false}` (number true = "AND/OR A NUMBER"), `answers` |
| `mcq` | `items: {"14": {"stem": "…", "options": {"A": "…", "B": "…"}}}`, `answers: {"14": "C"}` |
| `multi` (choose two/three letters; range spans all its questions) | `choose: 3`, `stem`, `options: {"A": "…"}`, `answer: "C, D, E"` (no `answers`) |
| `headings` / `match` (options list shown) | `options: {"title": ["**List of Headings**"], "list": {"i": "…"}, "after": false}`, `items: {"1": "Paragraph **A**"}` (for `match`: the statement/person/business to match), `answers`. |
| `grid` (match to paragraph/map letters, no list) | `letters: ["A","B","C","D","E","F","G","H"]`, `items: {"27": "statement"}`, `answers` |
| `gap` (notes / summary / sentences / table / form / flow-chart with typed answers) | `content: [ … ]`, `limit`, `answers`; optional `after: [ … ]`, `pairs`, `unordered: [[21, 22]]` (two answers that may come in either order) |
| `bank` (fill gaps from a lettered word box) | `content`, `options: {"title": [..] or null, "list": {"A": "word"}}`, `answers: {"9": "C"}` |

`content` items: a string paragraph with gaps written `[[9]]` (second blank of the same question: `[[9:2]]`), `{"center": "Title line"}`,
`{"h": "Heading"}`, or a table `{"table": [["Header1","Header2"],["cell [[14]]","cell"]]}` (all cells are strings; an empty cell is `""`).
Sentence-completion lists: one string per sentence. Where the book puts the gap inline, put `[[n]]` in the same place and keep the words
around it exactly. The number of the question always appears as `[[n]]`, never as printed digits. Example answers printed in the book
("Example: …") stay as plain text, not a gap. Bullets: start the paragraph with "• ".

## Check your work

```
python -X utf8 -I _generator/build_data.py reading src/reading D:/HarperSites/_scratch/forecast-cb/check-reading-N.json N
python -X utf8 -I _generator/check_data.py D:/HarperSites/_scratch/forecast-cb/check-reading-N.json N
python -X utf8 -I _generator/build_data.py listening src/listening D:/HarperSites/_scratch/forecast-cb/check-listening-N.json N
python -X utf8 -I _generator/check_listening.py D:/HarperSites/_scratch/forecast-cb/check-listening-N.json N
```

(run from `D:/HarperSites/IELTS-Forecast-Tests`; the last two lines are for Listening). Done means: both scripts say OK, and every page
picture of your test was compared with your text (passage text, every question, the key table, the notes / transcript).
Write JSON with the Write tool (UTF-8, real characters, not \u escapes). Do not use Python heredocs to write text that contains
quotation marks or accents.
