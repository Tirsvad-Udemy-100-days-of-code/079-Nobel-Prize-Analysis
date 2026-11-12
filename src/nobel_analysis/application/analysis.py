"""!
@file analysis.py
@brief Lectures 585 to 589: the analysis functions, named as in the assignment.
"""

import pandas as pd

from nobel_analysis.constants import (
    COL_BIRTH_CITY,
    COL_BIRTH_COUNTRY_CURRENT,
    COL_BIRTH_DATE,
    COL_CATEGORY,
    COL_FULL_NAME,
    COL_ISO,
    COL_ORG_CITY,
    COL_ORG_COUNTRY,
    COL_ORG_NAME,
    COL_PRIZE,
    COL_SEX,
    COL_SHARE_PCT,
    COL_WINNING_AGE,
    COL_YEAR,
    ROLLING_WINDOW,
    SEX_FEMALE,
    TOP_N,
)

COL_COUNT = "prize"


def women_percentage(df: pd.DataFrame) -> float:
    """!
    @brief Percentage of all laureates that are women.
    @param df The data set.
    @return The percentage, 0 to 100.
    """
    return float((df[COL_SEX] == SEX_FEMALE).sum() / df[COL_SEX].notna().sum() * 100)


def sex_counts(df: pd.DataFrame) -> pd.Series:
    """!
    @brief Number of prizes that went to each sex (data for the donut chart).
    @param df The data set.
    @return Counts indexed by sex.
    """
    return df[COL_SEX].value_counts()


def first_female_laureates(df: pd.DataFrame, count: int = 3) -> pd.DataFrame:
    """!
    @brief The first women to win a Nobel Prize.
    @param df The data set.
    @param count How many to return.
    @return The earliest rows for women.
    """
    women = df[df[COL_SEX] == SEX_FEMALE].sort_values(COL_YEAR)
    return women.head(count)


def repeat_winners(df: pd.DataFrame) -> pd.DataFrame:
    """!
    @brief Laureates that won more than once.
    @param df The data set.
    @return Rows of every laureate that appears at least twice, by name.
    """
    names = df[COL_FULL_NAME]
    return df[names.duplicated(keep=False)].sort_values(COL_FULL_NAME)


def number_of_categories(df: pd.DataFrame) -> int:
    """!
    @brief In how many categories prizes are awarded.
    @param df The data set.
    @return The number of distinct categories.
    """
    return int(df[COL_CATEGORY].nunique())


def prizes_per_category(df: pd.DataFrame) -> pd.Series:
    """!
    @brief Number of prizes per category, largest first.
    @param df The data set.
    @return Counts indexed by category.
    """
    return df[COL_CATEGORY].value_counts()


def first_prize_in_category(df: pd.DataFrame, category: str) -> pd.DataFrame:
    """!
    @brief The rows of the first year a prize was awarded in a category.
    @param df The data set.
    @param category The category, for example "Economics".
    @return The rows of the earliest year of that category.
    """
    rows = df[df[COL_CATEGORY] == category]
    earliest: pd.DataFrame = rows[rows[COL_YEAR] == rows[COL_YEAR].min()]
    return earliest


def prizes_by_category_and_sex(df: pd.DataFrame) -> pd.DataFrame:
    """!
    @brief Prizes per category split by sex (data for the stacked bar chart).
    @param df The data set.
    @return Columns category, sex and prize, with the counts.
    """
    counts = df.groupby([COL_CATEGORY, COL_SEX], as_index=False).agg(
        prize=(COL_PRIZE, "count")
    )
    ranked: pd.DataFrame = counts.sort_values(COL_COUNT, ascending=False)
    return ranked.reset_index(drop=True)


def prizes_per_year(df: pd.DataFrame) -> pd.Series:
    """!
    @brief Number of prizes awarded in each year.
    @param df The data set.
    @return Counts indexed by year, in year order.
    """
    return df.groupby(COL_YEAR)[COL_PRIZE].count()


def rolling_average(series: pd.Series, window: int = ROLLING_WINDOW) -> pd.Series:
    """!
    @brief Rolling mean that smooths a yearly series.
    @param series A yearly series.
    @param window The window in years.
    @return The rolling mean; the first window-1 values are NaN.
    """
    return series.rolling(window=window).mean()


def average_share_per_year(df: pd.DataFrame) -> pd.Series:
    """!
    @brief Average prize share (as a percentage) of the winners in each year.
    @param df The cleaned data set with share_pct.
    @return The yearly mean of share_pct.
    """
    return df.groupby(COL_YEAR)[COL_SHARE_PCT].mean()


def _top_counts(df: pd.DataFrame, column: str, top_n: int) -> pd.DataFrame:
    counts = df.groupby(column, as_index=False).agg(prize=(COL_PRIZE, "count"))
    ranked = counts.sort_values(COL_COUNT, ascending=True)
    return ranked.tail(top_n).reset_index(drop=True)


