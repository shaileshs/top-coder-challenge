# Mileage Tuning Task List (Temporary)

## 1. Refine the Mileage Rate Drop-Off
- [ ] Replace the flat post-100-mile rate with a sharper drop-off or a curve (logarithmic or square root) for very high mileage.
  - Example: Use `extra_miles ** 0.8 * 0.25` or `math.log1p(extra_miles) * 10` for miles above 100.

## 2. Enhance Efficiency (Miles/Day) Logic
- [ ] Keep the 180-220 miles/day bonus.
- [ ] Add a stronger penalty for extremely high miles/day (e.g., >300).
- [ ] Add a stronger penalty for very low miles/day (e.g., <80).

## 3. Contextual Bonuses/Penalties
- [ ] Increase the bonus for high mileage + low spending.
- [ ] Remove bonuses or add a penalty for high mileage + high spending.

## 4. Multiple Calculation Paths
- [ ] Consider different formulas or bonuses for short, high-mileage trips vs. long, high-mileage trips.
- [ ] Apply more aggressive diminishing returns or caps for long, high-mileage trips.

## 5. Test and Iterate
- [ ] After each change, run the evaluation and check the error on high-mileage cases.
- [ ] Tune exponents, multipliers, and thresholds based on test results.

---

*Check off each item as you implement and test it. Remove this file when tuning is complete.* 