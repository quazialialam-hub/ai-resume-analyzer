# `scripts/fixtures.py`

**Path:** `scripts/fixtures.py`
**Purpose:** The sample resume and job description used by the smoke test.

## What it does

Provides the text the smoke test analyses, plus a builder for the DOCX
version of the same resume.

| Name | Kind | Description |
| --- | --- | --- |
| `RESUME_LINES` | constant | The resume, one line per entry |
| `RESUME` | constant | The resume as a single string |
| `JOB` | constant | The job description as a single string |
| `write_docx(directory)` | function | Writes the resume as a DOCX file |

## The sample content

The resume deliberately contains everything the checks look for:

- a name and an e-mail address, so the ATS contact check passes
- the section headers "Skills" and "Experience"
- the skills Python, SQL, AWS, Docker and PostgreSQL
- a quantified achievement ("30%", "15%"), so the quantification check
  passes
- a table in the DOCX version, so the table extraction path is exercised

The job description asks for Python, SQL, AWS, Airflow, Docker, Kubernetes
and PostgreSQL, which gives both matching and missing skills.

## Notes

- The DOCX file is written with `python-docx`, which is already a dependency
  of the project.
- The PDF version of the same resume is built by `scripts/pdf_fixture.py`.
