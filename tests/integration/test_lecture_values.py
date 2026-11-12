"""The values the lectures give, asserted against the real bundled data set."""

import numpy as np
import pandas as pd
import pytest

from nobel_analysis.application import analysis, cleaning
from nobel_analysis.constants import (
    COL_BIRTH_COUNTRY_CURRENT,
    COL_FULL_NAME,
    COL_ORG_CITY,
    COL_ORG_NAME,
    COL_PRIZE,
    COL_SHARE_PCT,
    COL_WINNING_AGE,
    COL_YEAR,
)


def test_shape_is_962_rows_and_16_columns(raw_df: pd.DataFrame) -> None:
    assert cleaning.data_shape(raw_df) == (962, 16)


def test_first_and_last_year(raw_df: pd.DataFrame) -> None:
    assert cleaning.first_year(raw_df) == 1901
    assert cleaning.last_year(raw_df) == 2020


def test_there_are_no_duplicates(raw_df: pd.DataFrame) -> None:
    assert cleaning.count_duplicates(raw_df) == 0


def test_nan_counts_per_column(raw_df: pd.DataFrame) -> None:
    assert cleaning.nan_per_column(raw_df).to_dict() == {
        "organization_name": 255,
        "organization_city": 255,
        "organization_country": 254,
        "motivation": 88,
        "birth_city": 31,
        "birth_date": 28,
        "sex": 28,
        "birth_country_current": 28,
        "birth_country": 28,
        "ISO": 28,
    }


def test_birth_date_becomes_datetime(clean_df: pd.DataFrame) -> None:
    assert pd.api.types.is_datetime64_any_dtype(clean_df["birth_date"])


def test_share_pct_values(clean_df: pd.DataFrame) -> None:
    counts = clean_df[COL_SHARE_PCT].round(4).value_counts().to_dict()
    assert counts == {100.0: 352, 50.0: 321, 33.3333: 219, 25.0: 70}


def test_women_percentage(clean_df: pd.DataFrame) -> None:
    assert analysis.women_percentage(clean_df) == pytest.approx(6.2098501, abs=1e-6)
    assert analysis.sex_counts(clean_df).to_dict() == {"Male": 876, "Female": 58}


def test_first_three_female_laureates(clean_df: pd.DataFrame) -> None:
    first = analysis.first_female_laureates(clean_df)
    assert first[COL_YEAR].tolist() == [1903, 1905, 1909]
    assert first[COL_FULL_NAME].iloc[0].startswith("Marie Curie")
    assert first["category"].tolist() == ["Physics", "Peace", "Literature"]


def test_repeat_winners(clean_df: pd.DataFrame) -> None:
    names = set(analysis.repeat_winners(clean_df)[COL_FULL_NAME])
    assert len(names) == 6
    assert any(name.startswith("Marie Curie") for name in names)
    assert any(name.startswith("Comit") for name in names)
    assert {"Linus Carl Pauling", "John Bardeen", "Frederick Sanger"} <= names
    assert (
        "Office of the United Nations High Commissioner for Refugees (UNHCR)" in names
    )
    assert len(analysis.repeat_winners(clean_df)) == 13


def test_number_of_categories_and_their_prizes(clean_df: pd.DataFrame) -> None:
    assert analysis.number_of_categories(clean_df) == 6
    counts = analysis.prizes_per_category(clean_df)
    assert counts.to_dict() == {
        "Medicine": 222,
        "Physics": 216,
        "Chemistry": 186,
        "Peace": 135,
        "Literature": 117,
        "Economics": 86,
    }
    assert counts.index[0] == "Medicine"


def test_first_economics_prize_was_in_1969(clean_df: pd.DataFrame) -> None:
    first = analysis.first_prize_in_category(clean_df, "Economics")
    assert first[COL_YEAR].unique().tolist() == [1969]
    assert set(first[COL_FULL_NAME]) == {"Jan Tinbergen", "Ragnar Frisch"}


def test_prizes_by_category_and_sex_covers_every_known_sex(
    clean_df: pd.DataFrame,
) -> None:
    result = analysis.prizes_by_category_and_sex(clean_df)
    assert len(result) == 12
    assert result[COL_PRIZE].sum() == 934


