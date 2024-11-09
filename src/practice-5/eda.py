import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler

file_path = 'Mall_Customers.csv'
df = pd.read_csv(file_path)

# Первинний аналіз даних
print("Розмір датасету:", df.shape)
print("\nПерші кілька рядків датасету:")
print(df.head())
print("\nТипи даних:")
print(df.dtypes)
print("\nОписова статистика:")
print(df.describe())

# Перевірка на пропущені значення
missing_values = df.isnull().sum()
print("\nКількість пропущених значень у кожній колонці:")
print(missing_values)

# Побудова гістограм для кожної змінної
columns_to_plot = ['Age', 'Annual Income (k$)', 'Spending Score (1-100)']  # Основні числові ознаки
plt.figure(figsize=(15, 5))
for i, col in enumerate(columns_to_plot, 1):
    plt.subplot(1, len(columns_to_plot), i)
    sns.histplot(df[col], kde=True, bins=20, color='blue')
    plt.title(f'Розподіл {col}')
plt.tight_layout()
plt.show()

# Стандартизація даних
scaler = StandardScaler()
numerical_features = ['Age', 'Annual Income (k$)', 'Spending Score (1-100)']
df_scaled = scaler.fit_transform(df[numerical_features])
df_scaled = pd.DataFrame(df_scaled, columns=numerical_features)

# Збереження стандартизованих даних у файл
df_scaled.to_csv('scaled_data.csv', index=False)
print("Стандартизовані дані збережені у файл 'scaled_data.csv'")

print("\nПерші кілька рядків стандартизованих даних:")
print(df_scaled.head())
