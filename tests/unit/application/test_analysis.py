"""Tests of the analysis functions on a small hand-made frame."""

import numpy as np
import pandas as pd
import pytest

from nobel_analysis.application import analysis
from nobel_analysis.constants import (
    COL_BIRTH_COUNTRY_CURRENT,
    COL_BIRTH_DATE,
    COL_CATEGORY,
    COL_FULL_NAME,
    COL_ORG_NAME,
    COL_PRIZE,
    COL_SEX,
    COL_WINNING_AGE,
    COL_YEAR,
    SEX_FEMALE,
)


def test_women_percentage_is_share_of_known_sexes(small_clean_df: pd.DataFrame) -> None:
    assert analysis.women_percentage(small_clean_df) == pytest.approx(30.0)


def test_women_percentage_ignores_missing_sex() -> None:
    frame = pd.DataFrame({COL_SEX: [SEX_FEMALE, "Male", None, None]})
    assert analysis.women_percentage(frame) == pytest.approx(50.0)


def test_sex_counts(small_clean_df: pd.DataFrame) -> None:
    counts = analysis.sex_counts(small_clean_df)
    assert counts.to_dict() == {"Male": 7, "Female": 3}


def test_first_female_laureates_are_in_year_order(
    small_clean_df: pd.DataFrame,
) -> None:
    first = analysis.first_female_laureates(small_clean_df, 2)
    assert first[COL_FULL_NAME].tolist() == ["Ann A", "Ann A"]
    assert first[COL_YEAR].tolist() == [1901, 1910]


def test_first_female_laureates_default_is_at_most_three(
    small_clean_df: pd.DataFrame,
) -> None:
    assert len(analysis.first_female_laureates(small_clean_df)) == 3


def test_first_female_laureates_empty_without_women() -> None:
    frame = pd.DataFrame({COL_SEX: ["Male"], COL_YEAR: [1901]})
    assert analysis.first_female_laureates(frame).empty


def test_repeat_winners_returns_all_rows_of_repeaters(
    small_clean_df: pd.DataFrame,
) -> None:
    repeats = analysis.repeat_winners(small_clean_df)
    assert repeats[COL_FULL_NAME].tolist() == ["Ann A", "Ann A"]


def test_repeat_winners_empty_when_everyone_wins_once() -> None:
    frame = pd.DataFrame({COL_FULL_NAME: ["a", "b"]})
    assert analysis.repeat_winners(frame).empty


def test_number_of_categories(small_clean_df: pd.DataFrame) -> None:
    assert analysis.number_of_categories(small_clean_df) == 3


def test_number_of_categories_of_empty_frame_is_zero() -> None:
    assert analysis.number_of_categories(pd.DataFrame({COL_CATEGORY: []})) == 0


def test_prizes_per_category_is_largest_first(small_clean_df: pd.DataFrame) -> None:
    counts = analysis.prizes_per_category(small_clean_df)
    assert counts.index[0] == "Physics"
    assert counts["Physics"] == 4


def test_first_prize_in_category_returns_rows_of_earliest_year(
    small_clean_df: pd.DataFrame,
) -> None:
    first = analysis.first_prize_in_category(small_clean_df, "Chemistry")
    assert first[COL_YEAR].tolist() == [1901, 1901]


def test_first_prize_in_unknown_category_is_empty(
    small_clean_df: pd.DataFrame,
) -> None:
    assert analysis.first_prize_in_category(small_clean_df, "Maths").empty


def test_prizes_by_category_and_sex(small_clean_df: pd.DataFrame) -> None:
    result = analysis.prizes_by_category_and_sex(small_clean_df)
    assert len(result) == 4
    assert result[COL_PRIZE].sum() == 10
    physics_women = result[
        (result[COL_CATEGORY] == "Physics") & (result[COL_SEX] == SEX_FEMALE)
    ]
    assert physics_women[COL_PRIZE].iloc[0] == 3


def test_prizes_per_year(small_clean_df: pd.DataFrame) -> None:
    assert analysis.prizes_per_year(small_clean_df).to_dict() == {
        1901: 3,
        1910: 3,
        1920: 2,
        1930: 2,
    }


def test_rolling_average_has_nan_for_first_window_minus_one() -> None:
    result = analysis.rolling_average(pd.Series([1, 2, 3, 4, 5, 6]))
    assert result.iloc[:4].isna().all()
    assert result.iloc[4] == 3.0
    assert result.iloc[5] == 4.0


def test_rolling_average_accepts_a_window() -> None:
    result = analysis.rolling_average(pd.Series([2.0, 4.0, 6.0]), window=2)
    assert np.isnan(result.iloc[0])
    assert result.iloc[1:].tolist() == [3.0, 5.0]


