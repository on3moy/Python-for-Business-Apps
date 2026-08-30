# Authoring Style Guide — IS 640 Business Application Programming

How lesson pages in `docs/notes/` are written. Derived from a full read of all 17 CH1–CH3 files. Follow this when adding a new chapter or section so new pages are indistinguishable from existing ones.

Author: Moy Patel (`on3moy`). Site: <https://on3moy.github.io/Python-for-Business-Apps/>

---

## 1. Document skeleton

**There is no boilerplate.** No front matter, no learning objectives, no "By the end of this section…", no summary, no key takeaways, no exercises. The page starts with the H1 and it just *stops* when the content runs out. Do not add a conclusion.

```
# <Title>                      <- exactly one H1, line 1
<optional Giphy <img> line>
<optional one-line conversational hook>
**term:**
Definition sentence.
## <Section>                   <- H2s, topic-named, unnumbered
### <Subsection>               <- H3, rare
```

- Chapter pages are **one topic per file**, with 1–5 unnumbered H2s. Chapter 1 was originally a single long survey page and has since been split to match.
- Bare `---` separators are rare — `2.8-module-basics.md` is the main user.
- H2 phrasing is casual — verbs and questions, not noun-phrase headings:
  `## Adding stuff into a dictionary`, `## Deleting stuff`, `## How do we pull items from the dictionary` (no question mark), `## Modify the lists`, `## Formatting Floats`, `## Sequence type functions`.
- **Nearly every line ends with two trailing spaces.** This is a hard line break and it is load-bearing — the `**term:**` / definition pairs render wrong without it.

## 2. Voice and tone

Second person ("you"), plus first-person-plural "Lets/Let's" as the teacher walking alongside the student. Conversational, jokey, emoji-laden, with occasional personal anecdote and self-deprecation. Business / data-analytics framing is constant — salary, taxes, Excel, pandas, Databricks, APIs, reports.

The author writes **"Lets"** without the apostrophe roughly as often as "Let's". Typos and informal grammar ("its" for "it's") are left in. Don't over-correct into formal prose — it stops sounding like him.

Representative sentences:

> It's not ideal to work with long float formats. You are hurting the eyes of your veteran peers.

> Dictionaries are versatile and highly used in my data analytics experience! Get to know how to use dictionaries!

> When I learned Python, dictionaries were not able to store data in an ordered format. Meaning, the order in which you stored data would move around 🥲.

> YES! We all do and its okay. We do not have to be a perfectionist when we start typing.

> To display any outputs, when you run code in automation, you don't need to see outputs for everything. Unless you want to be a rebel.

> Best shown by example…

**Emoji in active use:** 🦖 (mascot — appears in every `??? example` title) ✅ ❌ ⚠️ 🤯 🥲 😓 👉 ⬅️ ➡️ 🌕 🌑 📖

**Analogy sources:** Excel (SUM/COUNT as built-ins, macros as stored instructions, a list as "similar to a column in excel"), telephone operators, reading a book, Harry Potter.

## 3. Code conventions

- **Bare triple-backtick fences. Zero language tags.** Highlighting is left to `codehilite` guessing. Match this. (Slides are the deliberate exception — decks tag the language so Marp applies its syntax theme. See `SLIDE_STYLE_GUIDE.md` §5.)
- **No `hl_lines`, no `linenums`, no `title=`** on any fence, even though `pymdownx.highlight` is enabled with `anchor_linenums`.
- **No `>>>` REPL style** anywhere.
- **3–8 lines typical**, ~12 max. No function or class definitions. Single-quoted strings, always.
- **Comments carry the teaching** — first-person-plural imperative, one per step, sometimes asking the reader a rhetorical question:

```
# Lets show the value
print(x)

# Lets show the type
print(type(x))
```

```
# The old way of formatting using {} and format method
print('Hi my name is {}. {} is my favorite color'.format(student, color))

# The new way, use this. You can see its more intuitive and easy to follow
print(f'Hi my name is {student}. {color} is my favorite color')

# Did you notice the only way to bring in data into a string is by using {}?
```

**Showing output** — three accepted forms:

