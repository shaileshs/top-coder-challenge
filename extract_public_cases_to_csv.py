import json
import csv

with open('public_cases.json', 'r') as f:
    data = json.load(f)

with open('public_cases.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['trip_duration_days', 'miles_traveled', 'total_receipts_amount', 'expected_output'])
    for case in data:
        inp = case['input']
        writer.writerow([
            inp['trip_duration_days'],
            inp['miles_traveled'],
            inp['total_receipts_amount'],
            case['expected_output']
        ]) 