# `scripts/check_loc.py`

**Path:** `scripts/check_loc.py`
**Purpose:** Enforces the 50 code-line budget for every source file.

## What it does

Walks the project, counts the code lines of every Python file and reports
the ones over the limit. A "code line" is any line that is not blank, not a
comment and not part of a docstring, so documentation does not eat into the
budget.

## Usage

```
python scripts/check_loc.py
```

## Output

```
[OK ]  24  resume_analyzer/core/pipeline.py
[OVER] 57  resume_analyzer/ui/inputs.py
```

The script exits with status 1 when a file is over budget, so it can be
wired into CI or a pre-commit hook.

## How the count is made

The file is parsed with `ast`, which gives the exact line range of every
docstring. Those lines, blank lines and comment lines are then excluded from
the count. This is more accurate than counting "non-empty lines", which
would count a docstring as code.

## Why it exists

The project is kept to a maximum of 50 code lines per file so that every
module has one clear job and stays easy to read. This script is the
mechanical check for that rule.

## Notes

- It skips `venv`, `.git`, `__pycache__` and `.freebuff` directories.
- The script itself is written to the same budget, so it is a working
  example of the rule.
