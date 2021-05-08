from dataclasses import dataclass


@dataclass
class TrainingParams:
    model_type: str
    penalty: str
    C: float
