
def generate_signals(df):
    df["signal"] = 0
    df.loc[(df["ema_5"] > df["ema_15"]) & (df["regime"] == 1), "signal"] = 1
    df.loc[(df["ema_5"] < df["ema_15"]) & (df["regime"] == -1), "signal"] = -1
    return df
