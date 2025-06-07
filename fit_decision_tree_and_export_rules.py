import pandas as pd
from sklearn.tree import DecisionTreeRegressor, export_text, plot_tree
import matplotlib.pyplot as plt

# Load data
csv_file = 'public_cases.csv'
df = pd.read_csv(csv_file)
X = df[['trip_duration_days', 'miles_traveled', 'total_receipts_amount']]
y = df['expected_output']

# Fit decision tree
reg = DecisionTreeRegressor(max_depth=4, random_state=42)
reg.fit(X, y)

# Print tree as Python if/else rules
print('--- Decision Tree Rules (max_depth=4) ---')
print(export_text(reg, feature_names=list(X.columns)))

# Plot and save the tree
plt.figure(figsize=(20,10))
plot_tree(reg, feature_names=list(X.columns), filled=True, rounded=True, fontsize=10)
plt.savefig('decision_tree.png')
plt.close()
print('Tree image saved as decision_tree.png')

# Print feature importances
print('--- Feature Importances ---')
for name, importance in zip(X.columns, reg.feature_importances_):
    print(f'{name}: {importance:.3f}') 