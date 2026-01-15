
import numpy as np

def backtest(df):
    df["position"] = df["signal"].replace(0, method="ffill")
    df["strategy_ret"] = df["position"].shift(1) * df["spot_ret"]

    total_return = (1 + df["strategy_ret"]).prod() - 1
    sharpe = np.sqrt(252 * 78) * df["strategy_ret"].mean() / df["strategy_ret"].std()

    return total_return, sharpe
