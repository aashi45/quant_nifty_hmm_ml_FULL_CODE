
import numpy as np

def add_ema(df):
    df["ema_5"] = df["spot_close"].ewm(span=5, adjust=False).mean()
    df["ema_15"] = df["spot_close"].ewm(span=15, adjust=False).mean()
    return df

def add_derived_features(df):
    df["avg_iv"] = (df["call_iv"] + df["put_iv"]) / 2
    df["iv_spread"] = df["call_iv"] - df["put_iv"]
    df["pcr_oi"] = df["put_oi"] / df["call_oi"]
    df["pcr_vol"] = df["put_volume"] / df["call_volume"]
    df["futures_basis"] = (df["fut_close"] - df["spot_close"]) / df["spot_close"]
    df["spot_ret"] = df["spot_close"].pct_change()
    df["delta_neutral_ratio"] = abs(df["call_delta"]) / abs(df["put_delta"])
    df["gamma_exposure"] = df["spot_close"] * df["call_gamma"] * df["call_oi"]
    return df
