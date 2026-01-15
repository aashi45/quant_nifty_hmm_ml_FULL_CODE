
from xgboost import XGBClassifier

def train_xgb(X, y):
    model = XGBClassifier(n_estimators=300, max_depth=5, learning_rate=0.05)
    model.fit(X, y)
    return model
