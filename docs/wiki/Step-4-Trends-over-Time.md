**English** · [Dansk](Step-4-Trends-over-Time-da) · [Bahasa Malaysia](Step-4-Trends-over-Time-ms)

# Step 4: Trends over time with Matplotlib

**Question:** Are more prizes awarded recently than when the prize was created, and are prizes shared more than before?

## Lecture summary

The lecture looks at the number of prizes per year and asks whether more prizes are given now. A 5 year rolling average smooths the noise, and a second axis shows whether prizes are shared among more people over time.

*Lecture 586*

![chart-step-4-prizes-per-year.png](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/079-Nobel-Prize-Analysis/raw/branch/main/docs/images/chart-step-4-prizes-per-year.png)


## What the code does

`prizes_per_year` counts the prizes of each year (the peak is **15 in 2001**). `rolling_average` smooths them with a 5 year window, so the first four values are NaN. The chart draws the points in `dodgerblue` and the average in `crimson`, with a tick every 5 years from 1900 to 2020 made with NumPy. `average_share_per_year` and its rolling average show whether the share per winner changes, drawn on a second y-axis.

## What you gained

- `.rolling(window=5).mean()` smooths a noisy time series so the trend shows.
- Matplotlib can superimpose a line on a scatter plot and use two y-axes (`twinx`).
- `np.arange` generates tick marks at regular steps.
- Named colours such as `dodgerblue` and `crimson` make charts readable.

Previous: [Step-3-Bar-and-Donut-Charts](Step-3-Bar-and-Donut-Charts) · Next: [Step-5-Choropleth-Map](Step-5-Choropleth-Map)
