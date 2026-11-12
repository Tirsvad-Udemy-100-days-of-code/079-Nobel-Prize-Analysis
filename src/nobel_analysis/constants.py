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

## Hole size of the donut chart (fraction of the radius).
DONUT_HOLE: float = 0.4

## Range in years of the x axis of the time charts.
YEAR_AXIS_START: int = 1900
YEAR_AXIS_END: int = 2020

## Figure size in inches, facet size and marker style of the charts.
FIGURE_SIZE: tuple[float, float] = (16.0, 8.0)
FACET_HEIGHT: float = 3.0
FACET_ASPECT: float = 3.0
POINT_SIZE: int = 50
LINE_WIDTH: float = 3.0
POINT_ALPHA: float = 0.7

## Plotly sunburst size in pixels.
SUNBURST_SIZE: int = 800

## Chart titles.
TITLE_SEX: str = "Percentage of Male vs. Female Winners"
TITLE_CATEGORY: str = "Number of Prizes Awarded per Category"
TITLE_CATEGORY_SEX: str = "Number of Prizes Awarded per Category split by Sex"
TITLE_COUNTRIES: str = "Top 20 Countries by Number of Prizes"
TITLE_CHOROPLETH: str = "Number of Prizes by Country"
TITLE_COUNTRY_CATEGORY: str = "Top 20 Countries by Number of Prizes and Category"
TITLE_ORGANISATIONS: str = "Top 20 Research Institutions by Number of Prizes"
TITLE_ORG_CITIES: str = "Which Cities Make the Most Discoveries?"
TITLE_BIRTH_CITIES: str = "Where were the Nobel Laureates Born?"
TITLE_SUNBURST: str = "Where do Discoveries Take Place?"
TITLE_PRIZES_PER_YEAR: str = "Number of Nobel Prizes Awarded per Year"
TITLE_SHARE_PER_YEAR: str = "Number of Prizes and Average Prize Share per Year"
TITLE_AGE_HISTOGRAM: str = "Distribution of Winning Age"
TITLE_AGE_BY_CATEGORY: str = "Winning Age by Category"
TITLE_AGE_OVER_TIME: str = "Winning Age over Time"

## Axis labels.
LABEL_PRIZES: str = "Number of Prizes"
LABEL_SHARE: str = "Average Prize Share (%)"
LABEL_YEAR: str = "Year"
LABEL_AGE: str = "Age at the Time of the Award"
