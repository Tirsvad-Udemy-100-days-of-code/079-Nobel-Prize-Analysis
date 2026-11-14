**English** · [Dansk](Step-6-Sunburst-Charts-da) · [Bahasa Malaysia](Step-6-Sunburst-Charts-ms)

# Step 6: Sunburst charts of research locations

**Question:** Which research organisations and cities had the most laureates at the time of the discovery?

## Lecture summary

The lecture asks where discoveries are made. It ranks research organisations and cities, compares them with where laureates were born, and shows the country, city and organisation hierarchy in a sunburst chart.

*Lecture 588*

![chart-step-6-sunburst.png](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/079-Nobel-Prize-Analysis/raw/branch/main/docs/images/chart-step-6-sunburst.png)


## What the code does

`top_organisations` ranks the University of California (**40**), Harvard University (**29**), Stanford University (23), MIT (21) and the University of Chicago (**20**). `top_organisation_cities` puts Cambridge, MA first (50) before New York (45) and Cambridge in the United Kingdom (31). `top_birth_cities` finds New York (53), Paris (26) and London (19). `sunburst_data` groups prizes by organisation country, city and organisation, and the sunburst chart shows that hierarchy with `px.sunburst`.

## What you gained

- Reusing one pattern (`.groupby().agg()` then `.sort_values()`) for organisations, cities and birth cities.
- `.dropna()` before grouping a hierarchy.
- A sunburst chart shows part-to-whole relationships across several levels and invites exploration by clicking.
- Different questions point to different places: where people were born is not where they worked.

Previous: [Step-5-Choropleth-Map](Step-5-Choropleth-Map) · Next: [Step-7-Laureate-Age](Step-7-Laureate-Age)
