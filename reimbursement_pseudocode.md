# Pseudocode for Legacy Reimbursement Calculation

Inputs:
- trip_duration_days (int)
- miles_traveled (int)
- total_receipts_amount (float)

Output:
- reimbursement_amount (float, rounded to 2 decimals)

---

1. // Per Diem Calculation
   per_diem = 100 * trip_duration_days
   if trip_duration_days == 5:
       per_diem += 50  // 5-day bonus
   if trip_duration_days in [4, 5, 6]:
       per_diem *= 1.05  // sweet spot multiplier
   if trip_duration_days > 7:
       per_diem *= 0.9  // diminishing returns for long trips

2. // Mileage Calculation
   if miles_traveled <= 100:
       mileage = miles_traveled * 0.58
   else:
       mileage = 100 * 0.58 + (miles_traveled - 100) * 0.32
   miles_per_day = miles_traveled / trip_duration_days
   if 180 <= miles_per_day <= 220:
       mileage *= 1.10  // efficiency bonus
   if miles_per_day < 80 or miles_per_day > 300:
       mileage *= 0.9  // penalty for too low/high efficiency

3. // Receipts Calculation
   if total_receipts_amount < 50:
       receipts = total_receipts_amount * 0.5  // penalty for low receipts
   elif total_receipts_amount <= 800:
       receipts = total_receipts_amount * 0.9
   elif total_receipts_amount <= 1500:
       receipts = 800 * 0.9 + (total_receipts_amount - 800) * 0.3
   else:
       receipts = 800 * 0.9 + 700 * 0.3 + (total_receipts_amount - 1500) * 0.1
   if receipts ends with .49 or .99:
       receipts += 2  // rounding bug bonus

4. // Combo Bonuses & Penalties
   if trip_duration_days == 5 and miles_per_day >= 180 and (total_receipts_amount / trip_duration_days) < 100:
       combo_bonus = 50
   else:
       combo_bonus = 0
   if trip_duration_days >= 8 and (total_receipts_amount / trip_duration_days) > 90:
       vacation_penalty = 0.95
   else:
       vacation_penalty = 1
   if miles_per_day >= 180 and (total_receipts_amount / trip_duration_days) < 75:
       high_mileage_low_spending_bonus = 25
   else:
       high_mileage_low_spending_bonus = 0
   if miles_per_day < 80 and (total_receipts_amount / trip_duration_days) > 120:
       low_mileage_high_spending_penalty = 0.95
   else:
       low_mileage_high_spending_penalty = 1

5. // Final Calculation
   total = per_diem + mileage + receipts
   total += combo_bonus + high_mileage_low_spending_bonus
   total *= vacation_penalty
   total *= low_mileage_high_spending_penalty
   reimbursement_amount = round(total, 2)

6. // Data Validation (optional)
   if any input is negative or nonsensical:
       reimbursement_amount = 0 or error

Return reimbursement_amount 