# Імпорт необхідних бібліотек
import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import seaborn as sns

# Завантаження стандартизованих даних
df_scaled = pd.read_csv('scaled_data.csv')

# Завантаження оригінального датасету
file_path = 'Mall_Customers.csv'
df = pd.read_csv(file_path)

# Вказати оптимальну кількість кластерів (з попереднього завдання)
optimal_clusters = 5  # Змініть на отримане значення

# Кластеризація методом K-means
kmeans = KMeans(n_clusters=optimal_clusters, random_state=42)
df_scaled['Cluster'] = kmeans.fit_predict(df_scaled)

# Додавання кластерів до оригінального датасету
df['Cluster'] = df_scaled['Cluster']

# Аналіз кластерів: середні значення показників (лише числові колонки)
numerical_columns = ['Age', 'Annual Income (k$)', 'Spending Score (1-100)']  # Вибір числових колонок
cluster_summary = df.groupby('Cluster')[numerical_columns].mean()
print("\nСередні значення показників для кожного кластеру:")
print(cluster_summary)

# Візуалізація кластерів
plt.figure(figsize=(10, 6))
sns.scatterplot(
    x=df_scaled['Annual Income (k$)'], 
    y=df_scaled['Spending Score (1-100)'], 
    hue=df_scaled['Cluster'], 
    palette='Set1', 
    s=100, 
    alpha=0.8
)
plt.title('Кластери клієнтів (K-means)')
plt.xlabel('Annual Income (k$)')
plt.ylabel('Spending Score (1-100)')
plt.legend(title='Кластер')
plt.show()

# Маркетингові стратегії для кожного кластеру (коментарі):
# - Кластер 0: Наприклад, клієнти з високим доходом і низьким Spending Score можуть бути перспективними для преміальних продуктів.
# - Кластер 1: Клієнти з низьким доходом і середнім Spending Score можуть бути чутливими до знижок.
# - Кластер 2: Розробіть стратегію для клієнтів із високим доходом і високим Spending Score — їм можуть підходити ексклюзивні пропозиції.
# - Кластер 3: Молоді клієнти із середнім доходом можуть потребувати більш таргетованого підходу (знижки, акції).
# - Кластер 4: Інші сегменти клієнтів потребують додаткового аналізу для визначення їх потреб.

# Виведення перших кількох рядків із присвоєними кластерами
print("\nДатасет із присвоєними кластерами:")
print(df.head())
