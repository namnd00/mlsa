#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""
@File    :   pipeline.py
@Time    :   2023/11/30 00:21:54
"""

from src.config import core as cfg
from src.modeling import model_train, model_validation, model_push
from src.processing import data_transformation

from src.config.core import _data_files, experiment_name, model_name

# read data
data_transformation.read_data(_data_files)

# split to train and test
data_transformation.split_train_test(_data_files)

# preprocess data
data_transformation.preprocess_data(_data_files)

# train model
model_train.train_model_ci(
    data_files=_data_files,
    experiment_name=experiment_name,
    model_name=model_name,
    track_cv_performance=True,
)
