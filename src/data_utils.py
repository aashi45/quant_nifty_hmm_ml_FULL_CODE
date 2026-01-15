
import pandas as pd
import numpy as np

def calculate_atm(price, step=50):
    return int(round(price / step) * step)

def clean_timeseries(df: pd.DataFrame) -> pd.DataFrame:
    df = df.drop_duplicates()
    df = df.sort_values("timestamp")
    df = df.fillna(method="ffill")
    return df

def continuous_futures(df: pd.DataFrame) -> pd.DataFrame:
    df = df.sort_values("timestamp")
    if "contract" not in df.columns:
        return df
    df["adj_close"] = df["close"]
    rollover = df["contract"] != df["contract"].shift(1)
    gap = df["close"].shift(1) - df["open"]
    df.loc[rollover, "adj_close"] += gap
    return df
