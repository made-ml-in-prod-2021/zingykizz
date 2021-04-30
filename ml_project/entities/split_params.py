from dataclasses import dataclass


@dataclass
class SplittingParams:
    val_size: float = 0.2
    random_state: int = 0
