# --- Завдання 2, 3, 4, 5 (Створення вибіркових данних, побудова, оцінка моделей, функція для пргнозування цін)
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression, Lasso, Ridge
from sklearn.metrics import mean_squared_error, r2_score
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import joblib

# --- Завдання 2 ---
def prepare_data(file_path, test_size=0.2, random_state=42, scaler_filename='standard_scaler.pkl'):
    df = pd.read_csv(file_path)
    X = df.drop(columns='MedHouseVal')
    y = df['MedHouseVal']
    
    # Розділення на тренувальну та тестову вибірки
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state)
    
    # Масштабування даних за допомогою StandardScaler
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    # Збереження скейлера
    joblib.dump(scaler, scaler_filename)
    
    # Збереження підготовлених даних у файли
    joblib.dump(X_train_scaled, 'X_train_scaled.pkl')
    joblib.dump(X_test_scaled, 'X_test_scaled.pkl')
    joblib.dump(y_train, 'y_train.pkl')
    joblib.dump(y_test, 'y_test.pkl')
    
    print("Дані успішно підготовлені та збережені у файли.")
    
    return X_train_scaled, X_test_scaled, y_train, y_test
# --- Завдання 2 ---

def adjusted_r2_score(r2, n, p):
    return 1 - ((1 - r2) * (n - 1)) / (n - p - 1)

def visualize_results(y_test, y_pred, title):
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x=y_test, y=y_pred, alpha=0.6)
    plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--', lw=2)
    plt.title(f'{title}: Прогнозовані vs Реальні значення')
    plt.xlabel('Реальні значення')
    plt.ylabel('Прогнозовані значення')
    plt.show()

    # Графік залишків
    residuals = y_test - y_pred
    plt.figure(figsize=(10, 6))
    sns.histplot(residuals, kde=True, bins=30, color='blue')
    plt.title(f'{title}: Розподіл залишків')
    plt.xlabel('Залишки')
    plt.ylabel('Частота')
    plt.show()

# --- Завдання 3 і 4 ---
def simple_linear_regression(X_train, X_test, y_train, y_test, feature_index, target='MedHouseVal'):
    X_train_simple = X_train[:, [feature_index]]
    X_test_simple = X_test[:, [feature_index]]
    
    model = LinearRegression()
    model.fit(X_train_simple, y_train)
    
    joblib.dump(model, 'simple_linear_model.pkl')
    
    y_pred = model.predict(X_test_simple)
    
    # Розрахунок метрик
    mse = mean_squared_error(y_test, y_pred)
    rmse = np.sqrt(mse)
    r2 = r2_score(y_test, y_pred)
    adj_r2 = adjusted_r2_score(r2, X_test.shape[0], 1)  # 1 ознака
    
    print(f"\nМетрики для простої лінійної регресії:")
    print(f"Mean Squared Error (MSE): {mse:.4f}")
    print(f"Root Mean Squared Error (RMSE): {rmse:.4f}")
    print(f"R-squared (R²): {r2:.4f}")
    print(f"Adjusted R-squared: {adj_r2:.4f}")
    
    # Візуалізація результатів
    visualize_results(y_test, y_pred, 'Проста лінійна регресія')
    
    return y_pred

def multiple_linear_regression(X_train, X_test, y_train, y_test, feature_names):
    model = LinearRegression()
    model.fit(X_train, y_train)
    
    joblib.dump(model, 'multiple_linear_model.pkl')
    
    y_pred = model.predict(X_test)
    
    # Розрахунок метрик
    mse = mean_squared_error(y_test, y_pred)
    rmse = np.sqrt(mse)
    r2 = r2_score(y_test, y_pred)
    adj_r2 = adjusted_r2_score(r2, X_test.shape[0], X_test.shape[1])
    
    print("\nМетрики для множинної лінійної регресії:")
    print(f"Mean Squared Error (MSE): {mse:.4f}")
    print(f"Root Mean Squared Error (RMSE): {rmse:.4f}")
    print(f"R-squared (R²): {r2:.4f}")
    print(f"Adjusted R-squared: {adj_r2:.4f}")
    
    # Аналіз коефіцієнтів
    coef_df = pd.DataFrame(model.coef_, index=feature_names, columns=['Коефіцієнти'])
    print("\nКоефіцієнти моделі:")
    print(coef_df)
    
    # Візуалізація результатів
    visualize_results(y_test, y_pred, 'Множинна лінійна регресія')
    
    return y_pred, coef_df

