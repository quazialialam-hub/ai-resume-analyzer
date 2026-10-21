# Source Code Audit

Audit of the project before the v2 restructure, with the outcome of every
finding. The previous layout was four flat modules in the project root:

| Old file | Lines | Responsibility |
| --- | --- | --- |
| `app.py` | 211 | Streamlit UI, input handling, business logic and report building |
| `analyzer.py` | 131 | Scoring, skill gaps, recommendations, ATS checks |
| `skill_extractor.py` | 82 | Skill database and matching |
| `resume_parser.py` | 59 | PDF / DOCX / TXT text extraction |

---

## 1. Project structure

1. **No package boundary.** Every module sat in the project root and was
   imported flat (`from analyzer import ...`). The application could not be
   reused as a library, and importing any module pulled in Streamlit.
   *Fixed* - the code now lives in the `resume_analyzer` package, split into
   `core` (pure logic), `parsers`, `skills` and `ui`.

2. **`.devcontainer/` was dead weight.** It configured a Codespaces container
   that installed Streamlit with `pip3 install --user` and started `app.py` at
   the repository root. It referenced paths that no longer exist and the
   project now ships its own launcher.
   *Fixed* - removed, and replaced by `run.bat` (one-click setup and launch).

3. **`app.py` was a 211-line script.** Page chrome, input handling, analysis
   calls and report generation were all in one top-level file.
   *Fixed* - `app.py` is now a 22-line entry point; the UI is in
   `resume_analyzer/ui/`.

4. **No per-file documentation.** Nothing explained what any individual file
   was responsible for.
   *Fixed* - every source file has a matching page under `docs/`.

## 2. Dead code and unused imports

5. **`app.py` imported `re`, `io`, `TfidfVectorizer` and `cosine_similarity`**,
   none of which it used. The TF-IDF work happened in `analyzer.py`, so the
   app paid the import cost of Scikit-learn twice over conceptually.
   *Fixed* - the app imports only what it calls.

6. **`resume_parser.py` imported `io`** and never used it.
   *Fixed* - removed.

7. **`pandas` was used for one two-row DataFrame** that fed `st.bar_chart`
   for the skill coverage chart.
   *Fixed* - `st.bar_chart` accepts a plain dictionary, so `pandas` was
   dropped from `requirements.txt` (about 60 MB of install weight, including
   NumPy).

## 3. Correctness

8. **The ATS check flagged every non-ASCII character.** The rule
   `re.search(r"[^\x00-\x7F]", resume_text)` reported a warning for em
   dashes, curly quotes, accented names and any typographic character - so
   nearly every modern resume produced a false positive.
   *Fixed* - only genuinely risky glyphs are flagged now (bullet characters,
   tick marks, em/en dashes, non-breaking spaces, trademark symbols).

9. **The TF-IDF model is unigram-only.** A phrase such as "machine learning"
   is scored as two unrelated words.
   *Measured and left as it is* - switching the vectoriser to unigrams plus
   bigrams was tried and made the score consistently **lower**, by about ten
   points on a realistic resume, because the extra phrase dimensions do not
   match and cosine similarity divides by the length of both vectors. Phrase
   matching is handled where it belongs instead: the skill extractor knows
   the real equivalences ("Amazon Web Services" is "aws") and reports matched
   skills separately.

10. **Short skill names matched ordinary English.** Because the text was
    lower-cased before matching, "go" (the Go language) matched "go to
    market" and "r" matched "R&D".
    *Fixed* - `go` and `r` are matched against the original text and only in
    their canonical form ("Go" and "R"), and the rule is documented in
    `skills/database.py`.

11. **The same skill could be counted twice.** The database held
    "sklearn" and "scikit-learn", "nodejs" and "node.js", "golang" and "go",
    so the matched and missing counts were inflated.
    *Fixed* - `skills/aliases.py` maps every alternative spelling onto one
    canonical name, and the extractor only ever returns canonical names.

12. **The score thresholds were hard-coded twice** - in the recommendation
    logic and again in the UI for the colour of the score.
    *Fixed* - both now read `SCORE_WEAK` and `SCORE_STRONG` from
    `resume_analyzer/config.py`.

13. **The match score was computed more than once per analysis.**
    *Fixed* - the pipeline computes it once and passes it to every consumer.

## 4. Robustness

14. **No upload size limit.** A very large PDF could stall the server.
    *Fixed* - uploads are capped at 10 MB with a clear message.

15. **The parsers were coupled to the Streamlit `UploadedFile` object**
    (`seek`, `.name`, `.read`), so they could not be reused or tested
    without a Streamlit runtime.
    *Fixed* - every reader works on raw bytes plus a file name.

16. **Decode errors were silent.** The TXT reader used
    `decode("utf-8", errors="ignore")`, which quietly dropped characters.
    *Fixed* - encodings are tried in order and a lossy decode is the explicit
    last resort.

17. **`PyPDF2` is unmaintained.** Its last release (3.0.1) was in 2022.
    *Fixed* - replaced with its actively maintained successor `pypdf`.

18. **Parse errors surfaced as raw exceptions** inside the sidebar.
    *Fixed* - the upload is read in a guarded helper and failures are shown
    inline as a readable message.

## 5. Performance

19. **The resume was re-parsed on every Streamlit re-run.** Streamlit
    re-executes the whole script on any interaction, so the PDF was decoded
    again each time the user typed in the job-description box.
    *Fixed* - parsing is cached with `st.cache_data`, keyed on the file
    bytes, so a resume is decoded once.

20. **Around 130 regular expressions were recompiled on every call** to
    `extract_skills`, and the function was called twice per analysis.
    *Fixed* - patterns are compiled once into a module-level cache.

21. **Multi-word skills relied on a sort order** to be matched before their
    substrings.
    *Fixed* - the boundary-aware matcher makes the ordering irrelevant.

## 6. Known limitations (left as they are, on purpose)

- Scanned or image-based PDFs still yield no text. OCR is out of scope.
- The ATS checks are heuristics over extracted text. Visual problems -
  multi-column layouts, embedded graphics, exotic fonts - cannot be detected
  from plain text at all.
- The skill database is curated. It cannot cover every skill, and the alias
  table only handles the common alternative spellings.
- The score measures vocabulary overlap, not seniority or relevance. Two
  resumes with identical wording score identically, however different the
  candidates are.
- `streamlit run app.py` exposes the app without authentication. Do not
  deploy it publicly as-is.

## 7. Verification

- `python scripts/check_loc.py` - every source file is within the
  50 code-line budget.
- `python scripts/smoke_test.py` - end-to-end check of the whole pipeline
  with a TXT, DOCX and PDF resume.
