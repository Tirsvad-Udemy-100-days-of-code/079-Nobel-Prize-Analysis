"""Tests of the pure business rules."""

from datetime import date

import pytest

from nobel_analysis.domain.rules import age_in_year, share_to_percent


@pytest.mark.parametrize(
    ("share", "expected"),
    [("1/1", 100.0), ("1/2", 50.0), ("1/4", 25.0), ("0/3", 0.0)],
)
def test_share_to_percent_returns_percentage(share: str, expected: float) -> None:
    assert share_to_percent(share) == expected


def test_share_to_percent_handles_a_third() -> None:
    assert share_to_percent("1/3") == pytest.approx(33.3333333)


@pytest.mark.parametrize("text", ["", "abc", "0.5", "1-2"])
def test_share_to_percent_rejects_text_without_fraction(text: str) -> None:
    with pytest.raises(ValueError):
        share_to_percent(text)


def test_share_to_percent_rejects_zero_divisor() -> None:
    with pytest.raises(ValueError, match="zero divisor"):
        share_to_percent("1/0")


def test_share_to_percent_rejects_non_numeric_parts() -> None:
    with pytest.raises(ValueError):
        share_to_percent("a/b")


def test_age_in_year_subtracts_birth_year() -> None:
    assert age_in_year(date(1867, 11, 7), 1903) == 36


def test_age_in_year_is_zero_in_birth_year() -> None:
    assert age_in_year(date(1950, 12, 31), 1950) == 0
