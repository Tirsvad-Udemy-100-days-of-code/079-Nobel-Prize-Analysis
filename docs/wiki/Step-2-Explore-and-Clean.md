**English** · [Dansk](Step-2-Explore-and-Clean-da) · [Bahasa Malaysia](Step-2-Explore-and-Clean-ms)

# Step 2: Explore and clean the data set

**Question:** What is the shape of the data, are there duplicates or NaN values, and how do we make the columns usable?

## Lecture summary

The lecture loads the data set and inspects it: its shape, the first and last rows, duplicates and missing values. It then converts the birth date to a real date and turns the prize share into a percentage so later steps can calculate with it.

*Lecture 584*


## What the code does

`data_shape` gives **962 rows and 16 columns**. `first_year` is **1901** and `last_year` is **2020**. `count_duplicates` finds **0** duplicates. `nan_per_column` shows where values are missing: `organization_name` and `organization_city` (255), `organization_country` (254), `motivation` (88), `birth_city` (31) and 28 each for `birth_date`, `sex`, `birth_country`, `birth_country_current` and `ISO`. `convert_birth_date` makes `birth_date` a datetime and `add_share_pct` turns a share such as `1/2` into `50.0`.

## What you gained

- `.shape`, `.head()` and `.tail()` give a first impression of a table.
- `.duplicated()` and `.isna().sum()` find duplicates and missing values.
- NaN values often have a reason: organisations have no birth data, and Literature and Peace laureates often have no research organisation.
- `pd.to_datetime` converts text to dates; `.map()` builds a new column from an old one.
- In Google Colab you would upgrade plotly first; here the dependency is declared in `pyproject.toml`.

Previous: [Step-1-Goals](Step-1-Goals) · Next: [Step-3-Bar-and-Donut-Charts](Step-3-Bar-and-Donut-Charts)
