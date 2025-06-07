# Edge Cases and Bug Replication Test Cases

## 1. Five-Day Trip Bonus
- Input: 5 days, 100 miles, $500 receipts
  - Edge: Should trigger 5-day bonus

## 2. Sweet Spot Trip Length
- Input: 4 days, 100 miles, $500 receipts
  - Edge: Should be in 'sweet spot' but no 5-day bonus
- Input: 6 days, 100 miles, $500 receipts
  - Edge: Should be in 'sweet spot' but no 5-day bonus

## 3. Long Trip Diminishing Returns
- Input: 10 days, 100 miles, $500 receipts
  - Edge: Should apply diminishing returns for long trips

## 4. Mileage Tier Drop
- Input: 3 days, 99 miles, $100 receipts
  - Edge: All miles at high rate
- Input: 3 days, 101 miles, $100 receipts
  - Edge: 100 miles at high rate, 1 mile at lower rate

## 5. Efficiency Bonus/Penalty
- Input: 2 days, 400 miles, $100 receipts
  - Edge: High miles/day, should check for penalty
- Input: 2 days, 360 miles, $100 receipts
  - Edge: 180 miles/day, should trigger efficiency bonus
- Input: 2 days, 50 miles, $100 receipts
  - Edge: Low miles/day, should check for penalty

## 6. Receipts Diminishing Returns
- Input: 3 days, 100 miles, $30 receipts
  - Edge: Very low receipts, should be penalized
- Input: 3 days, 100 miles, $700 receipts
  - Edge: Medium-high receipts, should be optimal
- Input: 3 days, 100 miles, $2000 receipts
  - Edge: Very high receipts, should be capped/diminished

## 7. Rounding Bug
- Input: 3 days, 100 miles, $99.49 receipts
  - Edge: Receipts end in .49, should trigger rounding bug
- Input: 3 days, 100 miles, $99.99 receipts
  - Edge: Receipts end in .99, should trigger rounding bug

## 8. Combo Bonus
- Input: 5 days, 1000 miles, $400 receipts
  - Edge: 5 days, high miles/day, low spending/day, should trigger combo bonus

## 9. Vacation Penalty
- Input: 9 days, 100 miles, $1000 receipts
  - Edge: Long trip, high spending/day, should trigger vacation penalty

## 10. High Mileage, Low Spending
- Input: 4 days, 800 miles, $100 receipts
  - Edge: High mileage, low spending, should trigger bonus

## 11. Low Mileage, High Spending
- Input: 4 days, 50 miles, $1000 receipts
  - Edge: Low mileage, high spending, should trigger penalty

## 12. Data Type and Value Limits
- Input: 0 days, 0 miles, $0 receipts
  - Edge: All inputs at minimum; should handle gracefully (likely $0 reimbursement or minimum allowed)
- Input: 1 day, 0 miles, $0 receipts
  - Edge: Minimum valid trip duration, no travel or receipts
- Input: 1 day, 1 mile, $0.01 receipts
  - Edge: Smallest positive values for all inputs
- Input: 365 days, 100000 miles, $1000000 receipts
  - Edge: Extremely large values for all inputs; test for overflow or logic errors
- Input: -1 days, 100 miles, $100 receipts
  - Edge: Negative trip duration; should be rejected or handled as invalid
- Input: 3 days, -50 miles, $100 receipts
  - Edge: Negative miles; should be rejected or handled as invalid
- Input: 3 days, 100 miles, -$100 receipts
  - Edge: Negative receipts; should be rejected or handled as invalid
- Input: 3 days, 100 miles, 999999999.99 receipts
  - Edge: Maximum float value for receipts; test for overflow or rounding issues
- Input: 2147483647 days, 2147483647 miles, 2147483647.99 receipts
  - Edge: Maximum 32-bit signed integer values; test for integer overflow
- Input: 3 days, 100 miles, 0.0001 receipts
  - Edge: Very small float for receipts; test for rounding/precision

## 13. Fraud and Abuse Scenarios
- Input: 5 days, 100 miles, $799.99 receipts (repeated 10 times)
  - Edge: Repeated claims at optimal threshold; test for system adaptation or detection
- Input: 3 days, 100 miles, $0 receipts (repeated 10 times)
  - Edge: Repeated minimal claims; test for system stinginess or adaptation
- Input: 10 days, 100 miles, $2000 receipts (repeated 5 times)
  - Edge: Repeated excessive claims; test for capping or penalty escalation
- Input: 2 days, 100 miles, $100 receipts; then 2 days, 100 miles, $2000 receipts (alternating)
  - Edge: Alternating low/high receipts; test for pattern detection or average adjustment
- Input: 3 days, 100 miles, $100 receipts; then 3 days, 100 miles, $1000 receipts; then 3 days, 100 miles, $100 receipts (pattern)
  - Edge: Sandwiching high claim between low claims; test for system "memory"
- Input: 1 day, 1 mile, $0.01 receipts (repeated 100 times)
  - Edge: Micro-claims in bulk; test for anti-abuse measures
- Input: 5 days, 100 miles, $847 receipts
  - Edge: "Magic number" theory; test for folklore-based bonus
- Input: 3 days, 100 miles, $999.99 receipts
  - Edge: Receipts just below a round number; test for rounding or capping behavior

## 14. Interview Rule-Specific Cases
- Input: 5 days, 180 miles, $499 receipts
  - Edge: All three 'combo bonus' conditions met (5 days, 180+ miles/day, <$100/day spending)
- Input: 8 days, 800 miles, $800 receipts
  - Edge: Long trip, high spending/day, should trigger vacation penalty
- Input: 3 days, 100 miles, $50 receipts
  - Edge: Receipts at the lower threshold for penalty
- Input: 3 days, 100 miles, $800 receipts
  - Edge: Receipts at the upper threshold for optimal treatment
- Input: 3 days, 100 miles, $801 receipts
  - Edge: Receipts just above the optimal threshold, should start diminishing returns
- Input: 2 days, 360 miles, $50 receipts
  - Edge: High efficiency, low spending, should maximize bonuses
- Input: 2 days, 50 miles, $800 receipts
  - Edge: Low efficiency, high spending, should maximize penalties
- Input: 5 days, 100 miles, $100 receipts
  - Edge: 5-day trip, low receipts, should test for bonus/penalty interaction
- Input: 5 days, 100 miles, $2000 receipts
  - Edge: 5-day trip, very high receipts, should test for bonus/diminishing returns interaction

---

*Use these cases to test and tune your implementation for edge behaviors, legacy bugs, data type robustness, fraud/abuse resilience, and explicit interview-derived rules.* 