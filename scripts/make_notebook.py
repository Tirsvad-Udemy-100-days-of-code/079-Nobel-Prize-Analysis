"""Build notebooks/Nobel_Prize_Analysis.ipynb: one section per lecture step.

Usage:
    python scripts/make_notebook.py
The notebook calls the tested `nobel_analysis` package; run it afterwards with
    jupyter nbconvert --to notebook --execute --inplace notebooks/Nobel_Prize_Analysis.ipynb
"""

from pathlib import Path

import nbformat
from nbformat.v4 import new_code_cell, new_markdown_cell, new_notebook

OUT = Path(__file__).resolve().parents[1] / "notebooks" / "Nobel_Prize_Analysis.ipynb"

CELLS: list[tuple[str, str]] = [
    ("md", """# Nobel Prize Analysis

Day 79 of Udemy's *100 Days of Code: The Complete Python Pro Bootcamp* (lectures 583 to 590).

On November 27, 1895, Alfred Nobel signed his last will in Paris. His estate was to endow "prizes to those who, during the preceding year, have conferred the greatest benefit to humankind". This notebook analyses the past winners with Pandas, Plotly, Matplotlib and Seaborn. The analysis functions live in the tested package `nobel_analysis`; each section below follows one lecture step."""),
    ("md", "## Step 1: The goals of the day (lecture 583)\n\nWe will create a choropleth map, plotly bar and sunburst charts, Seaborn `.lmplot()` charts with `row`, `hue` and `lowess`, and a Seaborn histogram. The data file `nobel_prize_data.csv` is in `data/` (Google Colab is not needed)."),
    ("code", """import matplotlib.pyplot as plt
import pandas as pd

from nobel_analysis.application import analysis, cleaning
from nobel_analysis.infrastructure.data import load_nobel
from nobel_analysis.presentation import charts

pd.options.display.float_format = '{:,.2f}'.format
df_raw = load_nobel()
df_raw.head()"""),
    ("md", """## Step 2: Explore and clean the data set (lecture 584)

**Challenge 1:** What is the shape of `df_data`? Which column names? In which year was the prize first awarded, and what is the latest year?"""),
    ("code", """print("shape:", cleaning.data_shape(df_raw))
print("columns:", list(df_raw.columns))
print("first year:", cleaning.first_year(df_raw), "| last year:", cleaning.last_year(df_raw))"""),
    ("md", "**Answer:** 962 rows and 16 columns; the first prizes were awarded in 1901 and the data goes up to 2020.\n\n**Challenge 2:** Are there duplicates or NaN values, which columns have them, and why?"),
    ("code", """print("duplicates:", cleaning.count_duplicates(df_raw))
cleaning.nan_per_column(df_raw)"""),
    ("md", "**Answer:** no duplicates. Organisation columns are NaN for laureates without a research organisation (many Literature and Peace prizes); birth columns are NaN for organisations that received a prize; `motivation` is missing for some prizes.\n\n**Challenge 3:** Convert `birth_date` to datetimes and add `share_pct`."),
    ("code", """df_data = cleaning.clean(df_raw)
df_data[["birth_date", "prize_share", "share_pct"]].head()"""),
    ("md", "## Step 3: Bar and donut charts (lecture 585)\n\n**Challenge 1:** Come up with 3 questions of your own about this data. For example: what percentage of the laureates were women? How many prizes were given in each category?\n\n**Challenge 2:** What percentage of all prizes went to women? Show it as a donut chart."),
    ("code", """print(f"women: {analysis.women_percentage(df_data):.2f} %")
charts.sex_donut_chart(df_data).show()"""),
    ("md", "**Challenge 3:** Who were the first three women to win, what for, and in which country were they born? Which laureates won more than once?"),
    ("code", """display(analysis.first_female_laureates(df_data)[["year", "category", "full_name", "birth_country"]])
analysis.repeat_winners(df_data)[["full_name", "year", "category"]]"""),
    ("md", "**Challenge 4:** In how many categories are prizes awarded, and which has the most? When was the first Economics prize and who won it?"),
    ("code", """print("categories:", analysis.number_of_categories(df_data))
display(analysis.prizes_per_category(df_data))
display(analysis.first_prize_in_category(df_data, "Economics")[["year", "full_name"]])
charts.category_bar_chart(df_data).show()"""),
    ("md", "**Challenge 5:** Split men and women by category. How many prizes went to women in Literature compared to Physics?"),
    ("code", "charts.category_sex_bar_chart(df_data).show()"),
    ("md", "## Step 4: Trends over time (lecture 586)\n\n**Challenge 1:** Are more prizes awarded recently? Count the prizes per year, add a 5 year rolling average, draw the points in `dodgerblue` and the average in `crimson`, with a tick every 5 years from 1900 to 2020."),
    ("code", """per_year = analysis.prizes_per_year(df_data)
print("most prizes in one year:", per_year.max(), "in", per_year.idxmax())
charts.prizes_per_year_chart(df_data)"""),
    ("md", "**Challenge 2:** Are prizes shared more than before? Average share per year with a 5 year rolling average on a second axis."),
    ("code", "charts.share_per_year_chart(df_data)"),
    ("md", "## Step 5: A choropleth map and the countries with the most prizes (lecture 587)\n\n**Challenge 1:** Create `top20_countries`. Which column is best: `birth_country`, `birth_country_current` or `organization_country`? `birth_country` contains countries that no longer exist and `organization_country` has many NaN values, so `birth_country_current` is the least problematic."),
    ("code", """top20_countries = analysis.top20_countries(df_data)
display(top20_countries.tail(5))
charts.top_countries_bar_chart(df_data).show()"""),
    ("md", "**Challenge 2:** Show the prizes on a choropleth map."),
    ("code", "charts.country_choropleth(df_data).show()"),
    ("md", "**Challenge 3:** In which categories do the countries win prizes? And how did the cumulative number of prizes per country develop?"),
    ("code", """charts.country_category_bar_chart(df_data).show()
analysis.cumulative_prizes_by_country(df_data).tail()"""),
    ("md", "## Step 6: Sunburst charts of research locations (lecture 588)\n\n**Challenge 1:** Which organisations make up the top 20? How many laureates are affiliated with the University of Chicago and Harvard University?"),
    ("code", """top_orgs = analysis.top_organisations(df_data)
display(top_orgs.tail(5))
charts.top_organisations_bar_chart(df_data).show()"""),
    ("md", "**Challenge 2:** Which cities are hot spots for discoveries, and where are laureates born?"),
    ("code", """charts.organisation_cities_bar_chart(df_data).show()
charts.birth_cities_bar_chart(df_data).show()"""),
    ("md", "**Challenge 3:** Combine country, city and organisation in a sunburst chart. Click around in it."),
    ("code", "charts.sunburst_chart(df_data).show()"),
    ("md", "## Step 7: The age of the laureates (lecture 589)\n\n**Challenge 1:** Add `winning_age`, the age in the year of the ceremony.\n\n**Challenge 2:** Who were the oldest and the youngest winners? What is the average age, and below which age are 75 % of the laureates?"),
    ("code", """df_age = analysis.add_winning_age(df_data)
oldest, youngest = analysis.oldest_and_youngest(df_age)
print("oldest:", oldest["full_name"], oldest["winning_age"], oldest["category"])
print("youngest:", youngest["full_name"], youngest["winning_age"], youngest["category"])
analysis.age_statistics(df_age)"""),
    ("md", "Descriptive statistics and the distribution as a Seaborn histogram:"),
    ("code", "charts.winning_age_histogram(df_age)"),
    ("md", "**Challenge 3:** Are laureates nominated later in life than before? `.regplot()` of the winning age over the years."),
    ("code", "charts.winning_age_over_time_chart(df_age)"),
    ("md", "**Challenge 4:** How does the age vary by category? A box plot, then `.lmplot()` with one row per category."),
    ("code", """charts.winning_age_boxplot(df_age)"""),
    ("code", "charts.winning_age_by_category_facets(df_age)"),
    ("md", """## Step 8: Learning points and summary (lecture 590)

Reviewed: finding NaN values, converting objects and strings to numbers, donut and bar charts with plotly, a rolling average for time series, `.value_counts()`, `.groupby()`, `.merge()`, `.sort_values()` and `.agg()`.

New: a choropleth map, bar charts of different segments of the data, sunburst charts, Seaborn `.lmplot()` with `row`, `hue` and `lowess`, how a different picture emerges when you look at the same data in different ways, and the distribution of the data in a Seaborn histogram."""),
]


def main() -> None:
    """Write the notebook file."""
    nb = new_notebook()
    nb.metadata["kernelspec"] = {"display_name": "Python 3", "language": "python", "name": "python3"}
    for kind, text in CELLS:
        nb.cells.append(new_markdown_cell(text) if kind == "md" else new_code_cell(text))
    OUT.parent.mkdir(parents=True, exist_ok=True)
    nbformat.write(nb, OUT)
    print("wrote", OUT)


if __name__ == "__main__":
    main()
