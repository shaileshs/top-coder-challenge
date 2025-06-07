# INTERVIEWS.md Summary: Employee Insights & System Quirks

## General Observations
- The system is unpredictable and inconsistent; similar trips can yield very different reimbursements.
- Employees have many theories, but no one fully understands the logic.

## Per Diem & Trip Duration
- $100/day is a common base per diem.
- 5-day trips often get a bonus; 4- or 6-day trips do not.
- There is a 'sweet spot' for trip length (4-6 days) with better reimbursements.

## Mileage
- First ~100 miles reimbursed at a high rate (e.g., $0.58/mile), then the rate drops (not linearly).
- High miles per day (180-220) are rewarded; too high or too low can be penalized.
- Mileage bonuses/penalties interact with trip length and spending.

## Receipts
- Receipts are not reimbursed dollar-for-dollar.
- Medium-high receipts ($600-800) get the best treatment; very high or very low receipts are penalized.
- Submitting small receipts can result in a lower reimbursement than submitting none.
- Diminishing returns for high receipt totals.

## Bonuses, Penalties, and Quirks
- Certain combinations (e.g., 5 days, 180+ miles/day, <$100/day spending) trigger bonuses.
- Long trips with high spending are penalized ("vacation penalty").
- High mileage with low spending is good; low mileage with high spending is bad.
- Rounding bug: receipts ending in .49 or .99 may get extra money.
- There may be intentional randomness or noise (possibly tied to submission day, lunar cycles, etc.).
- Multiple calculation paths likely exist, depending on trip characteristics.

## Other Factors
- Submission timing (day of week, end of quarter) may have a small effect.
- Spending per day thresholds for bonuses/penalties vary by trip length.
- The system may "remember" user history and adjust generosity.
- Department or role may influence reimbursement, but not consistently.

---

*Use this summary as a reference for identifying rules, edge cases, and quirks in your algorithm design.* 