# Algorithm Design for Legacy Reimbursement System (Draft)

## 1. Inputs
- `trip_duration_days` (integer)
- `miles_traveled` (integer)
- `total_receipts_amount` (float)

## 2. Step-by-Step Calculation

### Step 1: Per Diem Calculation
- Set base per diem: `per_diem = 100 * trip_duration_days`
- If `trip_duration_days == 5`, add a bonus (e.g., $50). (Tunable: try $40-$60 based on data)
- If `trip_duration_days` in [4, 5, 6], consider a 'sweet spot' multiplier (e.g., 1.05)
- For trips >7 days, apply a diminishing return (e.g., per_diem *= 0.9)

### Step 2: Mileage Calculation
- If `miles_traveled <= 100`: `mileage = miles_traveled * 0.58`
- If `miles_traveled > 100`: 
    - `mileage = 100 * 0.58 + (miles_traveled - 100) * 0.32` (Tunable: adjust 0.32 based on data)
- Calculate efficiency: `miles_per_day = miles_traveled / trip_duration_days`
- If `180 <= miles_per_day <= 220`, add a bonus (e.g., mileage *= 1.10)
- If `miles_per_day < 80` or `miles_per_day > 300`, apply a penalty (e.g., mileage *= 0.9)

### Step 3: Receipts Calculation
- If `total_receipts_amount < 50`, apply a penalty (e.g., receipts = total_receipts_amount * 0.5)
- If `50 <= total_receipts_amount <= 800`, receipts = total_receipts_amount * 0.9
- If `total_receipts_amount > 800`, receipts = 800 * 0.9 + (total_receipts_amount - 800) * 0.3
- If `total_receipts_amount > 1500`, apply a cap or further diminishing return (e.g., receipts *= 0.8)
- If receipts end in .49 or .99, add a rounding bonus (e.g., +$2)

### Step 4: Bonuses & Penalties (Combinations)
- If `trip_duration_days == 5` and `miles_per_day >= 180` and `total_receipts_amount / trip_duration_days < 100`, add a combo bonus (e.g., +$50)
- If `trip_duration_days >= 8` and `total_receipts_amount / trip_duration_days > 90`, apply a 'vacation penalty' (e.g., total *= 0.95)
- If high mileage and low spending, add a bonus (e.g., +$25)
- If low mileage and high spending, apply a penalty (e.g., total *= 0.95)

### Step 5: Final Calculation
- `total = per_diem + mileage + receipts`
- Apply any bonuses/penalties from Step 4
- Round to 2 decimal places

## 3. Notes & Tunable Parameters
- All constants (rates, bonuses, penalties, thresholds) should be tuned based on public_cases.json for best fit.
- Some randomness/noise may be added for realism, but keep it small (e.g., ±$1).
- Edge cases and bugs (e.g., rounding, small receipts) should be explicitly handled.

---

*This draft algorithm synthesizes business requirements, interview heuristics, and suspected system quirks. Tune and test each step against the data for best results.* 