1. Inline labels (dominant, for one-liners):
   ```
   Input:
   `5 // 3`
   Output:
   `1`
   ```
2. A second bare fence after the code fence, optionally preceded by `Output:`.
3. Trailing inline: ``Output of x: `[1, 2, 3, 4]` ``

**Naming:** working default is `lower_snake_case` (`down_payment`, `num_months`, `sqrt_num`, `my_string`, `list_a`). Constants shout: `SALARY = 80000`. Playful throwaway names are welcome and used freely: `beans`, `wowmom`, `ImBabyTRex`, `hey_you`, `itDoesntMatterWhatYouCallMe`. Naming is *deliberately* mixed on the naming-conventions pages to model good vs bad.

## 4. Admonitions — the semantic contract

Frequency across CH1–CH3: `??? example` ×15, `??? question` ×11, `!!! note` ×8, `!!! info` ×7, `!!! quote` ×6, `!!! abstract` ×6, `??? info` ×5, `!!! example` ×4, `!!! warning` ×2, `!!! tip` ×2, `??? tip` ×1, `!!! question` ×1.

**Never used:** `!!!+` / `???+` (open-by-default), `!!! danger`, `!!! bug`, `!!! success`, `!!! failure`. Content is indented 4 spaces. `???` = collapsed/optional depth, `!!!` = inline callout.

| Admonition | Used for | Typical title |
|-|-|-|
| `??? example` | The workhorse — a collapsed hands-on demo | `"🦖 Example"` (almost always literally this) |
| `??? question` | An anticipated student question, answered inside — the signature device | the literal question |
| `!!! quote` | Verbatim textbook definition, attributed | `"Zybooks"` / `"Zybooks Glossary"` |
| `!!! abstract` | Introduces a callable/utility | the function name, e.g. `"float()"`, `"pop()"` |
| `!!! info` | Untitled aside or metaphor box | often `" "` (a single space) |
| `!!! note` | A correction, refinement, or aside | `"Note"`, `"Fun Fact"` |
| `!!! warning` | Gotchas only | `"Do not confuse yourself with sets"` |
| `!!! tip` | Practical rule or recap | `"Reserved Words"`, `"To Summarize"` |

Examples to copy verbatim in shape:

```
??? example "🦖 Example"  

    Let's use `'wowmom'` as an example. 

    Grab the first letter
    `'wowmom'[0]`    
```

```
!!! quote "Zybooks"  

    **expression:** 
    is a combination of items, like variables, literals, operators, and parentheses, that evaluates to a value, like 2 * (x + 1).  
```

```
!!! abstract "float()"   

    You can use the **float()** function to convert your value into a float if possible.  
    - You can't convert 'Hi' into a decimal.  
```

Real `??? question` titles in use, for calibration of tone:
`"Variables - Why is this is awesome!?"` · `"Why print()?"` · `"What is an Escape Sequence?"` · `"How do you know if its a function?"` · `"How can we know which words not to use?"` · `"Do you struggle with attention to details at times?"` · `"What is whitespace?"`

**Nesting is used** — `??? question` inside `!!! warning`, `!!! info` inside `??? question`, H3 headings inside a `??? question`.

## 5. Annotations, tables, marks

**Annotations are the most distinctive feature here.** Pattern is `(1)` marker → `{ .annotate }` line → numbered list:

```
Input:
`5 % 3`(1)  
Output:
`2`  
{ .annotate }

1. 5 / 3 approximately is 1 with a remainder of 2, so we get the remainder 2.  
```

```
- Python is **open-source**(1)  
    { .annotate }  

    1. The community (even you) can participate in defining the language and creating new interpreters.  
