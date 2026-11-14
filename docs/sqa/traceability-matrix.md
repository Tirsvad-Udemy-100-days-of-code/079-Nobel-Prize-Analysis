# Traceability Matrix

## Metadata
| Key | Value |
| --- | --- |
| ID | TM-001 |
| CrossReference | [BC-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-12 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | [23ad5bb] |
| 2026-11-14 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Added RC-010 (lecture summaries replace Udemy screenshots) | pending |

---

## Purpose

Tracks backward and forward links between artifact instances so that traceability is measurable. A row is added or updated whenever an artifact is created or reviewed.

## Traceability Table

| Artifact Instance | Type | Language | Domain | Upstream (Backward Link) | Downstream (Forward Link) | Last Reviewed (RC-ID) |
| --- | --- | --- | --- | --- | --- | --- |
| [BC-001] | BC | en | it | - | [SA-001], [PP-001] | [RC-001], [RC-010] |
| [SA-001] | SA | en | it | [BC-001] | [PP-001] | [RC-002] |
| [PP-001] | PP | en | it | [BC-001], [SA-001] | [MIL-001], [MIL-002], [MIL-003] | [RC-003], [RC-010] |
| [MIL-001] | MIL | en | it | [PP-001] | [MIL-002] | [RC-004] |
| [MIL-002] | MIL | en | it | [MIL-001] | [MIL-003] | [RC-005] |
| [PY-001] | PY | - | - | [MIL-002] | - | [RC-007] |
| [WIKI-001] | WIKI | en, da, ms | it | [MIL-003] | - | [RC-010], [RC-009], [RC-008] |
| [MIL-003] | MIL | en | it | [MIL-002] | - | [RC-006], [RC-010] |

## Concern Coverage

| Concern (CN-ID) | Views that answer it | Decisions (ADR) | Quality check (TP) | Status |
| --- | --- | --- | --- | --- |
| CN-001 | [MIL-002] | - | - | Covered by plan; verified at the gateway |
| CN-002 | [PP-001] | - | - | Covered by plan; verified at the gateway |
| CN-003 | [MIL-001], [MIL-003] | - | - | Covered by plan; verified at the gateway |
| CN-004 | [MIL-002] | - | - | Covered by plan; verified at the gateway |
| CN-005 | [MIL-001], [MIL-003] | - | - | Covered by plan; verified at the gateway |
| CN-006 | [MIL-001] | - | - | Covered by plan; verified at the gateway |

## Open Inconsistencies

| # | Views | Inconsistency | Found in (RC-ID) | Status | Resolved in |
| --- | --- | --- | --- | --- | --- |
| 1 | - | None found | - | Closed | - |

---

[BC-001]: ../business-case.md
[SA-001]: ../stakeholder-analysis.md
[PP-001]: ../project-plan.md
[MIL-001]: ../milestones/mil-001-foundation.md
[MIL-002]: ../milestones/mil-002-analysis-library.md
[MIL-003]: ../milestones/mil-003-notebook-and-docs.md
[RC-001]: ./reviews/rc-001-business-case.md
[RC-002]: ./reviews/rc-002-stakeholder-analysis.md
[RC-003]: ./reviews/rc-003-project-plan.md
[RC-004]: ./reviews/rc-004-mil-001-foundation.md
[RC-005]: ./reviews/rc-005-mil-002-analysis-library.md
[RC-006]: ./reviews/rc-006-mil-003-notebook-and-docs.md
[RC-007]: ./reviews/rc-007-python-code-mil-002.md
[PY-001]: ../../src/nobel_analysis
[RC-008]: ./reviews/rc-008-wiki.md
[RC-009]: ./reviews/rc-009-wiki-published-check.md
[RC-010]: ./reviews/rc-010-lecture-summaries.md
[WIKI-001]: ../wiki/Home.md
[23ad5bb]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/079-Nobel-Prize-Analysis/commit/23ad5bbc2f45375d6f19cfe3fcb6a3fbe9c9c97b
