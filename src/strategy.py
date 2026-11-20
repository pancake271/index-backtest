import pandas as pd


def load_prices(path: str) -> pd.Series:
    df = pd.read_csv(path, index_col="Date", parse_dates=True)
    return df["Close"]


def sma_signal(close: pd.Series, window: int = 200) -> pd.Series:
    sma = close.rolling(window).mean()
    return (close > sma).astype(int)


if __name__ == "__main__":
    close = load_prices("data/QQQ.csv")
    signal = sma_signal(close)
    print(signal.tail()) 
    print(signal.value_counts())
    print(signal["2008-09":"2008-12"].mean())