def optimized_model(X_train, X_test, y_train, y_test, feature_names, alpha=0.1, regularization='lasso'):
    if regularization == 'lasso':
        model = Lasso(alpha=alpha)
    elif regularization == 'ridge':
        model = Ridge(alpha=alpha)
    else:
        raise ValueError("Невірний тип регуляризації. Використовуйте 'lasso' або 'ridge'.")
    
    model.fit(X_train, y_train)
    
    joblib.dump(model, f'optimized_model_{regularization}.pkl')
    
    y_pred = model.predict(X_test)
    
    # Розрахунок метрик
    mse = mean_squared_error(y_test, y_pred)
    rmse = np.sqrt(mse)
    r2 = r2_score(y_test, y_pred)
    adj_r2 = adjusted_r2_score(r2, X_test.shape[0], X_test.shape[1])
    
    print(f"\nМетрики для оптимізованої моделі ({regularization}):")
    print(f"Mean Squared Error (MSE): {mse:.4f}")
    print(f"Root Mean Squared Error (RMSE): {rmse:.4f}")
    print(f"R-squared (R²): {r2:.4f}")
    print(f"Adjusted R-squared: {adj_r2:.4f}")
    
    # Аналіз коефіцієнтів
    coef_df = pd.DataFrame(model.coef_, index=feature_names, columns=['Коефіцієнти'])
    print(f"\nКоефіцієнти оптимізованої моделі ({regularization}):")
    print(coef_df)
    
    # Візуалізація результатів
    visualize_results(y_test, y_pred, f'Оптимізована модель ({regularization})')
    
    return y_pred, coef_df
# --- Завдання 3 і 4 ---

# --- Завдання 5 ---
def predict_price(input_features, model_filename='optimized_model_lasso.pkl', scaler_filename='standard_scaler.pkl'):
    model = joblib.load(model_filename)
    scaler = joblib.load(scaler_filename)
    
    input_features_scaled = scaler.transform([input_features])
    
    predicted_price = model.predict(input_features_scaled)[0]
    
    return predicted_price
# --- Завдання 5 ---

# Головний блок виконання
if __name__ == "__main__":
    # Підготовка даних (Завдання 2)
    X_train_scaled, X_test_scaled, y_train, y_test = prepare_data('california_housing.csv')
    feature_names = pd.read_csv('california_housing.csv').drop(columns='MedHouseVal').columns
    
    # Побудова і оцінка простої лінійної регресії (Завдання 3 і 4)
    feature_index = 0  # Використовуємо найбільш корельовану ознаку
    y_pred_simple = simple_linear_regression(X_train_scaled, X_test_scaled, y_train, y_test, feature_index)
    
    # Побудова і оцінка множинної лінійної регресії (Завдання 3 і 4)
    y_pred_multiple, coef_df_multiple = multiple_linear_regression(X_train_scaled, X_test_scaled, y_train, y_test, feature_names)
    
    # Побудова і оцінка оптимізованої моделі (Завдання 3 і 4)
    y_pred_optimized, coef_df_optimized = optimized_model(X_train_scaled, X_test_scaled, y_train, y_test, feature_names, alpha=0.1, regularization='lasso')

    # Прогнозування ціни на основі характеристики даних і висновки (Завдання 5)
    example_features = [
      5.0,     # MedInc (медіанний дохід району в десятках тисяч доларів)
      30.0,    # HouseAge (середній вік будинків у районі)
      5.5,     # AveRooms (середня кількість кімнат)
      1.0,     # AveBedrms (середня кількість спалень)
      1000.0,  # Population (населення району)
      3.0,     # AveOccup (середня кількість мешканців на одну житлову одиницю)
      34.0,    # Latitude (широта)
      -118.0   # Longitude (довгота)
    ]
    predicted_price = predict_price(example_features)
    print(f"\nПрогнозована ціна для прикладних характеристик: ${predicted_price:.2f}")

  
# - Проста лінійна регресія допомагає побачити, як одна найважливіша ознака впливає на цільову змінну, але її точність обмежена,
#   бо вона не враховує всі інші фактори.
# - Множинна лінійна регресія дозволяє використовувати всі ознаки, тому модель краще підходить для прогнозування.
#   Але бувають проблеми з тим, що деякі ознаки можуть бути дуже схожими між собою, і це впливає на модель.
# - Регуляризація (Lasso, Ridge) допомагає зробити модель більш стійкою, щоб вона не переобучалась. Lasso може навіть прибрати
#   ознаки, які майже не впливають на результат, а Ridge зменшує їх вагу, але не прибирає.
# - Лінійні моделі не завжди справляються з дуже складними зв'язками між ознаками, тому іноді краще використовувати складніші моделі,
#   наприклад, Random Forest або нейронні мережі.
# - Залишки (різниця між реальними та передбаченими значеннями) мають бути розподілені рівномірно. Якщо це не так, можливо, потрібно
#   переглянути ознаки або зробити їхні перетворення.
# - Щоб покращити модель, можна спробувати додати нові ознаки або застосувати інші методи обробки даних.

