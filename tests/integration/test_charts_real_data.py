"""The charts built from the real data set carry the lecture numbers."""

import numpy as np
import pandas as pd

from nobel_analysis.presentation import charts


def test_donut_chart_shows_876_men_and_58_women(clean_df: pd.DataFrame) -> None:
    figure = charts.sex_donut_chart(clean_df)
    assert dict(zip(figure.data[0].labels, figure.data[0].values, strict=True)) == {
        "Male": 876,
        "Female": 58,
    }


def test_top_countries_chart_ends_with_the_united_states(
    clean_df: pd.DataFrame,
) -> None:
    figure = charts.top_countries_bar_chart(clean_df)
    assert len(figure.data[0].y) == 20
    assert figure.data[0].y[-1] == "United States of America"
    assert figure.data[0].x[-1] == 281


def test_prizes_per_year_chart_has_one_point_per_year(clean_df: pd.DataFrame) -> None:
    figure = charts.prizes_per_year_chart(clean_df)
    assert len(np.asarray(figure.axes[0].collections[0].get_offsets())) == 117


def test_boxplot_and_facets_have_six_categories(aged_df: pd.DataFrame) -> None:
    assert len(charts.winning_age_by_category_facets(aged_df).axes) == 6
    labels = charts.winning_age_boxplot(aged_df).axes[0].get_xticklabels()
    assert len(labels) == 6


def test_sunburst_and_choropleth_build_from_real_data(clean_df: pd.DataFrame) -> None:
    assert len(charts.country_choropleth(clean_df).data[0].locations) == 79
    assert "United States of America" in charts.sunburst_chart(clean_df).data[0].labels
