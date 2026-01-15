
# Quantitative Trading Strategy with Regime Detection and Machine Learning

## Project Overview
This project implements a complete end-to-end quantitative trading system on NIFTY 50 using
spot, futures, and options data at 5-minute frequency. The system integrates feature engineering,
options Greeks, Hidden Markov Model (HMM) based regime detection, rule-based EMA trading,
machine learning trade filtering, and high-performance trade analysis.

The goal is to demonstrate strong capabilities in quantitative research, data engineering,
statistical modeling, and applied machine learning.

## Key Components
- Data acquisition and cleaning (Spot, Futures, Options)
- Feature engineering (EMAs, IV, Greeks, PCR, Futures Basis)
- Market regime detection using Hidden Markov Models
- EMA crossover trading strategy with regime filter
- Backtesting with risk-adjusted performance metrics
- Machine learning enhancement using XGBoost and LSTM
- Outlier and alpha trade analysis

## Repository Structure
```
quant_nifty_hmm_ml/
│
├── data/
│   ├── nifty_spot_5min.csv
│   ├── nifty_futures_5min.csv
│   ├── nifty_options_5min.csv
│   ├── nifty_merged_5min.csv
│   └── nifty_features_5min.csv
│
├── notebooks/
│   ├── 1_data_fetch.ipynb
│   ├── 2_data_cleaning.ipynb
│   ├── 3_feature_engineering.ipynb
│   ├── 4_regime_detection.ipynb
│   ├── 5_strategy_backtest.ipynb
│   ├── 6_ml_models.ipynb
│   └── 7_outlier_analysis.ipynb
│
├── src/
│   ├── __init__.py
│   ├── data_utils.py
│   ├── features.py
│   ├── greeks.py
│   ├── regime.py
│   ├── strategy.py
│   ├── backtest.py
│   └── ml_models.py
│
├── models/
│   ├── xgboost_model.pkl
│   └── lstm_model.h5
│
├── plots/
│   ├── regime_overlay.png
│   ├── transition_matrix.png
│   ├── performance_curve.png
│   ├── feature_importance.png
│   └── outlier_analysis.png
│
├── results/
│   ├── backtest_metrics.csv
│   ├── ml_comparison.csv
│   └── outlier_stats.txt
│
├── requirements.txt
└── README.md


FILE-BY-FILE RESPONSIBILITY
🔹 src/data_utils.py

Purpose: Data engineering & futures handling
Contains:

ATM strike calculation

Timestamp alignment

Missing value handling

Continuous futures rollover logic

Used by:

1_data_fetch.ipynb

2_data_cleaning.ipynb

🔹 src/features.py

Purpose: Feature engineering
Contains:

EMA(5), EMA(15)

Returns

PCR (OI + Volume)

IV metrics

Futures basis

Gamma exposure

Delta-neutral ratio

Used by:

3_feature_engineering.ipynb

🔹 src/greeks.py

Purpose: Options mathematics
Contains:

Black–Scholes Greeks:

Delta

Gamma

Theta

Vega

Rho

Uses:

py_vollib

Risk-free rate = 6.5%

Used by:

3_feature_engineering.ipynb

🔹 src/regime.py

Purpose: Market regime detection
Contains:

HMM training (3 states)

Regime prediction

Train/test split (70/30)

Output:

Regime labels → {+1, 0, -1}

Used by:

4_regime_detection.ipynb

🔹 src/strategy.py

Purpose: Trading logic
Contains:

EMA crossover signals

Regime filter

Long/Short logic

No-trade in sideways regime

Used by:

5_strategy_backtest.ipynb

🔹 src/backtest.py

Purpose: Performance evaluation
Contains:

Vectorized backtesting

PnL calculation

Metrics:

Total return

Sharpe ratio

Max drawdown

Win rate

Profit factor

Used by:

5_strategy_backtest.ipynb

6_ml_models.ipynb

🔹 src/ml_models.py

Purpose: Machine learning enhancement
Contains:

XGBoost classifier

Time-series split

Confidence prediction

Trade filtering logic

Used by:

6_ml_models.ipynb
## Installation
```bash
pip install -r requirements.txt
```

## How to Run
1. Run notebooks sequentially from `1_data_fetch.ipynb` to `7_outlier_analysis.ipynb`
2. All intermediate data is saved in the `data/` folder
3. Plots and results are saved automatically

## Strategy Summary
- Trading Signal: 5/15 EMA crossover
- Regime Filter: HMM-based (Uptrend / Downtrend / Sideways)
- Execution: Next candle open
- ML Filter: Trade taken only when ML confidence > 0.5

## Key Results (Summary)
- Improved Sharpe Ratio using ML filtering
- Reduced drawdowns in sideways regimes
- Majority of high-alpha trades occurred in trending regimes
- Options-derived features significantly improved regime classification

## Author
Aashi Shokeen
