#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""
@File    :   utils.py
@Time    :   2023/11/27 15:00:12
"""
from typing import Callable, Optional, Text
import os
from joblib import Memory

from src.config import core as cfg

import logging
import mlflow


logger = logging.getLogger(__name__)


class ModelLoader:
    """
    Model Loader singleton: Load model productions from mlflow model registry
    """

    _instance: Optional[object] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self) -> None:
        self.model_path: Text = None
        self.model: Optional[Callable] = None
        mlflow_tracking_uri = os.environ.get("MLFLOW_TRACKING_URI")
        mlflow.set_tracking_uri(mlflow_tracking_uri)
        self.cache_dir = "model_cache"

    def get_model(self) -> Callable:
        """Get the model"""
        if not self.model:
            self._load_model()

        return self.model

    def _load_model(self) -> None:
        """Load model from mlflow model registry"""
        mlflow_model_prefix = str(cfg.MODEL_SERVING_STAGE)
        model_uri = f"models:/{cfg.MODEL_SERVING_NAME}/{mlflow_model_prefix}"
        logger.info(f"Model URI: %s" % model_uri)
        model_loader = cfg.MODEL_SERVING_LOADER
        logger.info("Loading model from: %s", model_uri)

        # Create a cache object
        # cache = Memory(self.cache_dir).cache

        # Check if a new model version is available
        # latest_model_version = mlflow.MlflowClient().get_latest_versions(
        #    cfg.MODEL_SERVING_NAME, stages=[mlflow_model_prefix]
        # )[0]
        # logger.info(f"Model version: {latest_model_version}")

        # Add the model version to the cache metadata
        if model_loader == "sklearn":
            # load_model_func = cache(
            #     mlflow.sklearn.load_model
            # )  # Apply caching to the load_model function
            self.model = mlflow.sklearn.load_model(model_uri)
        elif model_loader == "pyfunc":
            # load_model_func = cache(
            #     mlflow.pyfunc.load_model
            # )  # Apply caching to the load_model function
            self.model = mlflow.pyfunc.load_model(model_uri)
        else:
            self.model = None
            raise Exception(f"Not implemented model loading: %s" % model_uri)

        logger.info("Model loaded: %s" % model_uri)
