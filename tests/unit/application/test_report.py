"""Tests of the text report on a small hand-made frame."""

import pandas as pd

from nobel_analysis.application.report import build_report


def test_build_report_contains_the_lecture_answers(
    small_clean_df: pd.DataFrame,
) -> None:
    report = build_report(small_clean_df)
    assert "Shape: 10 rows, 17 columns" in report
    assert "First year: 1901" in report
    assert "Last year: 1930" in report
    assert "Duplicated rows: 0" in report
    assert "organization_name: 3" in report
    assert "Female laureates: 30.00%" in report
    assert "First women: Ann A (1901), Ann A (1910), Eve E (1910)" in report
    assert "Categories: 3" in report
    assert "Category with most prizes: Physics (4)" in report
    assert "First Economics prize: never awarded" in report
    assert "Repeat winners: Ann A" in report
    assert "Top country: France (4 prizes)" in report
    assert "Top organisation: Uni X (3 prizes)" in report
    assert "Oldest winner: Bob B (41)" in report
    assert "Youngest winner: Eve E (25)" in report
    assert "Mean winning age: 34.80" in report
    assert "75th percentile of winning age: 40" in report
