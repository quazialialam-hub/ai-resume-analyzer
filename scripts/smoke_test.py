"""
End-to-end smoke test for the AI Resume Analyzer.

Builds a resume in every supported format, runs it through the real
extraction and analysis code and checks the results.

    python scripts/smoke_test.py

Exits with status 0 when every check passes and 1 otherwise.
"""

import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from check_loc import main as check_loc_main
from fixtures import JOB, RESUME, write_docx
from pdf_fixture import write_pdf
from resume_analyzer.core.pipeline import run_analysis
from resume_analyzer.parsers.factory import extract_text
from resume_analyzer.skills.extractor import extract_skills
from resume_analyzer.ui.report import build_report

FAILURES = []


def check(label: str, condition: bool, detail: str = "") -> None:
    """Record the outcome of a single check."""
    status = "PASS" if condition else "FAIL"
    print(f"[{status}] {label}" + (f" -> {detail}" if detail and not condition else ""))
    if not condition:
        FAILURES.append(label)


def raises_value_error(func, *args) -> bool:
    """Return True when the call fails with a ValueError."""
    try:
        func(*args)
    except ValueError:
        return True
    return False


def main() -> int:
    """Run every check and return the process exit code."""
    with tempfile.TemporaryDirectory() as name:
        directory = Path(name)
        text_file = directory / "resume.txt"
        text_file.write_text(RESUME, encoding="utf-8")
        files = (text_file, write_docx(directory), write_pdf(directory, RESUME))
        for path in files:
            text = extract_text(path.read_bytes(), path.name)
            check(f"extract {path.suffix}", "Jane Doe" in text and "AWS" in text)
        check("unsupported format raises", raises_value_error(extract_text, b"data", "a.rtf"))
        check("empty file raises", raises_value_error(extract_text, b"", "a.txt"))

    skills = extract_skills(RESUME)
    check("skills found", {"python", "sql", "aws", "docker", "postgresql"} <= skills, str(skills))
    check("ambiguous 'go' ignored", "go" not in extract_skills("We must go to market and own it"))
    check("alias resolves", "aws" in extract_skills("Experience with Amazon Web Services"))

    analysis = run_analysis(RESUME, JOB)
    check("score in range", 0 <= analysis.match_score <= 100, str(analysis.match_score))
    check("matched skills", "python" in analysis.matched_skills, str(analysis.matched_skills))
    check("missing skills", "airflow" in analysis.missing_skills, str(analysis.missing_skills))
    check("recommendations", len(analysis.recommendations) > 0)
    report = build_report(analysis)
    check("report has score", f"{analysis.match_score:.0f}%" in report)
    check("code line budget", check_loc_main() == 0)
    print(f"\n{len(FAILURES)} failure(s)")
    return 1 if FAILURES else 0


if __name__ == "__main__":
    sys.exit(main())
