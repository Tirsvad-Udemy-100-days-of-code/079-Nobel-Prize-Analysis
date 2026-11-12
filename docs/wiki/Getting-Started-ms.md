[English](Getting-Started) · [Dansk](Getting-Started-da) · **Bahasa Malaysia**

# Bermula

Keperluan: Python 3.13 atau lebih baharu. Kebergantungan masa jalan: `pandas`, `numpy`, `plotly`, `matplotlib` dan `seaborn`.

## Windows (PowerShell)

Cipta dan gunakan `.venv` setempat:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

## Linux dan macOS

Cipta dan gunakan `.venv` setempat:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

## Jalankan analisis, ujian, semakan jenis dan buku nota (sama pada kedua-dua sistem):

```bash
python -m nobel_analysis
python -m pytest
python -m mypy
jupyter lab notebooks/Nobel_Prize_Analysis.ipynb
```

Imbas kod dengan opengrep sebelum anda push (laluan lalai Windows `~/.opengrep/cli/latest/opengrep.exe`):

```bash
bash scripts/scan.sh
```

**Apa yang anda peroleh:** persediaan yang boleh diulang (persekitaran maya bagi setiap projek), pakej yang dipasang dalam mod boleh sunting, dan ujian yang membuktikan setiap jawapan.

Sebelumnya: [Home](Home-ms) · Seterusnya: [Step-1-Goals](Step-1-Goals-ms)
