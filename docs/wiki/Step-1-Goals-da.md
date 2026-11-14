[English](Step-1-Goals) · **Dansk** · [Bahasa Malaysia](Step-1-Goals-ms)

# Trin 1: Dagens mål

**Spørgsmål:** Hvad analyserer vi i dag, og hvad lærer vi?

## Resumé af lektionen

Lektionen introducerer dagen: vi studerer Nobelprisens historie for at se, hvem der vinder, hvor og hvornår. Den opremser de diagrammer, vi skal bygge (et choropleth-kort, søjle- og sunburst-diagrammer, regressionslinjer og et histogram) og de spørgsmål, vi stiller til data.

*Lektion 583*


## Hvad koden gør

Repositoriet indeholder allerede datasættet (`data/nobel_prize_data.csv`: 962 priser fra 1901 til 2020) og notebooken (`notebooks/Nobel_Prize_Analysis.ipynb`). `load_nobel()` læser filen; Google Colab er ikke nødvendig.

## Hvad du lærte

- Målet: finde mønstre hos tidligere Nobelprismodtagere.
- Dagens værktøjer: et choropleth-kort, plotly-søjle- og sunburst-diagrammer, Seaborn `.lmplot()` med `row`, `hue` og `lowess` samt et Seaborn-histogram.
- De samme data fortæller forskellige historier, afhængigt af hvordan man ser på dem (boksplot mod tidsserie).

Forrige: [Getting-Started](Getting-Started-da) · Næste: [Step-2-Explore-and-Clean](Step-2-Explore-and-Clean-da)
