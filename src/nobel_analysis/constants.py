"""!
@file constants.py
@brief Every constant of the Nobel Prize analysis in one place.
"""

from pathlib import Path

## Folder that holds the data set shipped with the lecture.
DATA_DIR: Path = Path(__file__).resolve().parents[2] / "data"

## File name of the lecture data set.
DATA_FILE: str = "nobel_prize_data.csv"

## Column names of the data set.
COL_YEAR: str = "year"
COL_CATEGORY: str = "category"
COL_PRIZE: str = "prize"
COL_MOTIVATION: str = "motivation"
COL_PRIZE_SHARE: str = "prize_share"
COL_LAUREATE_TYPE: str = "laureate_type"
COL_FULL_NAME: str = "full_name"
COL_BIRTH_DATE: str = "birth_date"
COL_BIRTH_CITY: str = "birth_city"
COL_BIRTH_COUNTRY: str = "birth_country"
COL_BIRTH_COUNTRY_CURRENT: str = "birth_country_current"
COL_SEX: str = "sex"
COL_ORG_NAME: str = "organization_name"
COL_ORG_CITY: str = "organization_city"
COL_ORG_COUNTRY: str = "organization_country"
COL_ISO: str = "ISO"

## Columns added by the cleaning step.
COL_SHARE_PCT: str = "share_pct"
COL_WINNING_AGE: str = "winning_age"

## Values of the `sex` column.
SEX_FEMALE: str = "Female"
SEX_MALE: str = "Male"

## Size of the top lists in the lecture (countries, organisations, cities).
TOP_N: int = 20

## Window in years of the rolling averages.
ROLLING_WINDOW: int = 5

## Tick spacing in years of the time charts.
YEAR_TICK_STEP: int = 5

## Plotly colour scales named in the lecture.
SCALE_CATEGORY: str = "Aggrnyl"
SCALE_BIRTH_CITY: str = "Plasma"
SCALE_COUNTRY: str = "matter"

## Fixed seeds and sizes of the charts.
HISTOGRAM_BINS: int = 30

## Names of the Matplotlib colours the lecture asks for.
COLOR_POINTS: str = "dodgerblue"
COLOR_AVERAGE: str = "crimson"
