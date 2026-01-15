
from py_vollib.black_scholes.greeks.analytical import delta, gamma, theta, vega, rho

def compute_greeks(flag, S, K, T, r, iv):
    return {
        "delta": delta(flag, S, K, T, r, iv),
        "gamma": gamma(flag, S, K, T, r, iv),
        "theta": theta(flag, S, K, T, r, iv),
        "vega": vega(flag, S, K, T, r, iv),
        "rho": rho(flag, S, K, T, r, iv),
    }
