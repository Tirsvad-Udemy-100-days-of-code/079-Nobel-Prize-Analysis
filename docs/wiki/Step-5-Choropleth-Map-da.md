[English](Step-5-Choropleth-Map) · **Dansk** · [Bahasa Malaysia](Step-5-Choropleth-Map-ms)

# Trin 5: Et choropleth-kort og de bedste lande

**Spørgsmål:** Hvilke lande vinder flest priser, og i hvilke kategorier?

![Trin 5: Et choropleth-kort og de bedste lande](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/079-Nobel-Prize-Analysis/raw/branch/main/docs/images/step-5-choropleth-map.jpg)

*Lektion 587*

![chart-step-5-choropleth.png](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/079-Nobel-Prize-Analysis/raw/branch/main/docs/images/chart-step-5-choropleth.png)


## Hvad koden gør

`top20_countries` tæller priser pr. `birth_country_current`: USA fører med **281**, efterfulgt af Storbritannien (105), Tyskland (84), Frankrig (57) og Sverige (29). Kolonnen `birth_country_current` er den mindst problematiske: `birth_country` indeholder lande, der ikke længere findes, og `organization_country` har mange NaN-værdier. `prizes_per_country_iso` fodrer choropleth-kortet via kolonnen `ISO`, `prizes_by_country_and_category` deler søjlerne op efter kategori, og `cumulative_prizes_by_country` bruger `.cumsum()` til at vise hvordan føringen skiftede over tid.

## Hvad du lærte

- Det betyder noget at vælge den rigtige kolonne: hver kandidat har sine problemer.
- Et vandret søjlediagram rangerer lande tydeligt.
- `px.choropleth` farver et kort ud fra ISO-landekoder.
- At stable et søjlediagram efter kategori viser hvad hver total består af.
- `.cumsum()` efter `.groupby()` giver en løbende sum pr. gruppe.

Forrige: [Step-4-Trends-over-Time](Step-4-Trends-over-Time-da) · Næste: [Step-6-Sunburst-Charts](Step-6-Sunburst-Charts-da)
