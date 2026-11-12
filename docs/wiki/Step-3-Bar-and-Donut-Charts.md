**English** · [Dansk](Step-3-Bar-and-Donut-Charts-da) · [Bahasa Malaysia](Step-3-Bar-and-Donut-Charts-ms)

# Step 3: Bar and donut charts with plotly

**Question:** Which categories award the most prizes, and what share of the laureates are women?

![Step 3: Bar and donut charts with plotly](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/079-Nobel_Prize_Analysis/raw/branch/main/docs/images/step-3-bar-and-donut-charts.jpg)

*Lecture 585*

![chart-step-3-donut.png](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/079-Nobel_Prize_Analysis/raw/branch/main/docs/images/chart-step-3-donut.png)

![chart-step-3-categories.png](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/079-Nobel_Prize_Analysis/raw/branch/main/docs/images/chart-step-3-categories.png)


## What the code does

`sex_counts` gives 876 men and 58 women, so `women_percentage` is **6.21 %** (shown as a donut chart). `first_female_laureates` finds Marie Curie (Physics, 1903), Bertha von Suttner (Peace, 1905) and Selma Lagerlöf (Literature, 1909). `repeat_winners` lists those who won more than once: Marie Curie, Linus Pauling, John Bardeen, Frederick Sanger, the Red Cross (three times) and the UNHCR. `number_of_categories` is **6**; `prizes_per_category` ranks Medicine (222), Physics (216), Chemistry (186), Peace (135), Literature (117) and Economics (86). `first_prize_in_category` shows the first Economics prize in **1969**. `prizes_by_category_and_sex` feeds the stacked bar chart.

## What you gained

- A donut chart is a pie chart with `hole` set.
- A bar chart can be coloured with a named colour scale (`Aggrnyl`) without showing the colour axis.
- `.groupby()` with `.agg()` counts rows per group; `.value_counts()` is the shortcut.
- Asking good questions of the data is a skill of its own, and the data cannot answer every question.

Previous: [Step-2-Explore-and-Clean](Step-2-Explore-and-Clean) · Next: [Step-4-Trends-over-Time](Step-4-Trends-over-Time)
