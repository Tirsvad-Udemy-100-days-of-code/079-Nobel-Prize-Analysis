"""!
@file charts.py
@brief Presentation: every chart of the lectures, returned as a figure.

No function here shows or saves a figure; the caller decides. Plotly charts
return a plotly Figure, Matplotlib and Seaborn charts a matplotlib Figure.
"""

import numpy as np
import numpy.typing as npt
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import seaborn as sns
from matplotlib.figure import Figure

from nobel_analysis.application import analysis
from nobel_analysis.constants import (
    COL_BIRTH_CITY,
    COL_BIRTH_COUNTRY_CURRENT,
    COL_CATEGORY,
    COL_ISO,
    COL_ORG_CITY,
    COL_ORG_COUNTRY,
    COL_ORG_NAME,
    COL_PRIZE,
    COL_SEX,
    COL_WINNING_AGE,
    COL_YEAR,
    COLOR_AVERAGE,
    COLOR_POINTS,
    DONUT_HOLE,
    FACET_ASPECT,
    FACET_HEIGHT,
    FIGURE_SIZE,
    HISTOGRAM_BINS,
    LABEL_AGE,
    LABEL_PRIZES,
    LABEL_SHARE,
    LABEL_YEAR,
    LINE_WIDTH,
    POINT_ALPHA,
    POINT_SIZE,
    ROLLING_WINDOW,
    SCALE_BIRTH_CITY,
    SCALE_CATEGORY,
    SCALE_COUNTRY,
    SUNBURST_SIZE,
    TITLE_AGE_BY_CATEGORY,
    TITLE_AGE_HISTOGRAM,
    TITLE_AGE_OVER_TIME,
    TITLE_BIRTH_CITIES,
    TITLE_CATEGORY,
    TITLE_CATEGORY_SEX,
    TITLE_CHOROPLETH,
    TITLE_COUNTRIES,
    TITLE_COUNTRY_CATEGORY,
    TITLE_ORG_CITIES,
    TITLE_ORGANISATIONS,
    TITLE_PRIZES_PER_YEAR,
    TITLE_SEX,
    TITLE_SHARE_PER_YEAR,
    TITLE_SUNBURST,
    YEAR_AXIS_END,
    YEAR_AXIS_START,
    YEAR_TICK_STEP,
)


def _year_ticks() -> npt.NDArray[np.int_]:
    return np.arange(YEAR_AXIS_START, YEAR_AXIS_END + 1, YEAR_TICK_STEP)


def _horizontal_bar(
    data: pd.DataFrame, label_column: str, title: str, scale: str
) -> go.Figure:
    figure: go.Figure = px.bar(
        data,
        x=COL_PRIZE,
        y=label_column,
        orientation="h",
        color=COL_PRIZE,
        color_continuous_scale=scale,
        title=title,
    )
    figure.update_layout(
        xaxis_title=LABEL_PRIZES, yaxis_title=None, coloraxis_showscale=False
    )
    return figure


def sex_donut_chart(df: pd.DataFrame) -> go.Figure:
    """!
    @brief Donut chart of the prizes won by men and by women.
    @param df The data set.
    @return A Plotly figure.
    """
    counts = analysis.sex_counts(df)
    figure: go.Figure = px.pie(
        names=counts.index,
        values=counts.to_numpy(),
        title=TITLE_SEX,
        hole=DONUT_HOLE,
    )
    return figure


def category_bar_chart(df: pd.DataFrame) -> go.Figure:
    """!
    @brief Bar chart of the number of prizes per category.
    @param df The data set.
    @return A Plotly figure with the colour axis hidden.
    """
    counts = analysis.prizes_per_category(df)
    figure: go.Figure = px.bar(
        x=counts.index,
        y=counts.to_numpy(),
        color=counts.to_numpy(),
        color_continuous_scale=SCALE_CATEGORY,
        title=TITLE_CATEGORY,
    )
    figure.update_layout(
        xaxis_title=COL_CATEGORY.capitalize(),
        yaxis_title=LABEL_PRIZES,
        coloraxis_showscale=False,
    )
    return figure


def category_sex_bar_chart(df: pd.DataFrame) -> go.Figure:
    """!
    @brief Stacked bar chart of the prizes per category split by sex.
    @param df The data set.
    @return A Plotly figure.
    """
    data = analysis.prizes_by_category_and_sex(df)
    figure: go.Figure = px.bar(
        data, x=COL_CATEGORY, y=COL_PRIZE, color=COL_SEX, title=TITLE_CATEGORY_SEX
    )
    figure.update_layout(
        xaxis_title=COL_CATEGORY.capitalize(), yaxis_title=LABEL_PRIZES
    )
    return figure


