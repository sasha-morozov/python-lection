# Завдання 5: Кластеризація на даних після PCA та t-SNE

import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Шляхи до вхідних файлів
pca_file_path = 'pca_transformed_data.csv'  # Дані після PCA
tsne_file_path = 'tsne_transformed_data.csv'  # Дані після t-SNE

# Завантаження результатів PCA
df_pca = pd.read_csv(pca_file_path)

# Завантаження результатів t-SNE
df_tsne = pd.read_csv(tsne_file_path)

# Виконання кластеризації методом K-means для PCA
print("Виконується кластеризація для PCA...")
kmeans_pca = KMeans(n_clusters=3, random_state=42)
df_pca['Cluster'] = kmeans_pca.fit_predict(df_pca)

# Виконання кластеризації методом K-means для t-SNE
print("Виконується кластеризація для t-SNE...")
kmeans_tsne = KMeans(n_clusters=3, random_state=42)
df_tsne['Cluster'] = kmeans_tsne.fit_predict(df_tsne)

# Візуалізація кластеризації на PCA
plt.figure(figsize=(15, 6))

# PCA Clustering
plt.subplot(1, 2, 1)
plt.scatter(df_pca['PC1'], df_pca['PC2'], c=df_pca['Cluster'], cmap='viridis', alpha=0.7, edgecolors='k')
plt.title('Кластеризація на даних PCA')
plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')
plt.grid(True)

# t-SNE Clustering
plt.subplot(1, 2, 2)
plt.scatter(df_tsne['tSNE1'], df_tsne['tSNE2'], c=df_tsne['Cluster'], cmap='viridis', alpha=0.7, edgecolors='k')
plt.title('Кластеризація на даних t-SNE')
plt.xlabel('tSNE1')
plt.ylabel('tSNE2')
plt.grid(True)

plt.tight_layout()
plt.show()

# Збереження результатів кластеризації
df_pca.to_csv('pca_clustered_data.csv', index=False)
df_tsne.to_csv('tsne_clustered_data.csv', index=False)
