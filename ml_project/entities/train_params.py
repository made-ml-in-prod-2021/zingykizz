from dataclasses import dataclass


@dataclass
class TrainingParams:
    model_type: str = "CatBoostClassifier"
    random_state: int = 0
