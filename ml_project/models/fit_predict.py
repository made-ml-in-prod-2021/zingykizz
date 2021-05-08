import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import f1_score, balanced_accuracy_score
from typing import Dict
import joblib

from entities.train_params import TrainingParams


def train_model(
    features: pd.DataFrame, target: pd.Series, train_params: TrainingParams
) -> LogisticRegression:
    model = LogisticRegression(penalty=train_params.penalty, C=train_params.C)
    model.fit(features, target)
    return model


def predict_model(model: LogisticRegression, features: pd.DataFrame) -> np.ndarray:
    return model.predict(features)


def evaluate_model(predicts: np.ndarray, target: pd.Series) -> Dict[str, float]:
    return {
        "f1_score": f1_score(target, predicts, average="weighted"),
        "balanced_accuracy_score": balanced_accuracy_score(target, predicts),
    }


def serialize_model(model: LogisticRegression, fout: str) -> None:
    with open(fout, "wb") as f:
        joblib.dump(model, f)