```

**Tables** — pipe tables with a bare `|-|-|` separator row and trailing double-spaces per row. Used for operator references, error types, escape sequences, function catalogs. Sometimes 4-column paired layout (`|Function|Description|Function|Description|`).

**Right/wrong marks** — a characteristic device, applied to inline code:

```
x = 13 ✅
JohnDoe = 55 ✅  
`5 = x` ❌  
- mixedCase ... ⚠️ (Try not to use, unless its already common within scripts)
- Capitalized_Words_With_Underscores (ugly!) ❌ ❌ ❌   
```

**Task lists** are used metaphorically, not as checklists:

```
- [x] On 🌕 or True or 1
- [ ] Off 🌑 or False or 0
```

**Tabs (`===`) are never used**, despite `pymdownx.tabbed` being enabled.

## 6. Images and media

- **Mood-setter GIFs**: raw HTML `<img>` with a remote Giphy URL, unquoted `width`, no alt text, placed under the H1 or at the top of a section. ~15 occurrences.
  ```
  <img src='https://i.giphy.com/media/.../giphy.gif' width=200/>  
  ```
  `width=200` is the default; `300` occasionally. Quoting and spacing are sloppy in the originals — no need to reproduce the sloppiness, but don't add alt text where the house style has none.
- **Local screenshots**: Markdown syntax, relative `../../img/ChapterN/` path, optional title-as-caption.
  ```
  ![PythonInterpreter](../../img/Chapter1/PythonInterpreter.png "This screenshot is using python interpreter within the CMD")
  ```
  Images live in `docs/img/Chapter1/`, `docs/img/Chapter2/`, …
- **Textbook diagrams** are hotlinked from `zytools.zybooks.com`.
- **No iframes, no video embeds** in lesson pages. YouTube appears as a bare autolinked URL inside a `??? tip` with a `(Ctrl + Click to open in new tab)` instruction.

## 7. Pedagogical pattern

The dominant unit is **term → definition → admonition → code → output**.

Concept introduction is **definition-first, glossary-style**: bold term, colon, hard line break, one-sentence definition (usually paraphrased from Zybooks):

```
**string:**
A string is a sequence of characters, like the text MARY, that can be stored in a variable.  
```

Then an admonition that translates it into practice or a joke, then optionally a code fence.

- **No "Try it yourself", no numbered practice problems, no quizzes.** The closest thing is an imperative invitation inside prose: "You can copy and past below to get all characters from numbers 32-127.", "Convert these character back to numbers using ord()!!!"
- **Gotchas** go in `!!! warning`, `??? question`, or ✅/❌ marked inline code.
- **Emphasis:** `**bold**` for defined terms and function names in prose (`**float()**`); `` `inline code` `` for identifiers, operators, short expressions and outputs; *italics* is rare (pseudo-captions above fences).
- **Cross-references are relative markdown links.** This reverses the original rule — students arrive at a single note from search and need a way onward, so a note that mentions a topic covered elsewhere should link there.
    - Syntax is `[display text](relative/path.md)` — `[module basics](2.8-module-basics.md)` within a chapter, `[objects](../ch02/2.3-objects.md)` across chapters. The display text is the words already in the sentence — you wrap existing prose, you don't rewrite it to accommodate a link.
    - `mkdocs build --strict` fails on a broken link, so the build is the check.
    - **Link a target at most once per page, on first mention.** Repeat links just clutter the prose.
    - 2–4 inline links per page is the working range. Short pages may warrant one, or none. Don't force them.
    - Never place a wikilink inside a code fence, inside inline backticks, or in a heading.
    - Voice comes first. If a link can't be worked in without breaking the conversational tone, leave it out.
- **External links are frequent** and almost always PEP 8 or official docs.
- **"Why this matters" boxes** tie a topic to a real job — e.g. `??? info "Use cases"` in 3.4 lists JSON/API/IoT/legacy scenarios and closes with "All this to say, dictionaries are your go to for working with pandas, spark tables, and anything database related."

## 8. Files, naming, nav

- **No front matter.** The file starts at the H1, which supplies the page title. There is no `title:`, no `tags:`, no dates or status fields — see §1.
- Filename: `<chapter>.<section>-kebab-case-title.md` — `2.1-variable-assignments.md`, `3.10-string-formatting.md`. Chapter dirs are `docs/notes/ch01`, `ch02`, `ch03` (lowercase, zero-padded so they sort). Each chapter dir has an `index.md` hub.
- **Every chapter has an `index.md` Map of Content** — a sentence or two of intro in voice, then one bullet per section in order, each a wikilink plus one short clause. No summary at the end. This is the chapter's landing page under `navigation.indexes`.
- **H1 vs filename is inconsistent** and both are acceptable — about half carry the section number (`# 2.1 Variables and assignments`), half don't (`# Objects`, `# String Basics`). The H1 text also need not match the filename exactly.
- H1 lines usually carry trailing whitespace.
- **Every new page must be registered manually** in `nav:` in `mkdocs.yml`. The nav label always carries the number: `- 3.10 String Formatting: 'notes/ch03/3.10-string-formatting.md'`.
- Nav indentation: `nav:` children at 2 spaces, `Notes:` children at 4, chapter section entries at 6. Paths are single-quoted. The bare `'notes/chNN/index.md'` entry must come first inside each chapter — that is what makes it the section landing page under `navigation.indexes`.
- Section numbering may skip — CH3 jumps 3.4 → 3.10. Chapters get built out incrementally; only write the sections you actually cover.

## 9. Length and density

- **Typical CH2/CH3 page: ~210–460 words**, 1.5–5 KB, 2–5 H2s, 1–4 code fences, 2–4 admonitions, 0–1 GIF, 0–1 table.
- Median ~250 words. Shortest is `2.7-division-modulo.md` at 127 words with zero code fences (all inline `Input:`/`Output:` pairs).
- Longest subsections: `2.8-module-basics.md` (774 words), `3.2-list-basics.md` (580).

Err short. These are lecture companions, not a textbook — the zyBook already is the textbook.

---

## Checklist for a new page

1. Start at `# <Title>` on line 1 — no front matter.
2. Optional Giphy `<img src='…' width=200/>` right under the H1.
3. One-line conversational hook, or go straight to `**term:**` / definition pairs.
4. H2s named after the actual thing being done, casual verb phrasing, unnumbered.
5. Code fences: bare ` ``` `, no language tag, 3–8 lines, `# Lets …` comments narrating each step, single-quoted strings, snake_case.
6. Outputs as `Output:` + inline code, or a second bare fence.
7. Sprinkle `??? example "🦖 Example"`, `??? question "<a real student question>"`, `!!! quote "Zybooks"` for textbook definitions, `!!! abstract "someFunc()"` for callables, `!!! warning` for gotchas.
8. `(1)` + `{ .annotate }` + numbered list for footnotes.
9. Pipe tables for reference material; `✅ ❌ ⚠️` on right/wrong inline snippets.
10. Two trailing spaces at the end of nearly every line.
11. Tie it to a business / data-analytics scenario at least once.
12. **No summary, no exercises, no learning objectives — just stop.**
13. 2–4 inline `[display text](relative/path.md)` links, each target linked once, on first mention. **No "See also" footer** — pages end when the content ends.
14. Add the page to the chapter's `index.md` hub.
15. Register the page in `nav:` in `mkdocs.yml`.
