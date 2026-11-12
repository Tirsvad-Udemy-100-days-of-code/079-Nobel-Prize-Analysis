[English](Step-6-Sunburst-Charts) · **Dansk** · [Bahasa Malaysia](Step-6-Sunburst-Charts-ms)

# Trin 6: Sunburst-diagrammer over forskningssteder

**Spørgsmål:** Hvilke forskningsorganisationer og byer havde flest modtagere da opdagelsen blev gjort?

![Trin 6: Sunburst-diagrammer over forskningssteder](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/079-Nobel-Prize-Analysis/raw/branch/main/docs/images/step-6-sunburst-charts.jpg)

*Lektion 588*

![chart-step-6-sunburst.png](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/079-Nobel-Prize-Analysis/raw/branch/main/docs/images/chart-step-6-sunburst.png)


## Hvad koden gør

`top_organisations` rangerer University of California (**40**), Harvard University (**29**), Stanford University (23), MIT (21) og University of Chicago (**20**). `top_organisation_cities` sætter Cambridge, MA først (50) før New York (45) og Cambridge i Storbritannien (31). `top_birth_cities` finder New York (53), Paris (26) og London (19). `sunburst_data` grupperer priser efter organisationens land, by og organisation, og sunburst-diagrammet viser hierarkiet med `px.sunburst`.

## Hvad du lærte

- Samme mønster (`.groupby().agg()` og derefter `.sort_values()`) bruges til organisationer, byer og fødebyer.
- `.dropna()` før et hierarki grupperes.
- Et sunburst-diagram viser del-helhed på flere niveauer og indbyder til at udforske ved at klikke.
- Forskellige spørgsmål peger på forskellige steder: hvor man er født er ikke hvor man arbejdede.

Forrige: [Step-5-Choropleth-Map](Step-5-Choropleth-Map-da) · Næste: [Step-7-Laureate-Age](Step-7-Laureate-Age-da)
