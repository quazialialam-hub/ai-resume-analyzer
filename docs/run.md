# `run.bat`

**Path:** `run.bat` (project root)
**Purpose:** One-click setup and launch for Windows.

## What it does

A double-clickable Windows batch file that takes the project from a fresh
checkout to a running application without any manual steps.

| Step | Action |
| --- | --- |
| 1/3 | Creates a virtual environment in `.venv` if it does not exist yet |
| 2/3 | Installs every dependency from `requirements.txt` |
| 3/3 | Starts the Streamlit app on <http://localhost:8501> |

## Usage

Double-click `run.bat`, or run it from a terminal:

```
run.bat
```

## Behaviour notes

- **The environment is reused.** The virtual environment is only created on
  the first run, so the second start is fast.
- **Python discovery.** The launcher prefers the `py -3` launcher and falls
  back to `python`. If neither works, the error message points at
  <https://www.python.org/downloads/>.
- **Failures are visible.** If the environment cannot be created or the
  dependencies cannot be installed, the script prints the reason and pauses,
  so the window does not close before the message can be read.
- **The virtual environment is local.** Nothing is installed system-wide, and
  nothing outside the project folder is modified.

## Requirements

- Windows
- Python 3.10 or newer, on the PATH
- An internet connection for the first run

## Equivalent manual commands

```
python -m venv .venv
.venv\Scripts\pip install -r requirements.txt
.venv\Scripts\python -m streamlit run app.py
```
