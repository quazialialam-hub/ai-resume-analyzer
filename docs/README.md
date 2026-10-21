# Documentation Index

One page per source file, describing what the file does, what it exposes and
which other files it works with.

| File | Page | What it does |
| --- | --- | --- |
| `app.py` | [app.md](app.md) | Streamlit entry point that wires everything together |
| `run.bat` | [run.md](run.md) | One-click Windows setup and launcher |
| `requirements.txt` | [requirements.md](requirements.md) | Third-party dependencies |
| `resume_analyzer/config.py` | [config.md](config.md) | Shared thresholds and limits |
| `resume_analyzer/__init__.py` | [resume_analyzer.md](resume_analyzer.md) | Package root and version |
| `resume_analyzer/core/__init__.py` | [core/__init__.md](core/__init__.md) | Public API of the core package |
| `resume_analyzer/core/scoring.py` | [core/scoring.md](core/scoring.md) | TF-IDF and cosine similarity score |
| `resume_analyzer/core/skill_gap.py` | [core/skill_gap.md](core/skill_gap.md) | Matched and missing skill sets |
| `resume_analyzer/core/recommendations.py` | [core/recommendations.md](core/recommendations.md) | Score and skill-gap advice |
| `resume_analyzer/core/style_advice.py` | [core/style_advice.md](core/style_advice.md) | Wording, impact and length advice |
| `resume_analyzer/core/ats_check.py` | [core/ats_check.md](core/ats_check.md) | ATS compatibility heuristics |
| `resume_analyzer/core/pipeline.py` | [core/pipeline.md](core/pipeline.md) | End-to-end analysis pipeline |
| `resume_analyzer/parsers/__init__.py` | [parsers/__init__.md](parsers/__init__.md) | Public API of the parsers package |
| `resume_analyzer/parsers/factory.py` | [parsers/factory.md](parsers/factory.md) | Format dispatch |
| `resume_analyzer/parsers/pdf_reader.py` | [parsers/pdf_reader.md](parsers/pdf_reader.md) | PDF text extraction |
| `resume_analyzer/parsers/docx_reader.py` | [parsers/docx_reader.md](parsers/docx_reader.md) | DOCX text extraction |
| `resume_analyzer/parsers/text_reader.py` | [parsers/text_reader.md](parsers/text_reader.md) | TXT text extraction |
| `resume_analyzer/skills/__init__.py` | [skills/__init__.md](skills/__init__.md) | Public API of the skills package |
| `resume_analyzer/skills/database.py` | [skills/database.md](skills/database.md) | Curated skill database |
| `resume_analyzer/skills/aliases.md` | [skills/aliases.md](skills/aliases.md) | Alternative skill spellings |
| `resume_analyzer/skills/extractor.py` | [skills/extractor.md](skills/extractor.md) | Skill matching algorithm |
| `resume_analyzer/ui/__init__.py` | [ui/__init__.md](ui/__init__.md) | Public API of the UI package |
| `resume_analyzer/ui/header.py` | [ui/header.md](ui/header.md) | Page title and sidebar |
| `resume_analyzer/ui/inputs.py` | [ui/inputs.md](ui/inputs.md) | Upload and job description controls |
| `resume_analyzer/ui/styles.py` | [ui/styles.md](ui/styles.md) | Custom CSS |
| `resume_analyzer/ui/score_view.py` | [ui/score_view.md](ui/score_view.md) | Score card and coverage chart |
| `resume_analyzer/ui/skill_view.py` | [ui/skill_view.md](ui/skill_view.md) | Matched and missing skill pills |
| `resume_analyzer/ui/results.py` | [ui/results.md](ui/results.md) | Composition of the results view |
| `resume_analyzer/ui/report.py` | [ui/report.md](ui/report.md) | Downloadable text report |
| `scripts/check_loc.py` | [scripts/check_loc.md](scripts/check_loc.md) | 50 code-line budget check |
| `scripts/smoke_test.py` | [scripts/smoke_test.md](scripts/smoke_test.md) | End-to-end pipeline check |
| `scripts/fixtures.py` | [scripts/fixtures.md](scripts/fixtures.md) | Sample resume and job description |
| `scripts/pdf_fixture.py` | [scripts/pdf_fixture.md](scripts/pdf_fixture.md) | Sample PDF resume |

See [AUDIT.md](AUDIT.md) for the review of the previous code base and what
changed.
