from dataclasses import dataclass
from entities.split_params import SplittingParams
from entities.feature_params import FeatureParams
from entities.train_params import TrainingParams
from marshmallow_dataclass import class_schema
import yaml


@dataclass
class TrainingPipelineParams:
    input_data_path: str
    output_model_path: str
    metric_path: str
    splitting_params: SplittingParams
    feature_params: FeatureParams
    train_params: TrainingParams


TrainingPipelineParamsSchema = class_schema(TrainingPipelineParams)


def read_training_pipeline_params(path: str) -> TrainingPipelineParams:
    """Чтение параметров пайплайна"""
    with open(path, mode="r") as f:
        config_dict = yaml.safe_load(f)
        schema = TrainingPipelineParamsSchema().load(config_dict)
        return schema