def test_prizes_per_year_and_rolling_average(clean_df: pd.DataFrame) -> None:
    yearly = analysis.prizes_per_year(clean_df)
    assert yearly.head(3).to_dict() == {1901: 6, 1902: 7, 1903: 7}
    average = analysis.rolling_average(yearly)
    assert average.iloc[:4].isna().all()
    assert average.iloc[4] == pytest.approx(6.2)
    assert not np.isnan(average.iloc[4])


def test_average_share_per_year_starts_high(clean_df: pd.DataFrame) -> None:
    share = analysis.average_share_per_year(clean_df)
    assert share[1901] == pytest.approx(83.3333333)
    assert share[1902] == pytest.approx(71.4285714)


def test_top20_countries(clean_df: pd.DataFrame) -> None:
    top = analysis.top20_countries(clean_df)
    assert len(top) == 20
    assert top[COL_BIRTH_COUNTRY_CURRENT].iloc[-1] == "United States of America"
    assert top[COL_PRIZE].iloc[-1] == 281
    assert top[COL_BIRTH_COUNTRY_CURRENT].iloc[-2] == "United Kingdom"
    assert top[COL_PRIZE].iloc[-2] == 105
    assert top[COL_PRIZE].iloc[0] == 9
    assert top[COL_PRIZE].is_monotonic_increasing


def test_country_tables_cover_the_known_countries(clean_df: pd.DataFrame) -> None:
    iso = analysis.prizes_per_country_iso(clean_df)
    assert len(iso) == 79
    assert iso[COL_PRIZE].sum() == 934
    assert analysis.cumulative_prizes_by_country(clean_df)[COL_PRIZE].sum() == 934
    assert analysis.prizes_by_country_and_category(clean_df)[COL_PRIZE].sum() == 803


def test_top_organisations(clean_df: pd.DataFrame) -> None:
    top = analysis.top_organisations(clean_df)
    assert top[COL_ORG_NAME].iloc[-1] == "University of California"
    assert top[COL_PRIZE].iloc[-1] == 40
    assert top[COL_ORG_NAME].iloc[-2] == "Harvard University"
    assert top[COL_PRIZE].iloc[-2] == 29


def test_top_cities(clean_df: pd.DataFrame) -> None:
    organisation_cities = analysis.top_organisation_cities(clean_df)
    assert organisation_cities[COL_ORG_CITY].iloc[-1] == "Cambridge, MA"
    assert organisation_cities[COL_PRIZE].iloc[-1] == 50
    birth_cities = analysis.top_birth_cities(clean_df)
    assert birth_cities["birth_city"].iloc[-1] == "New York, NY"
    assert birth_cities[COL_PRIZE].iloc[-1] == 53


def test_sunburst_data_has_the_organisation_prizes(clean_df: pd.DataFrame) -> None:
    result = analysis.sunburst_data(clean_df)
    assert len(result) == 291
    assert result[COL_PRIZE].sum() == 703


def test_oldest_and_youngest_winner(aged_df: pd.DataFrame) -> None:
    oldest, youngest = analysis.oldest_and_youngest(aged_df)
    assert oldest[COL_FULL_NAME] == "John Goodenough"
    assert oldest[COL_WINNING_AGE] == 97
    assert oldest[COL_YEAR] == 2019
    assert youngest[COL_FULL_NAME] == "Malala Yousafzai"
    assert youngest[COL_WINNING_AGE] == 17
    assert youngest[COL_YEAR] == 2014


def test_winning_age_statistics(aged_df: pd.DataFrame) -> None:
    stats = analysis.age_statistics(aged_df)
    assert stats["count"] == 934
    assert stats["mean"] == pytest.approx(59.9486081, abs=1e-6)
    assert stats["25%"] == 51
    assert stats["50%"] == 60
    assert stats["75%"] == 69
    assert stats["min"] == 17
    assert stats["max"] == 97
    assert aged_df[COL_WINNING_AGE].isna().sum() == 28
