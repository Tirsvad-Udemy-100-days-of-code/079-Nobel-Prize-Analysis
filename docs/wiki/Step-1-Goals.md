**English** · [Dansk](Step-1-Goals-da) · [Bahasa Malaysia](Step-1-Goals-ms)

# Step 1: The goals of the day

**Question:** What do we analyse today, and what will we learn?

## Lecture summary

The lecture introduces the day: study the history of the Nobel Prize to see who wins, where and when. It lists the charts we will build (a choropleth map, bar and sunburst charts, regression lines and a histogram) and the questions we will ask of the data.

*Lecture 583*


## What the code does

The repository already holds the data set (`data/nobel_prize_data.csv`: 962 prizes from 1901 to 2020) and the notebook (`notebooks/Nobel_Prize_Analysis.ipynb`). `load_nobel()` reads the file; no Google Colab is needed.

## What you gained

- The aim: find patterns in the past winners of the Nobel Prize.
- The tools of the day: a choropleth map, plotly bar and sunburst charts, Seaborn `.lmplot()` with `row`, `hue` and `lowess`, and a Seaborn histogram.
- The same data tells different stories depending on how you look at it (box plot against time series).

Previous: [Getting-Started](Getting-Started) · Next: [Step-2-Explore-and-Clean](Step-2-Explore-and-Clean)
