# PRD.md Summary: Business Requirements & System Behaviors

## Business Problem
- ACME Corp relies on a 60-year-old, undocumented travel reimbursement system.
- The system is unpredictable, inconsistent, and sometimes illogical.
- No one fully understands the logic; original engineers and documentation are gone.

## Suspected System Factors
- Reimbursement is believed to depend on:
  - Per diem rules (daily rates)
  - Mileage adjustments (possibly tiered or non-linear)
  - Receipt totals (with caps, diminishing returns, or penalties)
  - Unknown quirks, bugs, or legacy artifacts

## Project Goal
- Faithfully replicate the legacy system's behavior, including any quirks or bugs.
- Output must match the legacy system with high fidelity, even for edge cases.

## System Characteristics
- May include non-linearities, caps, bonuses, penalties, and random/seasonal effects.
- System likely evolved with ad-hoc rules and exceptions over time.
- Multiple calculation paths or clusters may exist based on trip characteristics.

## Evaluation
- Replica will be tested against 1,000 public and 5,000 private cases.
- Success is defined by how closely the outputs match the legacy system.

---

*Use this summary as a reference for algorithm design and implementation.* 