def test_rolling_average_of_series_shorter_than_window_is_all_nan() -> None:
    assert analysis.rolling_average(pd.Series([1, 2])).isna().all()


def test_average_share_per_year(small_clean_df: pd.DataFrame) -> None:
    share = analysis.average_share_per_year(small_clean_df)
    assert share[1901] == pytest.approx(200 / 3)
    assert share[1910] == pytest.approx(100 / 3)
    assert share[1920] == 100.0
    assert share[1930] == 50.0


def test_top20_countries_is_smallest_first(small_clean_df: pd.DataFrame) -> None:
    top = analysis.top20_countries(small_clean_df)
    assert len(top) == 3
    assert top[COL_BIRTH_COUNTRY_CURRENT].iloc[-1] == "France"
    assert top[COL_PRIZE].is_monotonic_increasing


def test_top20_countries_limits_to_top_n(small_clean_df: pd.DataFrame) -> None:
    top = analysis.top20_countries(small_clean_df, top_n=1)
    assert top[COL_BIRTH_COUNTRY_CURRENT].tolist() == ["France"]
    assert top[COL_PRIZE].tolist() == [4]


def test_top20_countries_of_empty_frame_is_empty(
    small_clean_df: pd.DataFrame,
) -> None:
    assert analysis.top20_countries(small_clean_df.head(0)).empty


def test_prizes_per_country_iso(small_clean_df: pd.DataFrame) -> None:
    result = analysis.prizes_per_country_iso(small_clean_df)
    assert len(result) == 3
    assert result["ISO"].iloc[0] == "FRA"
    assert result[COL_PRIZE].sum() == 10


def test_prizes_by_country_and_category_keeps_top_countries(
    small_clean_df: pd.DataFrame,
) -> None:
    result = analysis.prizes_by_country_and_category(small_clean_df, top_n=1)
    assert set(result[COL_BIRTH_COUNTRY_CURRENT]) == {"France"}
    assert result[COL_PRIZE].sum() == 4


def test_cumulative_prizes_by_country_only_grows(
    small_clean_df: pd.DataFrame,
) -> None:
    result = analysis.cumulative_prizes_by_country(small_clean_df)
    france = result[result[COL_BIRTH_COUNTRY_CURRENT] == "France"]
    assert france["cumulative_prizes"].tolist() == [1, 3, 4]


def test_top_organisations_ignores_missing_organisations(
    small_clean_df: pd.DataFrame,
) -> None:
    top = analysis.top_organisations(small_clean_df)
    assert top[COL_ORG_NAME].iloc[-1] == "Uni X"
    assert top[COL_PRIZE].iloc[-1] == 3
    assert len(top) == 3


def test_top_organisation_cities(small_clean_df: pd.DataFrame) -> None:
    top = analysis.top_organisation_cities(small_clean_df)
    assert top["organization_city"].iloc[-1] == "Paris"


def test_top_birth_cities(small_clean_df: pd.DataFrame) -> None:
    top = analysis.top_birth_cities(small_clean_df, top_n=1)
    assert top["birth_city"].tolist() == ["Paris"]
    assert top[COL_PRIZE].tolist() == [4]


def test_sunburst_data_drops_rows_without_organisation(
    small_clean_df: pd.DataFrame,
) -> None:
    result = analysis.sunburst_data(small_clean_df)
    assert len(result) == 3
    assert result[COL_PRIZE].sum() == 7


def test_add_winning_age_subtracts_birth_year(small_clean_df: pd.DataFrame) -> None:
    aged = analysis.add_winning_age(small_clean_df)
    assert aged[COL_WINNING_AGE].tolist() == [31, 41, 36, 40, 30, 25, 30, 40, 40, 35]
    assert COL_WINNING_AGE not in small_clean_df.columns


def test_add_winning_age_is_nan_without_birth_date() -> None:
    frame = pd.DataFrame(
        {
            COL_YEAR: [1950, 1960],
            COL_BIRTH_DATE: pd.to_datetime(pd.Series(["1900-01-01", None])),
        }
    )
    aged = analysis.add_winning_age(frame)
    assert aged[COL_WINNING_AGE].iloc[0] == 50
    assert np.isnan(aged[COL_WINNING_AGE].iloc[1])


def test_oldest_and_youngest(small_aged_df: pd.DataFrame) -> None:
    oldest, youngest = analysis.oldest_and_youngest(small_aged_df)
    assert oldest[COL_FULL_NAME] == "Bob B"
    assert youngest[COL_FULL_NAME] == "Eve E"


def test_age_statistics(small_aged_df: pd.DataFrame) -> None:
    stats = analysis.age_statistics(small_aged_df)
    assert stats["count"] == 10
    assert stats["mean"] == pytest.approx(34.8)
    assert stats["min"] == 25
    assert stats["max"] == 41
