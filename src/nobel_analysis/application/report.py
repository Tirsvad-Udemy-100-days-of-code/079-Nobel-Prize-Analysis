"""!
@file report.py
@brief Use case: summarise the answers of the lecture assignments as text.
"""

import pandas as pd

from nobel_analysis.application import analysis, cleaning
from nobel_analysis.constants import (
    COL_BIRTH_COUNTRY_CURRENT,
    COL_FULL_NAME,
    COL_ORG_NAME,
    COL_PRIZE,
    COL_WINNING_AGE,
    COL_YEAR,
    SEX_FEMALE,
)

## Category whose first prize the report names.
REPORT_CATEGORY: str = "Economics"

## Quantile key of describe() the report shows.
THIRD_QUARTILE_KEY: str = "75%"

## Number of first women the report lists.
FIRST_WOMEN_COUNT: int = 3


def _top_label(counts: pd.DataFrame, column: str) -> str:
    row = counts.iloc[-1]
    return f"{row[column]} ({row[COL_PRIZE]} prizes)"


def _first_year_text(first_rows: pd.DataFrame) -> str:
    if first_rows.empty:
        return "never awarded"
    return str(int(first_rows[COL_YEAR].iloc[0]))


def _nan_lines(df: pd.DataFrame) -> list[str]:
    nan_counts = cleaning.nan_per_column(df)
    return [f"  {name}: {count}" for name, count in nan_counts.items()]


def build_report(df: pd.DataFrame) -> str:
    """!
    @brief Build the text summary of the lecture questions.
    @param df The cleaned data set (share_pct present, birth_date as datetime).
    @return A multi-line report.
    """
    aged = analysis.add_winning_age(df)
    oldest, youngest = analysis.oldest_and_youngest(aged)
    stats = analysis.age_statistics(aged)
    categories = analysis.prizes_per_category(df)
    first_women = analysis.first_female_laureates(df, FIRST_WOMEN_COUNT)
    first_economics = analysis.first_prize_in_category(df, REPORT_CATEGORY)
    repeats = analysis.repeat_winners(df)[COL_FULL_NAME].unique()
    rows, columns = cleaning.data_shape(df)
    lines = [
        f"Shape: {rows} rows, {columns} columns",
        f"First year: {cleaning.first_year(df)}",
        f"Last year: {cleaning.last_year(df)}",
        f"Duplicated rows: {cleaning.count_duplicates(df)}",
        "Columns with NaN values:",
        *_nan_lines(df),
        f"{SEX_FEMALE} laureates: {analysis.women_percentage(df):.2f}%",
        "First women: "
        + ", ".join(
            f"{row[COL_FULL_NAME]} ({row[COL_YEAR]})"
            for _, row in first_women.iterrows()
        ),
        f"Categories: {analysis.number_of_categories(df)}",
        f"Category with most prizes: {categories.index[0]} ({categories.iloc[0]})",
        f"First {REPORT_CATEGORY} prize: {_first_year_text(first_economics)}",
        "Repeat winners: " + "; ".join(str(name) for name in repeats),
        "Top country: "
        + _top_label(analysis.top20_countries(df), COL_BIRTH_COUNTRY_CURRENT),
        "Top organisation: " + _top_label(analysis.top_organisations(df), COL_ORG_NAME),
        f"Oldest winner: {oldest[COL_FULL_NAME]} ({int(oldest[COL_WINNING_AGE])})",
        f"Youngest winner: {youngest[COL_FULL_NAME]} "
        f"({int(youngest[COL_WINNING_AGE])})",
        f"Mean winning age: {stats['mean']:.2f}",
        f"75th percentile of winning age: {stats[THIRD_QUARTILE_KEY]:.0f}",
    ]
    return "\n".join(lines)
