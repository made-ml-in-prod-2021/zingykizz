from dataclasses import dataclass
from marshmallow_dataclass import class_schema
import yaml


@dataclass
class OnlineInferenceAppParams:
    model_path: str
    transformer_path: str
    host: str
    port: int


OnlineInferenceAppParamsSchema = class_schema(OnlineInferenceAppParams)


def read_online_inference_app_params(path: str) -> OnlineInferenceAppParams:
    """Чтение параметров приложения для инференса"""
    with open(path, mode="r") as f:
        config_dict = yaml.safe_load(f)
        schema = OnlineInferenceAppParamsSchema().load(config_dict)
        return schema
