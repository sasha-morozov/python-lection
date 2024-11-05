import pandas as pd
from sklearn.datasets import fetch_california_housing
import matplotlib.pyplot as plt
import seaborn as sns

# Завантаження датасету California Housing
data = fetch_california_housing(as_frame=True)
df = data.frame

# --- Завдання 1.1 (Провести базовий аналіз даних) ---
# Виведення описової статистики
print("Описова статистика:")
print(df.describe())

# Перевірка на наявність пропущених значень
print("\nПропущені значення в кожній колонці:")
print(df.isnull().sum())

# Визначення типів даних кожної колонки
print("\nТипи даних кожної колонки:")
print(df.dtypes)

# --- Завдання 1.2 (Візуальний аналіз) ---
# Гістограми розподілу
df.hist(bins=30, figsize=(20, 15))
plt.suptitle('Гістограми розподілу для кожної ознаки')
plt.show()

# Індивідуальні boxplot для кожної ознаки
plt.figure(figsize=(20, 40))
for i, column in enumerate(df.columns):
    plt.subplot(5, 2, i + 1)
    sns.boxplot(x=df[column])
    plt.title(f'Boxplot для {column}')
plt.tight_layout()
plt.show()

# Кореляційна матриця та теплова карта
correlation_matrix = df.corr()
plt.figure(figsize=(12, 10))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
plt.title('Теплова карта кореляційної матриці')
plt.show()

# Scatter plots між ціною та іншими ознаками з лініями регресії
target = 'MedHouseVal'
features = [col for col in df.columns if col != target]

plt.figure(figsize=(20, 20))
for i, feature in enumerate(features):
    plt.subplot(4, 2, i + 1)
    sns.regplot(x=df[feature], y=df[target])
    plt.title(f'Scatter plot: {feature} vs {target} (з лінією регресії)')
plt.tight_layout()
plt.show()

# --- Завданя 1.3 (Висновки) ---
# 1. Які ознаки найбільше корелюють з ціною (MedHouseVal):
#    Найсильніша кореляція з ціною спостерігається у ознаки MedInc (медіанний дохід).
# 2. Наявність викидів:
#    Є викиди в деяких ознаках, таких як AveRooms та AveOccup, які можуть вплинути на моделі. Тому їх можна або
#    видалити, або замінити їх середніми значеннями для зменшення впливу.
# 3. Необхідність трансформації даних:
#    Можливо слід розглянути стандартизацію для ознак із великою варіацією значень,
# щоб зробити дані більш підходящими для моделей, що чутливі до масштабу.