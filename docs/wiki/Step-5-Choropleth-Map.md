**English** · [Dansk](Step-5-Choropleth-Map-da) · [Bahasa Malaysia](Step-5-Choropleth-Map-ms)

# Step 5: A choropleth map and the top countries

**Question:** Which countries win the most prizes, and in which categories?

## Lecture summary

The lecture ranks the countries by prizes won, discusses which country column is the least problematic, and draws the result as a bar chart and a choropleth map. It ends with the prizes of each country split by category and a running total over time.

*Lecture 587*

![chart-step-5-choropleth.png](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/079-Nobel-Prize-Analysis/raw/branch/main/docs/images/chart-step-5-choropleth.png)


## What the code does

`top20_countries` counts prizes per `birth_country_current`: the United States of America leads with **281**, followed by the United Kingdom (105), Germany (84), France (57) and Sweden (29). The column `birth_country_current` is the least problematic: `birth_country` contains countries that no longer exist and `organization_country` has many NaN values. `prizes_per_country_iso` feeds the choropleth map through the `ISO` column, `prizes_by_country_and_category` splits the bars by category and `cumulative_prizes_by_country` uses `.cumsum()` to show how the lead changed over time.

## What you gained

- Choosing the right column matters: every candidate has its own problems.
- A horizontal bar chart ranks countries clearly.
- `px.choropleth` colours a map from ISO country codes.
- Stacking a bar chart by category shows what makes up each total.
- `.cumsum()` after `.groupby()` gives a running total per group.

Previous: [Step-4-Trends-over-Time](Step-4-Trends-over-Time) · Next: [Step-6-Sunburst-Charts](Step-6-Sunburst-Charts)
