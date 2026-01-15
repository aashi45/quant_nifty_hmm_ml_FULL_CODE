
import pandas as pd
import numpy as np

def calculate_atm(price, step=50):
    return int(round(price / step) * step)

def clean_timeseries(df):
    df = df.drop_duplicates()
    df = df.sort_values("timestamp")
    df = df.fillna(method="ffill")
    return df

def continuous_futures(df):
    df = df.sort_values("timestamp")
    df["adj_close"] = df["close"]
    rollover = df["contract"] != df["contract"].shift()
    gap = df["close"].shift() - df["open"]
    df.loc[rollover, "adj_close"] += gap
    return df
