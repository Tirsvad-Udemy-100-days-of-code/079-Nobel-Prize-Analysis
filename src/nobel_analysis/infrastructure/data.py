"""!
@file data.py
@brief Infrastructure: read the Nobel Prize CSV file into a DataFrame.
"""

from pathlib import Path

import pandas as pd

from nobel_analysis.constants import DATA_DIR, DATA_FILE


def load_nobel(data_dir: Path | str | None = None) -> pd.DataFrame:
    """!
    @brief Load nobel_prize_data.csv as the lecture does, without any cleaning.
    @param data_dir Folder with the CSV file; the bundled `data/` when omitted.
    @return The raw DataFrame (962 rows and 16 columns for the lecture data).
    """
    base = DATA_DIR if data_dir is None else Path(data_dir)
    return pd.read_csv(base / DATA_FILE)
