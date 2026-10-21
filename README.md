# AI Resume Analyzer

An AI-powered resume analyzer that evaluates a resume against a job
description using NLP, calculates a match score, identifies missing skills and
generates personalised ATS-compatibility recommendations. Built with Python,
Streamlit and Scikit-learn.

## Features

- **Multi-format resume parsing** - upload a PDF, DOCX or TXT resume
- **NLP skill extraction** - identifies technical and soft skills from a
  curated database of more than 130 skills, with an alias table so that
  "Amazon Web Services" and "AWS" count as the same skill
- **Match scoring** - TF-IDF vectorisation with cosine similarity, reported
  as a 0-100 percentage
- **Skill gap analysis** - matched and missing skills shown side by side
- **Personalised recommendations** - actionable tips based on the score, the
  missing skills, the wording of the resume and its length
- **ATS compatibility check** - flags the formatting issues that trip up
  Applicant Tracking Systems
- **Downloadable report** - export the whole analysis as a text file

## Quick start (Windows)

Double-click **`run.bat`**. It creates a virtual environment, installs every
dependency and starts the app on <http://localhost:8501>.

## Quick start (macOS and Linux)

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
streamlit run app.py
```

## Project structure

```
ai-resume-analyzer/
├── app.py                    # Streamlit entry point
├── run.bat                   # One-click setup and launcher (Windows)
├── requirements.txt
├── resume_analyzer/          # The application package
│   ├── config.py             # Shared thresholds and limits
│   ├── core/                 # Pure analysis logic
│   │   ├── scoring.py        #   TF-IDF and cosine similarity
│   │   ├── skill_gap.py      #   Matched and missing skills
│   │   ├── recommendations.py #   Score and skill-gap advice
│   │   ├── style_advice.py   #   Wording, impact and length advice
│   │   ├── ats_check.py      #   ATS compatibility heuristics
│   │   └── pipeline.py       #   End-to-end analysis
│   ├── parsers/              # Text extraction
│   │   ├── factory.py        #   Format dispatch
│   │   ├── pdf_reader.py     #   PDF
│   │   ├── docx_reader.py    #   DOCX
│   │   └── text_reader.py    #   TXT
│   ├── skills/               # Skill detection
│   │   ├── database.py       #   Curated skill database
│   │   ├── aliases.py        #   Alternative spellings
│   │   └── extractor.py      #   Matching algorithm
│   └── ui/                   # Streamlit rendering
│       ├── header.py         #   Title and sidebar
│       ├── inputs.py         #   Upload and job description
│       ├── styles.py         #   Custom CSS
│       ├── score_view.py     #   Score card and chart
│       ├── skill_view.py     #   Skill pills
│       ├── results.py        #   Results composition
│       └── report.py         #   Downloadable report
├── scripts/                  # Development tooling
│   ├── check_loc.py          #   50 code-line budget check
│   ├── smoke_test.py         #   End-to-end check
│   ├── fixtures.py           #   Sample resume and job description
│   └── pdf_fixture.py        #   Sample PDF resume
└── docs/                     # One page per source file
```

Every source file is limited to **50 code lines**, so each module has one
clear job. Run `python scripts/check_loc.py` to verify it.

## How to use it

1. **Upload your resume** (PDF, DOCX or TXT).
2. **Paste the job description** you are targeting.
3. Click **Analyze Resume**.
4. Review your:
   - overall match score (0-100 %)
   - skill coverage chart
   - matched versus missing skills
   - personalised recommendations
   - ATS formatting warnings
5. Optionally download the full analysis as a text report.

## How the match score works

Both documents are vectorised with **TF-IDF**, which weighs a word by how
often it appears in one document against how often it appears in the other,
and are then compared with **cosine similarity**. The result is a 0-100 %
score reflecting how closely the wording of the resume matches the wording of
the posting. Multi-word skills are handled separately by the skill matcher,
which knows the real equivalences - "Amazon Web Services" and "AWS" count as
the same skill.

## Extending the skill database

The skill list lives in `resume_analyzer/skills/database.py` as `SKILL_DB`.
Add a canonical name and the matcher picks it up immediately. If the same
skill is commonly written in another way, add that spelling to
`resume_analyzer/skills/aliases.md` so it resolves to the same canonical
name.

## Checks

```bash
python scripts/check_loc.py    # every file within the 50 code-line budget
python scripts/smoke_test.py   # extraction, skills, pipeline, report, budget
```

## Documentation

Every source file has its own page under [`docs/`](docs/README.md), which
explains what the file does, what it exposes and which other files it works
with. [`docs/AUDIT.md`](docs/AUDIT.md) records the review of the previous
code base and what changed.

## Notes and limitations

- Scanned or image-based PDFs produce no text - use a text-based PDF or a
  DOCX file.
- The skill database is curated and cannot cover every skill. Extend it as
  needed.
- The ATS checks are heuristics over extracted text. They cannot detect
  visual problems such as multi-column layouts, embedded graphics or exotic
  fonts.
- The score measures vocabulary overlap, not seniority or relevance.
- The app has no authentication. Do not expose it publicly as it is.

## Potential next steps

- Replace the curated skill list with a spaCy or NLTK based extractor for
  broader coverage
- Compare fit across several job descriptions at once
- Suggest rewritten bullet points
- Keep a local history of past analyses
