import pandas as pd

from strategy import load_prices, sma_signal


def run_backtest(close: pd.Series, signal: pd.Series) -> pd.DataFrame:
    returns = close.pct_change().fillna(0)
    position = signal.shift(1).fillna(0)
    strat_returns = position * returns

    return pd.DataFrame({
        "position": position,
        "returns": returns,
        "strat_returns": strat_returns,
        "equity_bh": (1 + returns).cumprod(),
        "equity_strat": (1 + strat_returns).cumprod(),
    })


if __name__ == "__main__":
    close = load_prices("data/QQQ.csv")
    signal = sma_signal(close)
    result = run_backtest(close, signal)

    print(result.tail())
    print("B&H final:  ", result["equity_bh"].iloc[-1])
    print("Strat final:", result["equity_strat"].iloc[-1])
    print("Check B&H:  ", close.iloc[-1] / close.iloc[0])