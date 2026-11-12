"""!
@file cli.py
@brief Presentation and composition root: print the report for the bundled data.
"""

from pathlib import Path

from nobel_analysis.application.cleaning import clean
from nobel_analysis.application.report import build_report
from nobel_analysis.infrastructure.data import load_nobel


def main(data_dir: Path | None = None) -> int:
    """!
    @brief Load and clean the data set and print the report.
    @param data_dir Folder with the CSV file; the bundled `data/` when omitted.
    @return The process exit code, 0 on success.
    """
    print(build_report(clean(load_nobel(data_dir))))
    return 0
