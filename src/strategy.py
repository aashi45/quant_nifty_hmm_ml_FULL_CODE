
def generate_signals(df):
    df["signal"] = 0

    cross_up = (df["ema_5"] > df["ema_15"]) & (df["ema_5"].shift(1) <= df["ema_15"].shift(1))
    cross_dn = (df["ema_5"] < df["ema_15"]) & (df["ema_5"].shift(1) >= df["ema_15"].shift(1))

    df.loc[cross_up & (df["regime"] == 1), "signal"] = 1
    df.loc[cross_dn & (df["regime"] == -1), "signal"] = -1

    return df
