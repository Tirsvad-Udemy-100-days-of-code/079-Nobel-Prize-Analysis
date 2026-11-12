"""Shared fixtures: the real data set (session scope) and a small hand-made frame."""

# ruff: noqa: E501  (the table of laureates is easier to read on one line per row)

import matplotlib

matplotlib.use("Agg")  # no display is needed; must run before pyplot is imported

import numpy as np  # noqa: E402
import pandas as pd  # noqa: E402
import pytest  # noqa: E402

from nobel_analysis.application.analysis import add_winning_age  # noqa: E402
from nobel_analysis.application.cleaning import clean  # noqa: E402
from nobel_analysis.constants import (  # noqa: E402
    COL_BIRTH_CITY,
    COL_BIRTH_COUNTRY,
    COL_BIRTH_COUNTRY_CURRENT,
    COL_BIRTH_DATE,
    COL_CATEGORY,
    COL_FULL_NAME,
    COL_ISO,
    COL_LAUREATE_TYPE,
    COL_MOTIVATION,
    COL_ORG_CITY,
    COL_ORG_COUNTRY,
    COL_ORG_NAME,
    COL_PRIZE,
    COL_PRIZE_SHARE,
    COL_SEX,
    COL_YEAR,
)
from nobel_analysis.infrastructure.data import load_nobel  # noqa: E402

FRANCE = "France"
GERMANY = "Germany"
USA = "United States of America"

# (year, category, share, name, birth date, birth city, country, sex, org, org city)
_ROWS: list[tuple[int, str, str, str, str, str, str, str, str | None, str | None]] = [
    (1901, "Physics", "1/1", "Ann A", "1870-01-01", "Paris", FRANCE, "Female", "Uni X", "Paris"),
    (1901, "Chemistry", "1/2", "Bob B", "1860-05-05", "Berlin", GERMANY, "Male", "Uni Y", "Berlin"),
    (1901, "Chemistry", "1/2", "Cid C", "1865-06-06", "Berlin", GERMANY, "Male", "Uni Y", "Berlin"),
    (1910, "Physics", "1/3", "Ann A", "1870-01-01", "Paris", FRANCE, "Female", "Uni X", "Paris"),
    (1910, "Physics", "1/3", "Dee D", "1880-02-02", "Paris", FRANCE, "Male", "Uni X", "Paris"),
    (1910, "Physics", "1/3", "Eve E", "1885-03-03", "Boston", USA, "Female", "Uni W", "Boston, MA"),
    (1920, "Chemistry", "1/1", "Fay F", "1890-04-04", "Berlin", GERMANY, "Male", None, None),
    (1920, "Medicine", "1/1", "Gus G", "1880-07-07", "Paris", FRANCE, "Male", None, None),
    (1930, "Medicine", "1/2", "Hal H", "1890-08-08", "Boston", USA, "Male", "Uni W", "Boston, MA"),
    (1930, "Medicine", "1/2", "Ian I", "1895-09-09", "Boston", USA, "Male", None, None),
]  # fmt: skip

_ISO = {FRANCE: "FRA", GERMANY: "DEU", USA: "USA"}
_ORG_COUNTRY = {"Uni X": FRANCE, "Uni Y": GERMANY, "Uni W": USA}


@pytest.fixture(scope="session")
def raw_df() -> pd.DataFrame:
    """The lecture data set exactly as read from the CSV file."""
    return load_nobel()


@pytest.fixture(scope="session")
def clean_df(raw_df: pd.DataFrame) -> pd.DataFrame:
    """The lecture data set after cleaning."""
    return clean(raw_df)


@pytest.fixture(scope="session")
def aged_df(clean_df: pd.DataFrame) -> pd.DataFrame:
    """The cleaned lecture data set with the winning_age column."""
    return add_winning_age(clean_df)


@pytest.fixture
def small_raw_df() -> pd.DataFrame:
    """Ten hand-made laureates in the raw layout: dates and shares as text."""
    records = []
    for year, category, share, name, born, city, country, sex, org, org_city in _ROWS:
        records.append(
            {
                COL_YEAR: year,
                COL_CATEGORY: category,
                COL_PRIZE: f"The Nobel Prize in {category} {year}",
                COL_MOTIVATION: np.nan,
                COL_PRIZE_SHARE: share,
                COL_LAUREATE_TYPE: "Individual",
                COL_FULL_NAME: name,
                COL_BIRTH_DATE: born,
                COL_BIRTH_CITY: city,
                COL_BIRTH_COUNTRY: country,
                COL_BIRTH_COUNTRY_CURRENT: country,
                COL_SEX: sex,
                COL_ORG_NAME: org if org else np.nan,
                COL_ORG_CITY: org_city if org_city else np.nan,
                COL_ORG_COUNTRY: _ORG_COUNTRY[org] if org else np.nan,
                COL_ISO: _ISO[country],
            }
        )
    return pd.DataFrame.from_records(records)


@pytest.fixture
def small_clean_df(small_raw_df: pd.DataFrame) -> pd.DataFrame:
    """The small frame after cleaning."""
    return clean(small_raw_df)


@pytest.fixture
def small_aged_df(small_clean_df: pd.DataFrame) -> pd.DataFrame:
    """The small cleaned frame with winning_age."""
    return add_winning_age(small_clean_df)
