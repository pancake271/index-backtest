import argparse
from pathlib import Path
import yfinance as yf


def download(ticker: str, start: str, out_dir: Path) -> Path:
    df = yf.download(ticker, start=start, auto_adjust=True,
                     multi_level_index=False, progress=False)
    if df.empty:
        raise ValueError(f"No data for {ticker}")
    out_dir.mkdir(parents=True, exist_ok=True)
    path = out_dir / f"{ticker.replace('^', '')}.csv"
    df.to_csv(path)
    return path


if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--ticker", default="QQQ")
    p.add_argument("--start", default="1999-03-10")
    args = p.parse_args()
    print(download(args.ticker, args.start, Path("data")))