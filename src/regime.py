
import numpy as np
from hmmlearn.hmm import GaussianHMM

def fit_hmm(df, feature_cols):
    X = df[feature_cols].dropna().values
    split = int(len(X) * 0.7)

    model = GaussianHMM(
        n_components=3,
        covariance_type="full",
        n_iter=100,
        random_state=42
    )
    model.fit(X[:split])

    regimes = model.predict(X)
    return regimes, model
