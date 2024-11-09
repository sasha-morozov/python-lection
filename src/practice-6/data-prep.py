import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder

file_path = 'Mall_Customers.csv'
df = pd.read_csv(file_path)

print("Dataset Shape:", df.shape)
print("First few rows:")
print(df.head())

print("Missing values:")
print(df.isnull().sum())

numerical_columns = ['Age', 'Annual Income (k$)', 'Spending Score (1-100)']
plt.figure(figsize=(15, 5))
for i, col in enumerate(numerical_columns, 1):
    plt.subplot(1, len(numerical_columns), i)
    sns.histplot(df[col], kde=True, bins=20)
    plt.title(f'Distribution of {col}')
plt.tight_layout()
plt.show()

if 'Gender' in df.columns:
    le = LabelEncoder()
    df['Gender'] = le.fit_transform(df['Gender'])
    
prepared_file_path = 'prepared_data.csv'
df.to_csv(prepared_file_path, index=False)
print(f"Prepared data saved to {prepared_file_path}")
