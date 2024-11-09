# Завдання 3: Аналіз t-SNE

import pandas as pd
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt

# Шляхи до вхідного файлу та збереження результатів
input_file_path = 'prepared_data.csv'  # Дані, підготовлені у Завданні 1
output_file_path = 'tsne_transformed_data.csv'  # Результати t-SNE

# Завантаження підготовленого датасету
df = pd.read_csv(input_file_path)

# Вибір числових колонок для t-SNE
numerical_columns = ['Age', 'Annual Income (k$)', 'Spending Score (1-100)']

# Виконання t-SNE
print("Виконується t-SNE...")
tsne = TSNE(n_components=2, perplexity=30, learning_rate=200, random_state=42)
tsne_result = tsne.fit_transform(df[numerical_columns])

# Створення DataFrame для t-SNE результатів
df_tsne = pd.DataFrame(tsne_result, columns=['tSNE1', 'tSNE2'])

# Збереження результатів t-SNE
df_tsne.to_csv(output_file_path, index=False)
print(f"Результати t-SNE збережено у файл {output_file_path}")

# Візуалізація результатів t-SNE
plt.figure(figsize=(8, 6))
plt.scatter(df_tsne['tSNE1'], df_tsne['tSNE2'], alpha=0.7, c='green', edgecolors='k')
plt.title('Візуалізація t-SNE у 2D')
plt.xlabel('tSNE1')
plt.ylabel('tSNE2')
plt.grid(True)
plt.show()
