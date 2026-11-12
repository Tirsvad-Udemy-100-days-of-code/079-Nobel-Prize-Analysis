"""Smoke test: the package imports and its constants point at the data file."""

from nobel_analysis import __version__
from nobel_analysis.constants import DATA_DIR, DATA_FILE


def test_package_has_a_version() -> None:
    assert __version__ == "0.1.0"


def test_data_file_is_present() -> None:
    assert (DATA_DIR / DATA_FILE).is_file()
