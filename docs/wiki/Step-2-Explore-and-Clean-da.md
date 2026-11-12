[English](Step-2-Explore-and-Clean) · **Dansk** · [Bahasa Malaysia](Step-2-Explore-and-Clean-ms)

# Trin 2: Udforsk og rens datasættet

**Spørgsmål:** Hvilken form har data, er der dubletter eller NaN-værdier, og hvordan gør vi kolonnerne brugbare?

![Trin 2: Udforsk og rens datasættet](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/079-Nobel_Prize_Analysis/raw/branch/main/docs/images/step-2-explore-and-clean.jpg)

*Lektion 584*


## Hvad koden gør

`data_shape` giver **962 rækker og 16 kolonner**. `first_year` er **1901** og `last_year` er **2020**. `count_duplicates` finder **0** dubletter. `nan_per_column` viser hvor der mangler værdier: `organization_name` og `organization_city` (255), `organization_country` (254), `motivation` (88), `birth_city` (31) og 28 hver for `birth_date`, `sex`, `birth_country`, `birth_country_current` og `ISO`. `convert_birth_date` gør `birth_date` til en datetime, og `add_share_pct` omdanner en andel som `1/2` til `50.0`.

## Hvad du lærte

- `.shape`, `.head()` og `.tail()` giver et første indtryk af en tabel.
- `.duplicated()` og `.isna().sum()` finder dubletter og manglende værdier.
- NaN-værdier har ofte en årsag: organisationer har ingen fødselsdata, og litteratur- og fredsprismodtagere har ofte ingen forskningsorganisation.
- `pd.to_datetime` omdanner tekst til datoer; `.map()` bygger en ny kolonne ud fra en gammel.
- I Google Colab skulle man opgradere plotly først; her er afhængigheden angivet i `pyproject.toml`.

Forrige: [Step-1-Goals](Step-1-Goals-da) · Næste: [Step-3-Bar-and-Donut-Charts](Step-3-Bar-and-Donut-Charts-da)
