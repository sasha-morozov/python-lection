# Завдання 4: Порівняння результатів PCA та t-SNE

import pandas as pd
import matplotlib.pyplot as plt

# Шляхи до вхідних файлів
pca_file_path = 'pca_transformed_data.csv'  # Дані після PCA
tsne_file_path = 'tsne_transformed_data.csv'  # Дані після t-SNE

# Завантаження результатів PCA
df_pca = pd.read_csv(pca_file_path)

# Завантаження результатів t-SNE
df_tsne = pd.read_csv(tsne_file_path)

# Порівняння PCA та t-SNE у візуалізації
plt.figure(figsize=(15, 6))

# PCA Visualization
plt.subplot(1, 2, 1)
plt.scatter(df_pca['PC1'], df_pca['PC2'], alpha=0.7, c='blue', edgecolors='k')
plt.title('PCA Visualization')
plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')
plt.grid(True)

# t-SNE Visualization
plt.subplot(1, 2, 2)
plt.scatter(df_tsne['tSNE1'], df_tsne['tSNE2'], alpha=0.7, c='green', edgecolors='k')
plt.title('t-SNE Visualization')
plt.xlabel('tSNE1')
plt.ylabel('tSNE2')
plt.grid(True)

plt.tight_layout()
plt.show()
