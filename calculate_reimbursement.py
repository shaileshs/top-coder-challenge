import sys
import random

trip_duration_days = float(sys.argv[1])
miles_traveled = float(sys.argv[2])
total_receipts_amount = float(sys.argv[3])

# 3 bins for each input (adjusted for sweet spot)
def bin_trip_days(days):
    if days <= 3:
        return 'short'
    elif days <= 6:
        return 'medium'  # sweet spot: 4-6 days
    else:
        return 'long'

def bin_miles(miles):
    if miles <= 200:
        return 'low'
    elif miles <= 600:
        return 'medium'
    else:
        return 'high'

def bin_receipts(receipts):
    if receipts <= 400:
        return 'low'
    elif receipts <= 900:
        return 'medium'
    else:
        return 'high'

# Simple formula (base weights, can be tuned)
def simple_formula(days, miles, receipts):
    # Per diem: $100/day, but adjust for bins
    day_bin = bin_trip_days(days)
    if day_bin == 'short':
        per_diem = 90 * days
    elif day_bin == 'medium':
        per_diem = 115 * days  # sweet spot bonus baked in
    else:
        per_diem = 95 * days

    # Mileage: diminishing returns
    mile_bin = bin_miles(miles)
    if mile_bin == 'low':
        mileage_amt = miles * 0.58
    elif mile_bin == 'medium':
        mileage_amt = 100 * 0.58 + (miles - 100) * 0.35
    else:
        mileage_amt = 100 * 0.58 + 500 * 0.35 + (miles - 600) * 0.15

    # Receipts: diminishing returns
    receipt_bin = bin_receipts(receipts)
    if receipt_bin == 'low':
        receipts_amt = receipts * 0.25
    elif receipt_bin == 'medium':
        receipts_amt = 400 * 0.25 + (receipts - 400) * 0.15
    else:
        receipts_amt = 400 * 0.25 + 500 * 0.15 + (receipts - 900) * 0.05

    return per_diem + mileage_amt + receipts_amt

reimbursement_amount = simple_formula(trip_duration_days, miles_traveled, total_receipts_amount)

# 1. Sweet spot bonus for 4-6 day trips
day_bin = bin_trip_days(trip_duration_days)
if day_bin == 'medium':
    reimbursement_amount += 50

# 2. Receipts: penalty for very low receipts (<$50) on multi-day trips
if total_receipts_amount < 50 and trip_duration_days > 1:
    reimbursement_amount -= 50

# 2. Receipts: bonus for receipts in $600–800 range
if 600 <= total_receipts_amount <= 800:
    reimbursement_amount += 50

# 3. Mileage/Spending: bonus/penalty for high/low mileage + low/high spending
mpd = miles_traveled / trip_duration_days if trip_duration_days > 0 else 0
spending_per_day = total_receipts_amount / trip_duration_days if trip_duration_days > 0 else 0
if mpd > 180 and spending_per_day < 100:
    reimbursement_amount += 50
if mpd < 120 and spending_per_day > 120:
    reimbursement_amount -= 50

# 4. Efficiency penalty scales with distance from optimal (180-220 mpd)
if mpd < 180:
    reimbursement_amount -= min(50, (180 - mpd) * 0.5)
elif mpd > 220:
    reimbursement_amount -= min(50, (mpd - 220) * 0.5)
else:
    reimbursement_amount += 25  # small bonus for being in the optimal range

# Vacation penalty: nuanced for long trips (8+ days) with high spending (receipts > $900)
vacation_penalty = 0
if trip_duration_days >= 8 and total_receipts_amount > 900:
    if trip_duration_days <= 10:
        vacation_penalty = 0.4 * (total_receipts_amount - 900)
    else:
        vacation_penalty = 0.7 * (total_receipts_amount - 900)
    vacation_penalty = min(vacation_penalty, 600)
    reimbursement_amount -= vacation_penalty
    if mpd > 180 and spending_per_day < 100:
        reimbursement_amount += 50
    if reimbursement_amount < 200:
        reimbursement_amount = 200

# 5. Rounding bug: receipts ending in .49 or .99 get extra $10
if str(total_receipts_amount).endswith('.49') or str(total_receipts_amount).endswith('.99'):
    reimbursement_amount += 10

# 6. Small random quirk: for edge cases, add or subtract $5 (simulate system quirk)
if int(trip_duration_days) == 7 and int(miles_traveled) % 7 == 0:
    reimbursement_amount += random.choice([-5, 0, 5])

print(f"{reimbursement_amount:.2f}") 