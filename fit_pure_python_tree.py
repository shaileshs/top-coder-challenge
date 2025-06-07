import csv
import math

# Load data
with open('public_cases.csv', 'r') as f:
    reader = csv.DictReader(f)
    data = [
        {
            'trip_duration_days': float(row['trip_duration_days']),
            'miles_traveled': float(row['miles_traveled']),
            'total_receipts_amount': float(row['total_receipts_amount']),
            'expected_output': float(row['expected_output'])
        }
        for row in reader
    ]

features = ['trip_duration_days', 'miles_traveled', 'total_receipts_amount']

# Helper: compute mean squared error for a split
def mse(groups):
    total = sum(len(g) for g in groups)
    return sum(
        sum((row['expected_output'] - (sum(r['expected_output'] for r in g) / len(g))) ** 2 for row in g)
        for g in groups if len(g) > 0
    ) / total

# Find the best split for a dataset
def best_split(rows):
    best_feature, best_thresh, best_score, best_groups = None, None, float('inf'), None
    for feature in features:
        values = sorted(set(row[feature] for row in rows))
        for i in range(1, len(values)):
            thresh = (values[i-1] + values[i]) / 2
            left = [row for row in rows if row[feature] <= thresh]
            right = [row for row in rows if row[feature] > thresh]
            if not left or not right:
                continue
            score = mse([left, right])
            if score < best_score:
                best_feature, best_thresh, best_score, best_groups = feature, thresh, score, (left, right)
    return best_feature, best_thresh, best_groups

# Recursively build the tree
def build_tree(rows, depth, max_depth):
    if depth == max_depth or len(rows) < 10:
        mean_val = sum(row['expected_output'] for row in rows) / len(rows)
        return {'type': 'leaf', 'value': mean_val}
    feature, thresh, groups = best_split(rows)
    if feature is None:
        mean_val = sum(row['expected_output'] for row in rows) / len(rows)
        return {'type': 'leaf', 'value': mean_val}
    left = build_tree(groups[0], depth+1, max_depth)
    right = build_tree(groups[1], depth+1, max_depth)
    return {'type': 'node', 'feature': feature, 'thresh': thresh, 'left': left, 'right': right}

# Print the tree as Python if/else code
def print_tree(node, indent='    '):
    def _print(node, level):
        pad = indent * level
        if node['type'] == 'leaf':
            print(f"{pad}return {node['value']:.2f}")
        else:
            print(f"{pad}if {node['feature']} <= {node['thresh']:.2f}:")
            _print(node['left'], level+1)
            print(f"{pad}else:")
            _print(node['right'], level+1)
    print('def decision_tree_predict(trip_duration_days, miles_traveled, total_receipts_amount):')
    _print(node, 1)

# Build and print the tree
tree = build_tree(data, 0, 6)
print_tree(tree) 