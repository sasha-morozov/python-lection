# Завдання 2: PCA (Аналіз головних компонент)

import pandas as pd
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

# Шляхи до вхідного та вихідного файлів
input_file_path = 'prepared_data.csv'  
output_file_path = 'pca_transformed_data.csv'

# Завантаження підготовленого датасету
df = pd.read_csv(input_file_path)

# Вибір числових колонок для PCA
numerical_columns = ['Age', 'Annual Income (k$)', 'Spending Score (1-100)']

# Виконання PCA
pca = PCA()
pca_result = pca.fit_transform(df[numerical_columns])

# Візуалізація частки поясненої дисперсії
explained_variance_ratio = pca.explained_variance_ratio_
plt.figure(figsize=(8, 5))
plt.plot(range(1, len(explained_variance_ratio) + 1), explained_variance_ratio.cumsum(), marker='o', linestyle='--')
plt.xlabel('Кількість головних компонент')
plt.ylabel('Кумулятивна пояснена дисперсія')
plt.title('Пояснена дисперсія для PCA')
plt.show()

# Вибір перших двох компонент для візуалізації
df_pca = pd.DataFrame(pca_result[:, :2], columns=['PC1', 'PC2'])

# Збереження даних після PCA
df_pca.to_csv(output_file_path, index=False)
print(f"Дані після PCA збережено у файл {output_file_path}")

# Візуалізація PCA у 2D
plt.figure(figsize=(8, 6))
plt.scatter(df_pca['PC1'], df_pca['PC2'], alpha=0.7, c='blue', edgecolors='k')
plt.title('Візуалізація PCA у 2D')
plt.xlabel('Головна компонента 1')
plt.ylabel('Головна компонента 2')
plt.grid(True)
plt.show()
