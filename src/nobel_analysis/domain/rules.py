"""!
@file rules.py
@brief Pure business rules of the Nobel Prize data: no I/O and no framework.
"""

from datetime import date


def share_to_percent(prize_share: str) -> float:
    """!
    @brief Convert a prize share written as a fraction into a percentage.
    @param prize_share A fraction such as "1/2" or "1/1".
    @return The share as a floating point percentage, for example 50.0.
    @throws ValueError When the text is not a fraction with a non-zero divisor.
    """
    numerator, separator, denominator = prize_share.partition("/")
    if not separator:
        raise ValueError(f"not a fraction: {prize_share!r}")
    divisor = float(denominator)
    if divisor == 0:
        raise ValueError(f"zero divisor in {prize_share!r}")
    return float(numerator) / divisor * 100


def age_in_year(birth_date: date, year: int) -> int:
    """!
    @brief Age of a person in a given year, as the lecture computes it.
    @param birth_date The date of birth.
    @param year The year of the ceremony.
    @return The year minus the birth year.
    """
    return year - birth_date.year
