# MIL-002 Analysis library

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-002 |
| CrossReference | [BC-001], [MIL-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-12 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | [23ad5bb] |

---

## Purpose

Decides whether the analysis functions are correct, tested and reviewed against the Python checklist before the notebook and the documentation depend on them.

## Deliverable

The Python package `nobel_analysis` with data loading and cleaning, the analysis functions that carry the assignment's names, chart functions (Plotly, Matplotlib, Seaborn) and a command line entry point, plus a pytest suite that asserts the lecture values. Constants live in `constants.py`; source comments use Doxygen.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | `pytest` passes | All tests pass | Any failure |
| 2 | Tests assert the lecture values (962 rows, 16 columns, first year 1901, last year 2020) | All assertions present and passing | A value is not asserted |
| 3 | Python code reviewed against `QC-PY` and recorded as an RC | Verdict Go | No-Go |
| 4 | opengrep scan reports no findings | 0 findings | Any finding |
| 5 | `mypy --strict` and `ruff check` pass | Exit code 0 | Any error |

## Dependencies

| Depends on | Reason |
| --- | --- |
| [MIL-001] | The package, configuration and data it builds on |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| [BC-001] objectives 1 and 3, success criterion 1 | CN-001, CN-004 |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 |

## Target Date

2026-11-12 — inside the Business Case constraint.

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Implement data loading and cleaning | Read the CSV, convert `birth_date` to datetimes, add `share_pct`, detect duplicates and NaN values (lectures 584). | No |  |
| 2 | Implement category and women functions | Prizes per category and share of women laureates for the bar and donut charts (lecture 585). | No |  |
| 3 | Implement time trend functions | Prizes per year and a 5 year rolling average (lecture 586). | No |  |
| 4 | Implement country functions | Top 20 countries by prizes, prizes per category per country and the ISO data for the choropleth map (lecture 587). | No |  |
| 5 | Implement organisation and city functions | Top 20 organisations and cities, and the country, city and organisation hierarchy for the sunburst chart (lecture 588). | No |  |
| 6 | Implement laureate age functions | Winning age, oldest and youngest laureate, descriptive statistics (lecture 589). | No |  |
| 7 | Implement chart functions | Plotly bar, donut, choropleth and sunburst; Matplotlib trend chart; Seaborn histogram, box plot and lmplot; all return figures so tests run without a display. | No |  |
| 8 | Add command line entry point | `python -m nobel_analysis` prints the answers to the lecture questions. | No |  |
| 9 | Write pytest suite | Assert the lecture values and every function's edge cases; real-value tests skip with a clear reason when the dataset is absent. | No |  |
| 10 | Review code against QC-PY | Review `src/` against `qc-programming-python.md` and record the RC. | No |  |

---

[BC-001]: ../business-case.md
[MIL-001]: ./mil-001-foundation.md
[23ad5bb]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/079-Nobel-Prize-Analysis/commit/23ad5bbc2f45375d6f19cfe3fcb6a3fbe9c9c97b
