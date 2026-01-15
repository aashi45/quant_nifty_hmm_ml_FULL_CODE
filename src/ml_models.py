
from xgboost import XGBClassifier

def train_xgboost(X_train, y_train):
    model = XGBClassifier(
        n_estimators=300,
        max_depth=5,
        learning_rate=0.05,
        subsample=0.8,
        colsample_bytree=0.8,
        eval_metric="logloss"
    )
    model.fit(X_train, y_train)
    return model
