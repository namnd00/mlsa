#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""
@File    :   core.py
@Time    :   2023/11/29 19:16:18
"""

from pathlib import Path
import os
import sys

sys.path.append(os.path.relpath(".."))

import src

SRC_ROOT = Path(src.__file__).resolve().parent
ROOT = SRC_ROOT.parent
DATASET_DIR = ROOT / "data"
ARTIFACTS_DIR = ROOT / "artifacts"

if not os.path.exists(ARTIFACTS_DIR):
    os.makedirs(ARTIFACTS_DIR)

DATA1 = DATASET_DIR / "input_data/telco_customer_churn_1.csv"
DATA2 = DATASET_DIR / "input_data/telco_customer_churn_2.csv"

RANDOM_STATE = 0
TEST_SIZE = 0.2

VARS_TO_DROP = ["customerID"]
CAT_VARS_ONEHOT = [
    "gender",
    "Partner",
    "Dependents",
    "PhoneService",
    "PaperlessBilling",
]
CAT_VARS_ORDINAL_ARBITARY = [
    "MultipleLines",
    "InternetService",
    "OnlineSecurity",
    "OnlineBackup",
    "DeviceProtection",
    "TechSupport",
    "StreamingTV",
    "StreamingMovies",
    "Contract",
    "PaymentMethod",
]
NUM_VARS_YEO_YOHNSON = ["TotalCharges"]
TARGET = "Churn"
VAR_REPLACE_EMPTY_DATA = ["TotalCharges"]

### Serving
MODEL_SERVING_NAME = "LR"
MODEL_SERVING_STAGE = "production"
MODEL_SERVING_LOADER = "sklearn"
MODEL_SERVING_API_VERSION = "v0.1.0"
MLFLOW_TRACKING_URI = "http://127.0.0.1:5001"
# MLFLOW_TRACKING_URI = "http://host.docker.internal:5001"

# DAGS configuration

model_name = "LR"
experiment_name = "churn_prediction"
reg_model = "LR/2"

_root_dir = "/"
_data_dir = "./data"
_output_data_dir = _data_dir + "/output_data"

if not os.path.exists(_output_data_dir):
    os.makedirs(_output_data_dir, mode=0o777)

_data_files = {
    "input_raw_data_file": os.path.join(DATA1),
    "raw_data_file": os.path.join(_output_data_dir + "/data.csv"),
    "raw_x_train_file": os.path.join(_output_data_dir + "/x_train_raw.csv"),
    "raw_x_test_file": os.path.join(_output_data_dir + "/x_test_raw.csv"),
    "raw_y_train_file": os.path.join(_output_data_dir + "/y_train_raw.csv"),
    "raw_y_test_file": os.path.join(_output_data_dir + "/y_test_raw.csv"),
    "transformed_x_train_file": os.path.join(_output_data_dir + "/x_train.csv"),
    "transformed_y_train_file": os.path.join(_output_data_dir + "/y_train.csv"),
    "transformed_x_test_file": os.path.join(_output_data_dir + "/x_test.csv"),
    "transformed_y_test_file": os.path.join(_output_data_dir + "/y_test.csv"),
}

if not _root_dir:
    raise ValueError("PROJECT_PATH environment variable not set")
