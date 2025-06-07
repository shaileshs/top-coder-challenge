# Rules and Heuristics Derived from Employee Interviews

## 1. Per Diem & Trip Duration
- Base per diem is $100 per day.
- 5-day trips often receive a bonus; 4- or 6-day trips do not.
- The 'sweet spot' for trip length is 4-6 days, which tends to yield higher reimbursements.

## 2. Mileage
- First ~100 miles are reimbursed at a high rate (e.g., $0.58/mile), with a lower rate for additional miles (not linear).
- Efficiency (miles per day):
  - 180-220 miles/day is optimal and rewarded with bonuses.
  - Too high or too low miles/day can result in penalties.
- Mileage bonuses/penalties interact with trip length and spending.

## 3. Receipts
- Receipts are not reimbursed dollar-for-dollar.
- Medium-high receipts ($600-800) are optimal; very high or very low receipts are penalized.
- Submitting small receipts can result in a lower reimbursement than submitting none at all.
- Diminishing returns for high receipt totals.

## 4. Bonuses, Penalties, and Quirks
- Bonus for certain combinations: 5 days, 180+ miles/day, and <$100/day spending.
- Penalty for long trips (8+ days) with high spending ("vacation penalty").
- High mileage with low spending is good; low mileage with high spending is bad.
- Rounding bug: receipts ending in .49 or .99 may get extra money.
- Multiple calculation paths likely exist, depending on trip characteristics.

## 5. Other Factors
- Submission timing (day of week, end of quarter) may have a small effect.
- Spending per day thresholds for bonuses/penalties vary by trip length.
- The system may "remember" user history and adjust generosity (possible adaptive or random component).
- Department or role may influence reimbursement, but not consistently.

---

*These rules are inferred from employee interviews and should guide the design of your reimbursement algorithm. Some rules may interact or have exceptions, so further data analysis is recommended for precise modeling.* 