def top_countries_bar_chart(df: pd.DataFrame) -> go.Figure:
    """!
    @brief Horizontal bar chart of the countries with most prizes.
    @param df The data set.
    @return A Plotly figure.
    """
    data = analysis.top20_countries(df)
    return _horizontal_bar(
        data, COL_BIRTH_COUNTRY_CURRENT, TITLE_COUNTRIES, SCALE_COUNTRY
    )


def country_choropleth(df: pd.DataFrame) -> go.Figure:
    """!
    @brief World map coloured by the number of prizes per country.
    @param df The data set.
    @return A Plotly figure located by ISO code.
    """
    data = analysis.prizes_per_country_iso(df)
    figure: go.Figure = px.choropleth(
        data,
        locations=COL_ISO,
        color=COL_PRIZE,
        hover_name=COL_BIRTH_COUNTRY_CURRENT,
        color_continuous_scale=SCALE_COUNTRY,
        title=TITLE_CHOROPLETH,
    )
    return figure


def country_category_bar_chart(df: pd.DataFrame) -> go.Figure:
    """!
    @brief Horizontal bar chart of the top countries split by category.
    @param df The data set.
    @return A Plotly figure with one stacked segment per category.
    """
    data = analysis.prizes_by_country_and_category(df)
    totals = data.groupby(COL_BIRTH_COUNTRY_CURRENT)[COL_PRIZE].sum()
    order = totals.sort_values().index.tolist()
    figure: go.Figure = px.bar(
        data,
        x=COL_PRIZE,
        y=COL_BIRTH_COUNTRY_CURRENT,
        color=COL_CATEGORY,
        orientation="h",
        title=TITLE_COUNTRY_CATEGORY,
    )
    figure.update_layout(
        xaxis_title=LABEL_PRIZES,
        yaxis_title=None,
        yaxis={"categoryorder": "array", "categoryarray": order},
    )
    return figure


def top_organisations_bar_chart(df: pd.DataFrame) -> go.Figure:
    """!
    @brief Horizontal bar chart of the organisations with most laureates.
    @param df The data set.
    @return A Plotly figure.
    """
    data = analysis.top_organisations(df)
    return _horizontal_bar(data, COL_ORG_NAME, TITLE_ORGANISATIONS, SCALE_COUNTRY)


def organisation_cities_bar_chart(df: pd.DataFrame) -> go.Figure:
    """!
    @brief Horizontal bar chart of the cities with most research institutions.
    @param df The data set.
    @return A Plotly figure.
    """
    data = analysis.top_organisation_cities(df)
    return _horizontal_bar(data, COL_ORG_CITY, TITLE_ORG_CITIES, SCALE_COUNTRY)


def birth_cities_bar_chart(df: pd.DataFrame) -> go.Figure:
    """!
    @brief Horizontal bar chart of the cities where most laureates were born.
    @param df The data set.
    @return A Plotly figure.
    """
    data = analysis.top_birth_cities(df)
    return _horizontal_bar(data, COL_BIRTH_CITY, TITLE_BIRTH_CITIES, SCALE_BIRTH_CITY)


def sunburst_chart(df: pd.DataFrame) -> go.Figure:
    """!
    @brief Sunburst of country, city and organisation weighted by prizes.
    @param df The data set.
    @return A Plotly figure.
    """
    data = analysis.sunburst_data(df)
    figure: go.Figure = px.sunburst(
        data,
        path=[COL_ORG_COUNTRY, COL_ORG_CITY, COL_ORG_NAME],
        values=COL_PRIZE,
        title=TITLE_SUNBURST,
        width=SUNBURST_SIZE,
        height=SUNBURST_SIZE,
    )
    return figure


