import pandas as pd

# Load your dataset (replace 'your_dataset.csv' with the actual file path)
df = pd.read_csv('/content/diabetes.csv')

# Separate the 'diabetes' column (target variable)
target = df['Glucose']

# Extract only the feature columns from the DataFrame
features = df.drop(columns=['Glucose'])

# Calculate Pearson correlation coefficient
pearson_corr = features.corrwith(target, method='pearson').abs().sort_values(ascending=False)

# Calculate Kendall correlation coefficient
kendall_corr = features.corrwith(target, method='kendall').abs().sort_values(ascending=False)

# Calculate Spearman correlation coefficient
spearman_corr = features.corrwith(target, method='spearman').abs().sort_values(ascending=False)

# Print the results
print("Pearson Correlation:")
print(pearson_corr)

print("\nKendall Correlation:")
print(kendall_corr)

print("\nSpearman Correlation:")
print(spearman_corr)
