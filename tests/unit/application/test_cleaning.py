"""Tests of the cleaning step on a small hand-made frame."""

import pandas as pd
import pytest

from nobel_analysis.application import cleaning
from nobel_analysis.constants import COL_BIRTH_DATE, COL_SHARE_PCT, COL_YEAR


def test_data_shape_returns_rows_and_columns(small_raw_df: pd.DataFrame) -> None:
    assert cleaning.data_shape(small_raw_df) == (10, 16)


def test_first_and_last_year(small_raw_df: pd.DataFrame) -> None:
    assert cleaning.first_year(small_raw_df) == 1901
    assert cleaning.last_year(small_raw_df) == 1930


def test_count_duplicates_is_zero_for_unique_rows(small_raw_df: pd.DataFrame) -> None:
    assert cleaning.count_duplicates(small_raw_df) == 0


def test_count_duplicates_counts_repeated_rows(small_raw_df: pd.DataFrame) -> None:
    doubled = pd.concat([small_raw_df, small_raw_df.head(2)])
    assert cleaning.count_duplicates(doubled) == 2


def test_nan_per_column_lists_only_columns_with_nan(
    small_raw_df: pd.DataFrame,
) -> None:
    counts = cleaning.nan_per_column(small_raw_df)
    assert counts["organization_name"] == 3
    assert counts["motivation"] == 10
    assert "year" not in counts.index
    assert list(counts.to_numpy()) == sorted(counts.to_numpy(), reverse=True)


def test_nan_per_column_is_empty_without_nan() -> None:
    frame = pd.DataFrame({"a": [1, 2]})
    assert cleaning.nan_per_column(frame).empty


def test_convert_birth_date_gives_datetime(small_raw_df: pd.DataFrame) -> None:
    converted = cleaning.convert_birth_date(small_raw_df)
    assert pd.api.types.is_datetime64_any_dtype(converted[COL_BIRTH_DATE])
    assert converted[COL_BIRTH_DATE].iloc[0].year == 1870
    assert not pd.api.types.is_datetime64_any_dtype(small_raw_df[COL_BIRTH_DATE])


def test_convert_birth_date_keeps_missing_as_nat() -> None:
    frame = pd.DataFrame({COL_BIRTH_DATE: ["1900-01-01", None]})
    converted = cleaning.convert_birth_date(frame)
    assert converted[COL_BIRTH_DATE].isna().tolist() == [False, True]


def test_add_share_pct_computes_percentages(small_raw_df: pd.DataFrame) -> None:
    result = cleaning.add_share_pct(small_raw_df)
    assert result[COL_SHARE_PCT].iloc[0] == 100.0
    assert result[COL_SHARE_PCT].iloc[1] == 50.0
    assert result[COL_SHARE_PCT].iloc[3] == pytest.approx(100 / 3)
    assert COL_SHARE_PCT not in small_raw_df.columns


def test_add_share_pct_rejects_invalid_share() -> None:
    frame = pd.DataFrame({"prize_share": ["1/2", "oops"]})
    with pytest.raises(ValueError):
        cleaning.add_share_pct(frame)


def test_clean_applies_every_step(small_raw_df: pd.DataFrame) -> None:
    result = cleaning.clean(small_raw_df)
    assert COL_SHARE_PCT in result.columns
    assert pd.api.types.is_datetime64_any_dtype(result[COL_BIRTH_DATE])
    assert len(result) == len(small_raw_df)


def test_cleaning_functions_handle_an_empty_frame() -> None:
    empty = pd.DataFrame({COL_YEAR: pd.Series(dtype="int64")})
    assert cleaning.data_shape(empty) == (0, 1)
    assert cleaning.count_duplicates(empty) == 0
    assert cleaning.nan_per_column(empty).empty
