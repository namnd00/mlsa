#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""
@File    :   data_serving.py
@Time    :   2023/11/27 15:39:29
"""
from src.processing.data_transformation import (
    replace_empty_in_col,
    fit_categorical_encoders,
    fit_numerical_transformers,
    transform_numerical_transformers,
    transform_categorical_encoders,
    fit_data_scaler,
    transform_data_scaler,
)

from src.config import core as cfg


def get_preprocess_data(X_data):
    # X_data = replace_empty_in_col(X_data)
    selected_cols = cfg.NUM_VARS_YEO_YOHNSON + cfg.CAT_VARS_ORDINAL_ARBITARY
    X_data = X_data[selected_cols]

    cat_encoders = fit_categorical_encoders(X_data)
    X_data = transform_categorical_encoders(X_data, cat_encoders)

    num_transformers = fit_numerical_transformers(X_data)
    X_data = transform_numerical_transformers(X_data, num_transformers)

    scaler = fit_data_scaler(X_data)
    X_data = transform_data_scaler(scaler, X_data)

    return X_data
