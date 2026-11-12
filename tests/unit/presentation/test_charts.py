"""Tests of the chart functions on a small hand-made frame."""

import numpy as np
import pandas as pd
import plotly.graph_objects as go
import pytest
from matplotlib.colors import to_rgba
from matplotlib.figure import Figure
from matplotlib.patches import Rectangle

from nobel_analysis.constants import (
    COLOR_AVERAGE,
    COLOR_POINTS,
    DONUT_HOLE,
    POINT_ALPHA,
    YEAR_AXIS_END,
    YEAR_AXIS_START,
    YEAR_TICK_STEP,
)
from nobel_analysis.presentation import charts


def _values(figure: go.Figure, axis: str) -> list[object]:
    return list(figure.data[0][axis])


def test_sex_donut_chart_is_a_pie_with_a_hole(small_clean_df: pd.DataFrame) -> None:
    figure = charts.sex_donut_chart(small_clean_df)
    assert isinstance(figure, go.Figure)
    assert isinstance(figure.data[0], go.Pie)
    assert figure.data[0].hole == DONUT_HOLE
    assert dict(zip(figure.data[0].labels, figure.data[0].values, strict=True)) == {
        "Male": 7,
        "Female": 3,
    }


def test_category_bar_chart_hides_the_colour_axis(
    small_clean_df: pd.DataFrame,
) -> None:
    figure = charts.category_bar_chart(small_clean_df)
    assert figure.layout.coloraxis.showscale is False
    assert _values(figure, "x") == ["Physics", "Chemistry", "Medicine"]
    assert _values(figure, "y") == [4, 3, 3]


def test_category_sex_bar_chart_has_a_trace_per_sex(
    small_clean_df: pd.DataFrame,
) -> None:
    figure = charts.category_sex_bar_chart(small_clean_df)
    assert {trace.name for trace in figure.data} == {"Male", "Female"}
    assert sum(sum(trace.y) for trace in figure.data) == 10


def test_top_countries_bar_chart_is_horizontal(small_clean_df: pd.DataFrame) -> None:
    figure = charts.top_countries_bar_chart(small_clean_df)
    assert figure.data[0].orientation == "h"
    assert _values(figure, "y")[-1] == "France"
    assert _values(figure, "x")[-1] == 4
    assert figure.layout.coloraxis.showscale is False


def test_country_choropleth_locates_by_iso(small_clean_df: pd.DataFrame) -> None:
    figure = charts.country_choropleth(small_clean_df)
    assert isinstance(figure.data[0], go.Choropleth)
    assert set(figure.data[0].locations) == {"FRA", "DEU", "USA"}


def test_country_category_bar_chart_has_a_trace_per_category(
    small_clean_df: pd.DataFrame,
) -> None:
    figure = charts.country_category_bar_chart(small_clean_df)
    assert {trace.name for trace in figure.data} == {"Physics", "Chemistry", "Medicine"}
    assert figure.layout.yaxis.categoryarray[-1] == "France"


def test_top_organisations_bar_chart(small_clean_df: pd.DataFrame) -> None:
    figure = charts.top_organisations_bar_chart(small_clean_df)
    assert _values(figure, "y")[-1] == "Uni X"


def test_organisation_cities_bar_chart(small_clean_df: pd.DataFrame) -> None:
    figure = charts.organisation_cities_bar_chart(small_clean_df)
    assert _values(figure, "y")[-1] == "Paris"


def test_birth_cities_bar_chart(small_clean_df: pd.DataFrame) -> None:
    figure = charts.birth_cities_bar_chart(small_clean_df)
    assert _values(figure, "y")[-1] == "Paris"
    assert _values(figure, "x")[-1] == 4


def test_sunburst_chart_has_country_city_and_organisation_levels(
    small_clean_df: pd.DataFrame,
) -> None:
    figure = charts.sunburst_chart(small_clean_df)
    assert isinstance(figure.data[0], go.Sunburst)
    labels = set(figure.data[0].labels)
    assert {"France", "Paris", "Uni X"} <= labels


def test_prizes_per_year_chart_draws_points_and_average(
    small_clean_df: pd.DataFrame,
) -> None:
    figure = charts.prizes_per_year_chart(small_clean_df)
    assert isinstance(figure, Figure)
    axes = figure.axes[0]
    assert len(np.asarray(axes.collections[0].get_offsets())) == 4
    assert axes.lines[0].get_color() == COLOR_AVERAGE
    facecolor = np.asarray(axes.collections[0].get_facecolor())[0].tolist()
    assert facecolor == pytest.approx(list(to_rgba(COLOR_POINTS, POINT_ALPHA)))


def test_prizes_per_year_chart_ticks_every_five_years(
    small_clean_df: pd.DataFrame,
) -> None:
    ticks = charts.prizes_per_year_chart(small_clean_df).axes[0].get_xticks()
    expected = np.arange(YEAR_AXIS_START, YEAR_AXIS_END + 1, YEAR_TICK_STEP)
    assert ticks.tolist() == expected.tolist()


def test_share_per_year_chart_has_a_second_y_axis(
    small_clean_df: pd.DataFrame,
) -> None:
    figure = charts.share_per_year_chart(small_clean_df)
    assert len(figure.axes) == 2
    assert figure.axes[1].lines[0].get_color() == COLOR_AVERAGE
    assert figure.axes[1].get_ylabel() == "Average Prize Share (%)"


def test_winning_age_histogram_has_bars(small_aged_df: pd.DataFrame) -> None:
    figure = charts.winning_age_histogram(small_aged_df)
    assert isinstance(figure, Figure)
    bars = [p for p in figure.axes[0].patches if isinstance(p, Rectangle)]
    assert sum(bar.get_height() for bar in bars) == 10


def test_winning_age_over_time_chart_has_a_fit_line(
    small_aged_df: pd.DataFrame,
) -> None:
    figure = charts.winning_age_over_time_chart(small_aged_df)
    axes = figure.axes[0]
    assert len(axes.lines) == 1
    assert len(np.asarray(axes.collections[0].get_offsets())) == 10


def test_winning_age_boxplot_has_a_box_per_category(
    small_aged_df: pd.DataFrame,
) -> None:
    figure = charts.winning_age_boxplot(small_aged_df)
    labels = [label.get_text() for label in figure.axes[0].get_xticklabels()]
    assert sorted(labels) == ["Chemistry", "Medicine", "Physics"]


def test_winning_age_by_category_facets_has_a_row_per_category(
    small_aged_df: pd.DataFrame,
) -> None:
    figure = charts.winning_age_by_category_facets(small_aged_df)
    assert isinstance(figure, Figure)
    assert len(figure.axes) == 3
