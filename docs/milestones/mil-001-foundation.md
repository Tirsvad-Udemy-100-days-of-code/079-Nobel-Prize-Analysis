# MIL-001 Foundation

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-001 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-12 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | [23ad5bb] |

---

## Purpose

Decides whether the repository is set up well enough to hold code: Python project configuration, ignore rules, the Doxyfile, the source data, set-up instructions and a public description.

## Deliverable

A repository with `pyproject.toml`, a Python `.gitignore`, a `Doxyfile`, the lecture dataset in `data/`, a README skeleton with the `.venv` guide, a clean opengrep scan and a repository description with topics on the git host.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | `pip install -e .[dev]` succeeds in a fresh `.venv` on Python 3.13 | Exit code 0 | Any error |
| 2 | `data/nobel_prize_data.csv` is present | File present | File missing |
| 3 | opengrep scan of the repository reports no findings | 0 findings | Any finding |
| 4 | Repository has a description and at least five topics on the git host | Both set | Either missing |
| 5 | `.env` is ignored by git | `git check-ignore .env` prints it | Not ignored |
| 6 | `doxygen Doxyfile` runs | Exit code 0 | Any error |

## Dependencies

| Depends on | Reason |
| --- | --- |
| none | First gateway |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| [BC-001] objectives 5 and 6, success criteria 5 and 6 | CN-005, CN-006 |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 |

## Target Date

2026-11-12 — inside the Business Case constraint (completion by 2026-11-12).

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Create pyproject.toml | Configure the project for Python 3.13 or newer with the chart libraries as runtime dependencies and pytest, jupyter, ruff and mypy as development extras, so S02 and S03 can install it with one command. | No |  |
| 2 | Add Python .gitignore | Ignore `.venv`, caches, notebook checkpoints, generated docs and `.env`, so secrets and build output never reach the repository. | No |  |
| 3 | Add Doxyfile | Configure Doxygen for the Python sources so the Doxygen comments in `src/` generate documentation. | No |  |
| 4 | Add lecture dataset | Place `nobel_prize_data.csv` in `data/` and record its source in the README, so the analysis runs offline. | No |  |
| 5 | Create package skeleton and smoke test | Add `src/nobel_analysis/__init__.py`, `constants.py` and a first test under `tests/` so the test command runs from the first milestone. | No |  |
| 6 | Write the .venv set-up guide | Document creating and activating `.venv` on Linux and Windows, `python -m pip install --upgrade pip` and installing the project, in the README skeleton built from the framework template. | No |  |
| 7 | Set repository description and topics | Use the git host's API with the repository token from `.env` (never printed) to set the description and topics. | No |  |
| 8 | Run opengrep before pushing | Scan with `~/.opengrep/cli/latest/opengrep.exe` before each push and record the command in the README. | No |  |

---

[BC-001]: ../business-case.md
[23ad5bb]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/079-Nobel_Prize_Analysis/commit/23ad5bbc2f45375d6f19cfe3fcb6a3fbe9c9c97b
