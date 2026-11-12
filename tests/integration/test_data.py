"""Tests of the CSV reader against the file system."""

from pathlib import Path

import pandas as pd
import pytest

from nobel_analysis.constants import DATA_FILE
from nobel_analysis.infrastructure.data import load_nobel


def test_load_nobel_reads_the_bundled_file(raw_df: pd.DataFrame) -> None:
    assert raw_df.shape == (962, 16)
    assert raw_df["year"].dtype.kind == "i"


def test_load_nobel_reads_a_file_from_a_given_folder(tmp_path: Path) -> None:
    (tmp_path / DATA_FILE).write_text("year,category\n1901,Peace\n", encoding="utf-8")
    result = load_nobel(tmp_path)
    assert result.to_dict("records") == [{"year": 1901, "category": "Peace"}]


def test_load_nobel_accepts_a_text_path(tmp_path: Path) -> None:
    (tmp_path / DATA_FILE).write_text("year\n1\n", encoding="utf-8")
    assert len(load_nobel(str(tmp_path))) == 1


def test_load_nobel_raises_for_a_missing_file(tmp_path: Path) -> None:
    with pytest.raises(FileNotFoundError):
        load_nobel(tmp_path)
