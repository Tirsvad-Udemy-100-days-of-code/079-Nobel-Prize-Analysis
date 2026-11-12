**English** · [Dansk](Getting-Started-da) · [Bahasa Malaysia](Getting-Started-ms)

# Getting started

Requirements: Python 3.13 or newer. Runtime dependencies: `pandas`, `numpy`, `plotly`, `matplotlib` and `seaborn`.

## Windows (PowerShell)

Create and use a local `.venv`:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

## Linux and macOS

Create and use a local `.venv`:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

## Run the analysis, the tests, the type check and the notebook (the same on both systems):

```bash
python -m nobel_analysis
python -m pytest
python -m mypy
jupyter lab notebooks/Nobel_Prize_Analysis.ipynb
```

Scan the code with opengrep before you push (Windows default path `~/.opengrep/cli/latest/opengrep.exe`):

```bash
bash scripts/scan.sh
```

**What you gain:** a repeatable set-up (a virtual environment per project), a package you install in editable mode, and tests that prove each answer.

Previous: [Home](Home) · Next: [Step-1-Goals](Step-1-Goals)
