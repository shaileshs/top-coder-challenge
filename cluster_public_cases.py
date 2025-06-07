import json
from collections import defaultdict
import sys

# Load public cases
def load_cases(filename):
    with open(filename, 'r') as f:
        return json.load(f)

# Simple binning function
def get_trip_bin(days):
    if days == 5:
        return 'ideal'
    elif days <= 3:
        return 'short'
    elif 4 <= days <= 6:
        return 'sweet_spot'
    elif days == 7:
        return 'medium'
    elif 8 <= days <= 11:
        return 'long'
    else:
        return 'very_long'

def get_miles_bin(miles, days):
    miles_per_day = miles / days if days > 0 else 0
    if 180 <= miles_per_day <= 220:
        return 'ideal'
    elif miles < 100:
        return 'low'
    elif miles <= 700:
        return 'medium'
    elif miles <= 1100:
        return 'high'
    else:
        return 'super_high'

def get_receipts_bin(receipts):
    if 600 <= receipts <= 800:
        return 'ideal'
    elif receipts < 200:
        return 'low'
    elif receipts <= 800:
        return 'medium'
    elif receipts <= 1800:
        return 'high'
    else:
        return 'super_high'

# Cluster and summarize
def cluster_cases(cases):
    clusters = defaultdict(list)
    for case in cases:
        inp = case['input']
        out = case['expected_output']
        trip_bin = get_trip_bin(inp['trip_duration_days'])
        miles_bin = get_miles_bin(inp['miles_traveled'], inp['trip_duration_days'])
        receipts_bin = get_receipts_bin(inp['total_receipts_amount'])
        key = (trip_bin, miles_bin, receipts_bin)
        clusters[key].append((inp['trip_duration_days'], inp['miles_traveled'], inp['total_receipts_amount'], out))
    return clusters

def print_cluster_stats(clusters):
    for key, cases in clusters.items():
        n = len(cases)
        avg_days = sum(c[0] for c in cases) / n
        avg_miles = sum(c[1] for c in cases) / n
        avg_receipts = sum(c[2] for c in cases) / n
        avg_output = sum(c[3] for c in cases) / n
        print(f"Cluster {key}: {n} cases")
        print(f"  Avg days: {avg_days:.2f}, Avg miles: {avg_miles:.2f}, Avg receipts: {avg_receipts:.2f}, Avg output: {avg_output:.2f}")
        print()

def print_distributions(cases):
    days = [case['input']['trip_duration_days'] for case in cases]
    miles = [case['input']['miles_traveled'] for case in cases]
    receipts = [case['input']['total_receipts_amount'] for case in cases]
    
    def describe(arr, label):
        arr_sorted = sorted(arr)
        n = len(arr_sorted)
        def pct(p):
            return arr_sorted[int(p * n)]
        print(f"{label}:")
        print(f"  Min: {arr_sorted[0]:.2f}")
        print(f"  25th pct: {pct(0.25):.2f}")
        print(f"  Median: {pct(0.5):.2f}")
        print(f"  75th pct: {pct(0.75):.2f}")
        print(f"  Max: {arr_sorted[-1]:.2f}")
        print(f"  Mean: {sum(arr_sorted)/n:.2f}\n")
    
    describe(days, "Trip Duration (days)")
    describe(miles, "Miles Traveled")
    describe(receipts, "Total Receipts Amount")

def fit_linear_formula(cluster_cases):
    # Fit output = a*days + b*miles + c*receipts + d using least squares
    # Only standard library
    n = len(cluster_cases)
    if n < 2:
        return None
    X = []
    Y = []
    for days, miles, receipts, out in cluster_cases:
        X.append([days, miles, receipts, 1])
        Y.append(out)
    # Compute X^T X and X^T Y
    XT = list(zip(*X))
    XTX = [[sum(xi * xj for xi, xj in zip(rowi, rowj)) for rowj in XT] for rowi in XT]
    XTY = [sum(xi * yi for xi, yi in zip(col, Y)) for col in XT]
    # Solve XTX * beta = XTY for beta (a, b, c, d)
    # Use Cramer's rule for 4x4 system
    def det4(m):
        from itertools import permutations
        idx = [0,1,2,3]
        return sum(((-1)**(i+j) * m[0][i] * m[1][j%4] * m[2][(j+1)%4] * m[3][(j+2)%4]) for i in idx for j in idx) / 24
    def replace_col(m, col, v):
        return [row[:col] + [v[i]] + row[col+1:] for i, row in enumerate(m)]
    D = det4(XTX)
    if abs(D) < 1e-8:
        return None
    betas = []
    for i in range(4):
        Di = det4(replace_col(XTX, i, XTY))
        betas.append(Di / D)
    return betas

def print_best_formulas(clusters):
    print("\nBest-fit linear weights for large clusters (40+ cases):")
    for key, cases in clusters.items():
        if len(cases) >= 40:
            weights = fit_linear_formula(cases)
            if weights:
                a, b, c, d = weights
                print(f"  Cluster {key} (n={len(cases)}): output = {a:.2f}*days + {b:.4f}*miles + {c:.4f}*receipts + {d:.2f}")
            else:
                print(f"  Cluster {key} (n={len(cases)}): Could not fit formula.")

def main():
    cases = load_cases('public_cases.json')
    print_distributions(cases)
    clusters = cluster_cases(cases)
    print_cluster_stats(clusters)
    print_best_formulas(clusters)

if __name__ == '__main__':
    main() 