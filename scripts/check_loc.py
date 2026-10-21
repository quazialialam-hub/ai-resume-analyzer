"""
Check that every source file stays within the 50 code-line budget.

A "code line" is any line that is not blank, not a comment and not part of a
docstring. Run it from the project root:

    python scripts/check_loc.py
"""

import ast
import pathlib
import sys

MAX_CODE_LINES = 50
ROOT = pathlib.Path(__file__).resolve().parent.parent


def _docstring_lines(tree: ast.AST) -> set:
    """Return the line numbers covered by module/class/function docstrings."""
    covered = set()
    for node in ast.walk(tree):
        if not isinstance(node, (ast.Module, ast.ClassDef, ast.FunctionDef, ast.AsyncFunctionDef)):
            continue
        body = getattr(node, "body", [])
        if not body:
            continue
        first = body[0]
        if isinstance(first, ast.Expr) and isinstance(first.value, ast.Constant):
            if isinstance(first.value.value, str):
                covered.update(range(first.lineno, (first.end_lineno or first.lineno) + 1))
    return covered


def count_code_lines(path: pathlib.Path) -> int:
    """Return the number of code lines in a Python file."""
    source = path.read_text(encoding="utf-8")
    tree = ast.parse(source)
    docstrings = _docstring_lines(tree)
    count = 0
    for number, line in enumerate(source.splitlines(), start=1):
        stripped = line.strip()
        if not stripped or stripped.startswith("#") or number in docstrings:
            continue
        count += 1
    return count


def main() -> int:
    """Check every Python file and report the ones over budget."""
    offenders = []
    for path in sorted(ROOT.rglob("*.py")):
        if any(part in {"venv", ".git", "__pycache__", ".freebuff"} for part in path.parts):
            continue
        lines = count_code_lines(path)
        relative = path.relative_to(ROOT).as_posix()
        status = "OK " if lines <= MAX_CODE_LINES else "OVER"
        print(f"[{status}] {lines:>3}  {relative}")
        if lines > MAX_CODE_LINES:
            offenders.append(relative)
    if offenders:
        print(f"\n{len(offenders)} file(s) exceed the {MAX_CODE_LINES} code-line budget.")
        return 1
    print(f"\nAll files are within the {MAX_CODE_LINES} code-line budget.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