def prizes_per_year_chart(df: pd.DataFrame) -> Figure:
    """!
    @brief Scatter of prizes per year with its rolling average.
    @param df The data set.
    @return A Matplotlib figure.
    """
    yearly = analysis.prizes_per_year(df)
    average = analysis.rolling_average(yearly)
    figure = Figure(figsize=FIGURE_SIZE)
    axes = figure.subplots()
    axes.set_title(TITLE_PRIZES_PER_YEAR)
    axes.set_xticks(_year_ticks())
    axes.set_xlabel(LABEL_YEAR)
    axes.set_ylabel(LABEL_PRIZES)
    axes.scatter(
        yearly.index,
        yearly.to_numpy(),
        c=COLOR_POINTS,
        s=POINT_SIZE,
        alpha=POINT_ALPHA,
    )
    axes.plot(
        average.index,
        average.to_numpy(),
        c=COLOR_AVERAGE,
        linewidth=LINE_WIDTH,
        label=f"{ROLLING_WINDOW}-year average",
    )
    axes.legend()
    return figure


def share_per_year_chart(df: pd.DataFrame) -> Figure:
    """!
    @brief Average prize share per year with its rolling average, on two axes.
    @param df The cleaned data set with share_pct.
    @return A Matplotlib figure whose second y axis holds the share.
    """
    yearly = analysis.prizes_per_year(df)
    average = analysis.rolling_average(yearly)
    share = analysis.rolling_average(analysis.average_share_per_year(df))
    figure = Figure(figsize=FIGURE_SIZE)
    axes = figure.subplots()
    share_axes = axes.twinx()
    axes.set_title(TITLE_SHARE_PER_YEAR)
    axes.set_xticks(_year_ticks())
    axes.set_xlabel(LABEL_YEAR)
    axes.set_ylabel(LABEL_PRIZES)
    share_axes.set_ylabel(LABEL_SHARE)
    axes.scatter(
        yearly.index,
        yearly.to_numpy(),
        c=COLOR_POINTS,
        s=POINT_SIZE,
        alpha=POINT_ALPHA,
    )
    axes.plot(average.index, average.to_numpy(), c=COLOR_POINTS, linewidth=LINE_WIDTH)
    share_axes.plot(
        share.index, share.to_numpy(), c=COLOR_AVERAGE, linewidth=LINE_WIDTH
    )
    return figure


def winning_age_histogram(df: pd.DataFrame) -> Figure:
    """!
    @brief Histogram of the age at which laureates won.
    @param df The data set with winning_age.
    @return A Matplotlib figure.
    """
    figure = Figure(figsize=FIGURE_SIZE)
    axes = figure.subplots()
    sns.histplot(data=df, x=COL_WINNING_AGE, bins=HISTOGRAM_BINS, ax=axes)
    axes.set_title(TITLE_AGE_HISTOGRAM)
    axes.set_xlabel(LABEL_AGE)
    return figure


def winning_age_over_time_chart(df: pd.DataFrame) -> Figure:
    """!
    @brief Scatter with a lowess trend line of winning age against the year.
    @param df The data set with winning_age.
    @return A Matplotlib figure.
    """
    figure = Figure(figsize=FIGURE_SIZE)
    axes = figure.subplots()
    sns.regplot(
        data=df,
        x=COL_YEAR,
        y=COL_WINNING_AGE,
        lowess=True,
        scatter_kws={"alpha": POINT_ALPHA},
        line_kws={"color": COLOR_AVERAGE},
        ax=axes,
    )
    axes.set_title(TITLE_AGE_OVER_TIME)
    axes.set_ylabel(LABEL_AGE)
    return figure


def winning_age_boxplot(df: pd.DataFrame) -> Figure:
    """!
    @brief Box plot of the winning age in each category.
    @param df The data set with winning_age.
    @return A Matplotlib figure.
    """
    figure = Figure(figsize=FIGURE_SIZE)
    axes = figure.subplots()
    sns.boxplot(data=df, x=COL_CATEGORY, y=COL_WINNING_AGE, ax=axes)
    axes.set_title(TITLE_AGE_BY_CATEGORY)
    axes.set_ylabel(LABEL_AGE)
    return figure


def winning_age_by_category_facets(df: pd.DataFrame) -> Figure:
    """!
    @brief One lowess panel per category of winning age against the year.
    @param df The data set with winning_age.
    @return The Matplotlib figure of the Seaborn facet grid.
    """
    grid = sns.lmplot(
        data=df,
        x=COL_YEAR,
        y=COL_WINNING_AGE,
        row=COL_CATEGORY,
        height=FACET_HEIGHT,
        aspect=FACET_ASPECT,
        lowess=True,
        scatter_kws={"alpha": POINT_ALPHA},
        line_kws={"color": COLOR_AVERAGE},
    )
    figure: Figure = grid.figure
    return figure
