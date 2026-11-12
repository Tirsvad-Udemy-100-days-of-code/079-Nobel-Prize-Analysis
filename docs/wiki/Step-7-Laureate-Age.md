**English** · [Dansk](Step-7-Laureate-Age-da) · [Bahasa Malaysia](Step-7-Laureate-Age-ms)

# Step 7: The age of the laureates

**Question:** How old are the laureates when they win the prize, does it vary by category, and how has it changed over time?

![Step 7: The age of the laureates](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/079-Nobel_Prize_Analysis/raw/branch/main/docs/images/step-7-laureate-age.jpg)

*Lecture 589*

![chart-step-7-age-histogram.png](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/079-Nobel_Prize_Analysis/raw/branch/main/docs/images/chart-step-7-age-histogram.png)


## What the code does

`add_winning_age` adds `winning_age`, the year of the ceremony minus the birth year. `oldest_and_youngest` finds the oldest winner, John Goodenough (Chemistry, **97**), and the youngest, Malala Yousafzai (Peace, **17**). `age_statistics` gives a mean of **59.95** years and a 75th percentile of **69**: three quarters of the laureates are younger than 69. The charts are a Seaborn histogram, a `.regplot()` of age against year, a box plot per category and `.lmplot()` with `row` per category and `lowess=True`.

## What you gained

- Date arithmetic: `.dt.year` on a datetime column.
- `.describe()` gives count, mean, quartiles and extremes in one call; `.idxmax()` and `.idxmin()` find the rows of the extremes.
- A histogram shows a distribution; the number of bins changes the picture.
- A regression line with `lowess` follows a trend without assuming a straight line; `row` and `hue` split it by category.
- Box plots and time series show different pictures of the same data.

Previous: [Step-6-Sunburst-Charts](Step-6-Sunburst-Charts) · Next: [Summary](Summary)