def top20_countries(df: pd.DataFrame, top_n: int = TOP_N) -> pd.DataFrame:
    """!
    @brief The countries with most prizes, by birth_country_current.
    @param df The data set.
    @param top_n How many countries to keep.
    @return Columns birth_country_current and prize, smallest first for a bar chart.
    """
    return _top_counts(df, COL_BIRTH_COUNTRY_CURRENT, top_n)


def prizes_per_country_iso(df: pd.DataFrame) -> pd.DataFrame:
    """!
    @brief Prizes per country with the ISO code (data for the choropleth map).
    @param df The data set.
    @return Columns birth_country_current, ISO and prize.
    """
    out = df.groupby([COL_BIRTH_COUNTRY_CURRENT, COL_ISO], as_index=False).agg(
        prize=(COL_PRIZE, "count")
    )
    return out.sort_values(COL_COUNT, ascending=False).reset_index(drop=True)


def prizes_by_country_and_category(
    df: pd.DataFrame, top_n: int = TOP_N
) -> pd.DataFrame:
    """!
    @brief The top countries with their prizes split by category.
    @param df The data set.
    @param top_n How many countries to keep.
    @return Columns birth_country_current, category and prize.
    """
    keep = top20_countries(df, top_n)[COL_BIRTH_COUNTRY_CURRENT]
    subset = df[df[COL_BIRTH_COUNTRY_CURRENT].isin(keep)]
    return subset.groupby(
        [COL_BIRTH_COUNTRY_CURRENT, COL_CATEGORY], as_index=False
    ).agg(prize=(COL_PRIZE, "count"))


def cumulative_prizes_by_country(df: pd.DataFrame) -> pd.DataFrame:
    """!
    @brief Cumulative number of prizes won by each country in every year.
    @param df The data set.
    @return Columns year, birth_country_current, prize and cumulative_prizes.
    """
    yearly = df.groupby([COL_YEAR, COL_BIRTH_COUNTRY_CURRENT], as_index=False).agg(
        prize=(COL_PRIZE, "count")
    )
    grouped = yearly.groupby(COL_BIRTH_COUNTRY_CURRENT)[COL_COUNT]
    yearly["cumulative_prizes"] = grouped.cumsum()
    return yearly


def top_organisations(df: pd.DataFrame, top_n: int = TOP_N) -> pd.DataFrame:
    """!
    @brief Research organisations with most laureates.
    @param df The data set.
    @param top_n How many to keep.
    @return Columns organization_name and prize, smallest first.
    """
    return _top_counts(df, COL_ORG_NAME, top_n)


def top_organisation_cities(df: pd.DataFrame, top_n: int = TOP_N) -> pd.DataFrame:
    """!
    @brief Cities with most laureate-affiliated research institutions.
    @param df The data set.
    @param top_n How many to keep.
    @return Columns organization_city and prize, smallest first.
    """
    return _top_counts(df, COL_ORG_CITY, top_n)


def top_birth_cities(df: pd.DataFrame, top_n: int = TOP_N) -> pd.DataFrame:
    """!
    @brief Cities where most laureates were born.
    @param df The data set.
    @param top_n How many to keep.
    @return Columns birth_city and prize, smallest first.
    """
    return _top_counts(df, COL_BIRTH_CITY, top_n)


def sunburst_data(df: pd.DataFrame) -> pd.DataFrame:
    """!
    @brief Prizes per country, city and organisation (data for the sunburst).
    @param df The data set.
    @return Columns organization_country, organization_city, organization_name, prize.
    """
    org = df.dropna(subset=[COL_ORG_COUNTRY, COL_ORG_CITY, COL_ORG_NAME])
    keys = [COL_ORG_COUNTRY, COL_ORG_CITY, COL_ORG_NAME]
    return org.groupby(keys, as_index=False).agg(prize=(COL_PRIZE, "count"))


def add_winning_age(df: pd.DataFrame) -> pd.DataFrame:
    """!
    @brief Add winning_age: the age in the year of the ceremony.
    @param df The cleaned data set (datetime birth_date).
    @return A copy with the winning_age column.
    """
    out = df.copy()
    out[COL_WINNING_AGE] = out[COL_YEAR] - out[COL_BIRTH_DATE].dt.year
    return out


def oldest_and_youngest(df: pd.DataFrame) -> tuple[pd.Series, pd.Series]:
    """!
    @brief The oldest and the youngest winner.
    @param df The data set with winning_age.
    @return A (oldest, youngest) tuple of rows.
    """
    ages = df[COL_WINNING_AGE]
    oldest = df.loc[[ages.idxmax()]].iloc[0]
    youngest = df.loc[[ages.idxmin()]].iloc[0]
    return oldest, youngest


def age_statistics(df: pd.DataFrame) -> pd.Series:
    """!
    @brief Descriptive statistics of the winning age (mean, quartiles, extremes).
    @param df The data set with winning_age.
    @return The output of describe().
    """
    return df[COL_WINNING_AGE].describe()
