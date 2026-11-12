"""Tests of the command line entry point."""

import runpy
import sys
from pathlib import Path

import pandas as pd
import pytest

from nobel_analysis.presentation.cli import main


def test_main_prints_the_report_of_the_bundled_data(
    capsys: pytest.CaptureFixture[str],
) -> None:
    assert main() == 0
    output = capsys.readouterr().out
    assert "Shape: 962 rows, 17 columns" in output
    assert "First year: 1901" in output
    assert "Last year: 2020" in output
    assert "Duplicated rows: 0" in output
    assert "Female laureates: 6.21%" in output
    assert "Categories: 6" in output
    assert "Category with most prizes: Medicine (222)" in output
    assert "First Economics prize: 1969" in output
    assert "Top country: United States of America (281 prizes)" in output
    assert "Top organisation: University of California (40 prizes)" in output
    assert "Oldest winner: John Goodenough (97)" in output
    assert "Youngest winner: Malala Yousafzai (17)" in output
    assert "Mean winning age: 59.95" in output
    assert "75th percentile of winning age: 69" in output


def test_main_reads_from_a_given_folder(
    tmp_path: Path, capsys: pytest.CaptureFixture[str], small_raw_df: pd.DataFrame
) -> None:
    small_raw_df.to_csv(tmp_path / "nobel_prize_data.csv", index=False)
    assert main(tmp_path) == 0
    assert "Shape: 10 rows, 17 columns" in capsys.readouterr().out


def test_python_dash_m_runs_main(
    monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]
) -> None:
    monkeypatch.setattr(sys, "argv", ["nobel_analysis"])
    with pytest.raises(SystemExit) as exit_info:
        runpy.run_module("nobel_analysis", run_name="__main__")
    assert exit_info.value.code == 0
    assert "Shape: 962 rows" in capsys.readouterr().out
