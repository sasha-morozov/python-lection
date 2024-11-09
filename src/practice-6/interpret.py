# Завдання 6: Інтерпретація результатів

import pandas as pd

# Шляхи до кластеризованих даних
pca_clustered_file = 'pca_clustered_data.csv'  # Дані після кластеризації PCA
tsne_clustered_file = 'tsne_clustered_data.csv'  # Дані після кластеризації t-SNE

# Завантаження кластеризованих даних
df_pca = pd.read_csv(pca_clustered_file)
df_tsne = pd.read_csv(tsne_clustered_file)

# Інтерпретація кластерів PCA
print("\nІнтерпретація кластерів PCA:")
for cluster in sorted(df_pca['Cluster'].unique()):
    cluster_data = df_pca[df_pca['Cluster'] == cluster]
    print(f"\nКластер {cluster}:")
    print(f"- Розмір: {len(cluster_data)}")
    print(f"- Середні значення:\n{cluster_data.mean()}")

# Інтерпретація кластерів t-SNE
print("\nІнтерпретація кластерів t-SNE:")
for cluster in sorted(df_tsne['Cluster'].unique()):
    cluster_data = df_tsne[df_tsne['Cluster'] == cluster]
    print(f"\nКластер {cluster}:")
    print(f"- Розмір: {len(cluster_data)}")
    print(f"- Середні значення:\n{cluster_data.mean()}")


# Маркетингові стратегії (приклади):
print("\nПропоновані маркетингові стратегії для кожного кластеру:")
print("""
1. Кластер 0: Клієнти з високим доходом і високими витратами. Пропозиції преміальних продуктів або ексклюзивних послуг.
2. Кластер 1: Клієнти з середнім доходом і низькими витратами. Рекламні акції та знижки для залучення уваги.
3. Кластер 2: Молодь із середнім доходом та активними витратами. Рекламувати модні та популярні товари.
4. Кластер 3: Клієнти з низьким доходом і низькими витратами. Таргетування через бюджетні пропозиції.
""")
