[English](Getting-Started) · **Dansk** · [Bahasa Malaysia](Getting-Started-ms)

# Kom i gang

Krav: Python 3.13 eller nyere. Kørselsafhængigheder: `pandas`, `numpy`, `plotly`, `matplotlib` og `seaborn`.

## Windows (PowerShell)

Opret og brug en lokal `.venv`:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

## Linux og macOS

Opret og brug en lokal `.venv`:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

## Kør analysen, testene, typetjekket og notebooken (ens på begge systemer):

```bash
python -m nobel_analysis
python -m pytest
python -m mypy
jupyter lab notebooks/Nobel_Prize_Analysis.ipynb
```

Scan koden med opengrep, før du pusher (Windows-standardsti `~/.opengrep/cli/latest/opengrep.exe`):

```bash
bash scripts/scan.sh
```

**Hvad du får:** en gentagelig opsætning (et virtuelt miljø pr. projekt), en pakke du installerer i redigerbar tilstand, og tests der beviser hvert svar.

Forrige: [Home](Home-da) · Næste: [Step-1-Goals](Step-1-Goals-da)
