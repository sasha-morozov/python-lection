import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.tsa.holtwinters import ExponentialSmoothing
from statsmodels.tsa.arima.model import ARIMA
from sklearn.metrics import mean_squared_error, mean_absolute_error
import os


def create_results_dir():
    """Створює папку для збереження результатів."""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    results_dir = os.path.join(script_dir, 'results')
    os.makedirs(results_dir, exist_ok=True)
    return results_dir


def download_stock_data(symbol, period, results_dir):
    """Завантажує дані акцій і зберігає їх."""
    stock_data = yf.download(symbol, period=period)
    data_file = os.path.join(results_dir, f"{symbol}_data.csv")
    stock_data.to_csv(data_file)
    print(f"Дані збережено у файл: {data_file}")
    return stock_data


def plot_and_save(data, title, xlabel, ylabel, filename, results_dir, *args):
    """Будує графік і зберігає його."""
    plt.figure(figsize=(12, 6))
    for line in args:
        plt.plot(line['data'], label=line['label'], color=line.get('color'))
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.legend()
    plt.grid(True)

    # Зберегти графік
    visual_path = os.path.join(results_dir, filename)
    plt.savefig(visual_path)
    print(f"Графік збережено: {visual_path}")
    plt.show()


def perform_decomposition(data, column, period, results_dir):
    """Виконує декомпозицію та зберігає графіки."""
    result = seasonal_decompose(data[column], model='additive', period=period)
    fig = result.plot()
    fig.set_size_inches(12, 10)

    visual_path = os.path.join(results_dir, f"{column}_decomposition.png")
    plt.savefig(visual_path)
    print(f"Графік декомпозиції збережено: {visual_path}")
    plt.show()
    return result


def save_metrics(metrics, filename, results_dir):
    """Зберігає метрики у текстовий файл."""
    metrics_path = os.path.join(results_dir, filename)
    with open(metrics_path, 'w') as f:
        for key, value in metrics.items():
            f.write(f"{key}: {value}\n")
    print(f"Метрики збережено у файл: {metrics_path}")


def forecast(train, test, horizon, results_dir):
    """Робить прогноз за допомогою Holt-Winters і ARIMA."""
    # Holt-Winters
    hw_model = ExponentialSmoothing(train, trend='add', seasonal=None).fit()
    hw_pred = hw_model.forecast(steps=horizon)

    # ARIMA
    arima_model = ARIMA(train, order=(1, 1, 1)).fit()
    arima_pred = arima_model.forecast(steps=horizon)

    # Метрики
    hw_mse = mean_squared_error(test, hw_pred)
    hw_mae = mean_absolute_error(test, hw_pred)
    arima_mse = mean_squared_error(test, arima_pred)
    arima_mae = mean_absolute_error(test, arima_pred)

    # Збереження метрик
    metrics = {
        "Holt-Winters MSE": hw_mse,
        "Holt-Winters MAE": hw_mae,
        "ARIMA MSE": arima_mse,
        "ARIMA MAE": arima_mae
    }
    save_metrics(metrics, "forecast_metrics.txt", results_dir)

    # Графік прогнозів
    plt.figure(figsize=(12, 5))
    plt.plot(train, label='Train')
    plt.plot(test, label='Test', color='red')
    plt.plot(hw_pred, label='Holt-Winters Forecast', color='yellow')
    plt.plot(arima_pred, label='ARIMA Forecast', color='orange')
    plt.title('Прогноз ціни')
    plt.xlabel('Дата')
    plt.ylabel('Ціна (USD)')
    plt.legend()
    plt.grid(True)

    visual_path = os.path.join(results_dir, 'forecast_comparison.png')
    plt.savefig(visual_path)
    print(f"Графік прогнозів збережено: {visual_path}")
    plt.show()


def main():
    # Налаштування
    stock_symbol = 'MSFT'
    data_period = '1y'
    seasonal_period = 30
    horizon = 30

    # Створення папки для результатів
    results_dir = create_results_dir()

    # Завантаження даних
    stock_data = download_stock_data(stock_symbol, data_period, results_dir)

    # Первинна візуалізація
    plot_and_save(stock_data, f"{stock_symbol} Closing Prices", "Дата", "Ціна (USD)",
                  "closing_prices.png", results_dir, {'data': stock_data['Close'], 'label': 'Close'})

    # Декомпозиція
    stock_data = stock_data.asfreq('B')
    stock_data['Close'] = stock_data['Close'].interpolate()
    perform_decomposition(stock_data, 'Close', seasonal_period, results_dir)

    # Прогнозування
    if not isinstance(stock_data.index, pd.DatetimeIndex):
        stock_data.index = pd.to_datetime(stock_data.index)

    train_data = stock_data['Close'].iloc[:-horizon]
    test_data = stock_data['Close'].iloc[-horizon:]
    forecast(train_data, test_data, horizon, results_dir)


if __name__ == "__main__":
    main()
