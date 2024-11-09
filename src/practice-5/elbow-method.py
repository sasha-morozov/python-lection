# Імпорт необхідних бібліотек
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
import matplotlib.pyplot as plt

# Завантаження стандартизованих даних
df_scaled = pd.read_csv('scaled_data.csv')

# Метод ліктя (Elbow Method)
def elbow_method(data, max_clusters=10):
    inertia = []
    for k in range(1, max_clusters + 1):
        kmeans = KMeans(n_clusters=k, random_state=42)
        kmeans.fit(data)
        inertia.append(kmeans.inertia_)
    
    # Побудова графіка
    plt.figure(figsize=(8, 5))
    plt.plot(range(1, max_clusters + 1), inertia, marker='o', linestyle='--')
    plt.xlabel('Кількість кластерів')
    plt.ylabel('Інерція')
    plt.title('Метод ліктя')
    plt.show()

# Розрахунок коефіцієнта силуету
def silhouette_analysis(data, max_clusters=10):
    silhouette_scores = []
    for k in range(2, max_clusters + 1):  # Silhouette Score недоступний для k=1
        kmeans = KMeans(n_clusters=k, random_state=42)
        labels = kmeans.fit_predict(data)
        score = silhouette_score(data, labels)
        silhouette_scores.append(score)
    
    # Побудова графіка
    plt.figure(figsize=(8, 5))
    plt.plot(range(2, max_clusters + 1), silhouette_scores, marker='o', linestyle='--', color='green')
    plt.xlabel('Кількість кластерів')
    plt.ylabel('Коефіцієнт силуету')
    plt.title('Silhouette Analysis')
    plt.show()
    return silhouette_scores

# Виконання аналізу
print("Виконується метод ліктя...")
elbow_method(df_scaled)

print("Виконується Silhouette Analysis...")
silhouette_scores = silhouette_analysis(df_scaled)

# Пошук оптимальної кількості кластерів
optimal_clusters = 2 + silhouette_scores.index(max(silhouette_scores))
print(f"\nОптимальна кількість кластерів: {optimal_clusters}")
