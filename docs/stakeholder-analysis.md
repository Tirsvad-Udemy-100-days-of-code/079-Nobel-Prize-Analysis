# Stakeholder Analysis

## Metadata
| Key | Value |
| --- | --- |
| ID | SA-001 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-12 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | pending |

---

## Purpose

This analysis names the people the Nobel Prize analysis project serves, how much power and interest each has, and what each needs from the result. It uses the power/interest grid and maps concerns to FURPS+ attributes.

## Stakeholder Summary Table

| ID | Name | Role/Title | Organization | Power Level | Interest Level | Quadrant | Primary Concern (Business Language) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| S01 | Jens Tirsvad Nielsen | Course participant: Product Owner, developer and reviewer | Tirsvad (private) | HIGH | HIGH | Manage Closely | A correct, finished assignment that is worth sharing |
| S02 | Udemy coursists | Fellow participants of the bootcamp | Udemy (public) | LOW | HIGH | Keep Informed | Readable, runnable code with the assignment's function names, and README instructions to run it |
| S03 | GitHub viewers | Visitors who browse the repository for ideas | GitHub (public) | LOW | MEDIUM | Keep Informed | A clear description, topics and README, and no more runtime dependencies than the charts need |

## Power/Interest Classification Rationale

- **Manage Closely (S01):** decides scope, accepts every plan and owns the repository.
- **Keep Informed (S02, S03):** cannot change the project but judge its usefulness; they are served by documentation, not by consultation.

## Primary Concerns and FURPS+ Mapping

| Concern ID | Stakeholder | Concern | FURPS+ attribute |
| --- | --- | --- | --- |
| CN-001 | S01 | Every assignment question is answered correctly | Functionality |
| CN-002 | S01 | Work follows the plan-first process with traceable reviews | Supportability |
| CN-003 | S02 | Code can be run from the README without guessing | Usability |
| CN-004 | S02 | Function names match the assignment | Usability |
| CN-005 | S03 | The repository explains itself: description, topics, README, wiki | Usability |
| CN-006 | S03 | Few dependencies and no hidden set-up | Supportability |

## Communication Requirements

| ID | Channel | Frequency | Deliverable | Phase / Milestone |
| --- | --- | --- | --- | --- |
| CR-001 | Chat with S01 | At plan acceptance and at the end of the run | Plan dry run and run summary | All milestones |
| CR-002 | README and wiki | Each milestone that changes behaviour | Instructions and explanations | MIL-003 |
| CR-003 | Repository description and topics | Once | Public summary for S02 and S03 | MIL-001 |

## Conflicting Interests and Mitigations

| Conflict | Stakeholders | Mitigation |
| --- | --- | --- |
| S03 wants few dependencies; the charts need Pandas, Plotly, Matplotlib and Seaborn | S03, S01 | Only the libraries the assignment names are runtime dependencies; notebook and test tools are development dependencies |

## Traceability Analysis

### Business Goal Alignment

| Stakeholder | Concern | Business Case objective |
| --- | --- | --- |
| S01 | CN-001, CN-002 | [BC-001] objectives 1 and 3 |
| S02 | CN-003, CN-004 | [BC-001] objectives 2 and 4 |
| S03 | CN-005, CN-006 | [BC-001] objectives 5 and 6 |

## Sign-Off

Accepted by S01 when the plan is accepted in chat; reviewed by the AI as stand-in for S01 (autonomous mode, not independent).

---

[BC-001]: ./business-case.md
