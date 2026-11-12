"""!
@file cleaning.py
@brief Lecture 584: explore and clean the data set.
"""

import pandas as pd

from nobel_analysis.constants import (
    COL_BIRTH_DATE,
    COL_PRIZE_SHARE,
    COL_SHARE_PCT,
    COL_YEAR,
)
from nobel_analysis.domain.rules import share_to_percent


def data_shape(df: pd.DataFrame) -> tuple[int, int]:
    """!
    @brief Rows and columns of the data set.
    @param df The data set.
    @return A (rows, columns) tuple.
    """
    return df.shape


def first_year(df: pd.DataFrame) -> int:
    """!
    @brief The year the prize was first awarded.
    @param df The data set.
    @return The smallest year.
    """
    return int(df[COL_YEAR].min())


def last_year(df: pd.DataFrame) -> int:
    """!
    @brief The latest year in the data set.
    @param df The data set.
    @return The largest year.
    """
    return int(df[COL_YEAR].max())


def count_duplicates(df: pd.DataFrame) -> int:
    """!
    @brief Number of fully duplicated rows.
    @param df The data set.
    @return The count of duplicate rows.
    """
    return int(df.duplicated().sum())


def nan_per_column(df: pd.DataFrame) -> pd.Series:
    """!
    @brief Number of NaN values per column, columns without any left out.
    @param df The data set.
    @return A Series indexed by column name, sorted from most to fewest NaN.
    """
    counts = df.isna().sum()
    return counts[counts > 0].sort_values(ascending=False)


def convert_birth_date(df: pd.DataFrame) -> pd.DataFrame:
    """!
    @brief Convert the birth_date text column to Pandas datetime values.
    @param df The data set.
    @return A copy with a datetime64 birth_date column (NaT where missing).
    """
    out = df.copy()
    out[COL_BIRTH_DATE] = pd.to_datetime(out[COL_BIRTH_DATE])
    return out


def add_share_pct(df: pd.DataFrame) -> pd.DataFrame:
    """!
    @brief Add the share_pct column: the prize share as a percentage.
    @param df The data set.
    @return A copy with a floating point share_pct column.
    """
    out = df.copy()
    out[COL_SHARE_PCT] = out[COL_PRIZE_SHARE].map(share_to_percent)
    return out


def clean(df: pd.DataFrame) -> pd.DataFrame:
    """!
    @brief Apply every cleaning step of the lecture.
    @param df The raw data set.
    @return The data set with datetime birth dates and a share_pct column.
    """
    return add_share_pct(convert_birth_date(df))
