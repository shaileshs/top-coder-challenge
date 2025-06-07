import sys
import math

# Parse input arguments as floats to handle non-integer values
trip_duration_days = float(sys.argv[1])
miles_traveled = float(sys.argv[2])
total_receipts_amount = float(sys.argv[3])

# 1. Per Diem Calculation
per_diem = 100 * trip_duration_days
if trip_duration_days == 5:
    per_diem += 50  # 5-day bonus
if trip_duration_days in [4, 5, 6]:
    per_diem *= 1.05  # sweet spot multiplier
if trip_duration_days > 7:
    per_diem *= 0.7  # more aggressive diminishing returns for long trips

# 2. Mileage Calculation (hybrid: linear for 100-500, logarithmic above 500)
if miles_traveled <= 100:
    mileage = miles_traveled * 0.58
elif miles_traveled <= 500:
    mileage = 100 * 0.58 + (miles_traveled - 100) * 0.32
else:
    # 100 at high rate, 400 at mid rate, rest at log curve
    extra_miles = miles_traveled - 500
    mileage = 100 * 0.58 + 400 * 0.32 + math.log1p(extra_miles) * 18  # 18 is a tunable factor
miles_per_day = miles_traveled / trip_duration_days if trip_duration_days > 0 else 0
if 180 <= miles_per_day <= 220:
    mileage *= 1.10  # efficiency bonus
if miles_per_day < 80 or miles_per_day > 300:
    mileage *= 0.9  # penalty for too low/high efficiency

# 3. Receipts Calculation (more aggressive diminishing returns)
if total_receipts_amount < 50:
    receipts = total_receipts_amount * 0.5  # penalty for low receipts
elif total_receipts_amount <= 800:
    receipts = total_receipts_amount * 0.8
elif total_receipts_amount <= 1500:
    receipts = 800 * 0.8 + (total_receipts_amount - 800) * 0.15
else:
    receipts = 800 * 0.8 + 700 * 0.15 + (total_receipts_amount - 1500) * 0.05
# Rounding bug: if receipts ends with .49 or .99, add $2
receipts_cents = int(round((total_receipts_amount - int(total_receipts_amount)) * 100))
if receipts_cents == 49 or receipts_cents == 99:
    receipts += 2

# 4. Combo Bonuses & Penalties
combo_bonus = 0
if trip_duration_days == 5 and miles_per_day >= 180 and (total_receipts_amount / trip_duration_days) < 100:
    combo_bonus = 50
vacation_penalty = 1
if trip_duration_days >= 8 and (total_receipts_amount / trip_duration_days) > 90:
    vacation_penalty = 0.95
high_mileage_low_spending_bonus = 0
if miles_per_day >= 180 and (total_receipts_amount / trip_duration_days) < 75:
    high_mileage_low_spending_bonus = 25
low_mileage_high_spending_penalty = 1
if miles_per_day < 80 and (total_receipts_amount / trip_duration_days) > 120:
    low_mileage_high_spending_penalty = 0.95

# 5. Final Calculation
total = per_diem + mileage + receipts
total += combo_bonus + high_mileage_low_spending_bonus
total *= vacation_penalty
total *= low_mileage_high_spending_penalty
reimbursement_amount = round(total, 2)

# 6. Data Validation (optional)
if trip_duration_days < 0 or miles_traveled < 0 or total_receipts_amount < 0:
    reimbursement_amount = 0.00

print(f"{reimbursement_amount:.2f}") 