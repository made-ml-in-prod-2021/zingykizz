import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from entities.feature_params import FeatureParams


def build_numerical_pipeline() -> Pipeline:
    numerical_pipeline = Pipeline([("standard_scaler", StandardScaler())])
    return numerical_pipeline


def build_categorical_pipeline() -> Pipeline:
    categorical_pipeline = Pipeline([("ohe", OneHotEncoder())])
    return categorical_pipeline


def build_transformer(params: FeatureParams) -> ColumnTransformer:
    transformer = ColumnTransformer(
        [
            (
                "categorical_pipeline",
                build_categorical_pipeline(),
                params.categorical_features,
            ),
            (
                "numerical_pipeline",
                build_numerical_pipeline(),
                params.numerical_features,
            ),
        ]
    )
    return transformer


def process_categorical_features(df: pd.DataFrame) -> pd.DataFrame:
    categorical_pipeline = build_categorical_pipeline()
    df.fillna("OTHER", inplace=True)
    return pd.DataFrame(categorical_pipeline.fit_transform(df).toarray())


def process_numerical_features(df: pd.DataFrame) -> pd.DataFrame:
    pipeline = build_numerical_pipeline()
    df.fillna(0, inplace=True)
    return pd.DataFrame(pipeline.fit_transform(df))


def process_features(transformer: ColumnTransformer, df: pd.DataFrame) -> pd.DataFrame:
    return pd.DataFrame(transformer.transform(df))


def extract_target(df: pd.DataFrame, params: FeatureParams) -> pd.Series:
    return df[params.target_col]
