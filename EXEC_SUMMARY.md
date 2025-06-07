# Executive Summary: Current Reimbursement Logic

## Overview

The current system is a **hybrid model** that combines:
- A **pure-Python decision tree** (fit to public data, max depth 6) for most cases.
- A **simple linear formula**: `reimbursement_formula = 60 * days + 0.5 * miles + 0.3 * receipts`
- **Blending and penalties** based on outlier/interview-informed rules.

### Decision Tree
- Predicts reimbursement using splits on days, miles, and receipts, capturing nonlinear and interaction effects from the public data.
- Handles the majority of "in-distribution" cases with high accuracy.

### Blending and Special-Case Logic
- **High receipts (> $1300):** Output is 70% tree, 30% formula (diminishing returns).
- **Very long trips (> 12 days):** Subtract $200 ("vacation penalty").
- **Long trips (≥ 8 days) with high receipts (> $900):** Subtract $100.
- **Very low receipts (< $50) on multi-day trips:** Subtract $50 (penalty for under-reporting).
- **High miles (> 1200):** Output is 70% tree, 30% formula (diminishing returns).
- **All other cases:** Use the tree output.

### Capping for Tree Inputs
- Receipts are capped at $1300 and miles at $1200 for the tree prediction, to avoid extrapolation beyond public data.

---

## Performance
- **Average error:** $115.71
- **Score:** 11,670.80
- **Maximum error:** $927.89
- **Close matches (±$1.00):** 14 out of 1000

This is the best-performing version so far, balancing accuracy for typical cases and robustness for outliers.

---

## Strengths
- **Captures nonlinear and interaction effects** via the decision tree.
- **Handles outliers and edge cases** using interview-informed rules and blending.
- **Avoids overfitting** by capping tree inputs and blending with a simple formula for OOD cases.
- **Interpretable and extensible:** Easy to add more rules or tune existing ones.

---

## Weaknesses / Remaining Issues
- **Some extreme outliers** (very high receipts, long trips) still have high error, but are less frequent.
- **Maximum error** is still significant, but much improved over naive or hard-capped approaches.
- **No explicit handling for rare combinations** (e.g., very high miles + very high receipts + long trip), but these are rare in public data.

---

## Next Steps / Opportunities
- **Further tune blend ratios, penalty amounts, or thresholds** for even better outlier handling.
- **Analyze and hand-tune specific high-error cases** if you want to squeeze out more performance.
- **Try ensemble or nearest-neighbor approaches** for further improvement, if needed.

---

## Summary
Your current approach is a robust, data-driven, and interview-informed hybrid model that achieves strong performance on both average and maximum error, with clear logic for handling outliers and edge cases. It is well-positioned for submission or further incremental improvement. 