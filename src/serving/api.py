#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""
@File    :   api.py
@Time    :   2023/11/27 15:17:34
"""

import logging

from typing import Callable, Text
from fastapi import FastAPI, BackgroundTasks
from fastapi.responses import (
    HTMLResponse,
    JSONResponse,
    Response,
)

from src.serving.utils import ModelLoader
from src.serving.models import DataModel, PredictionModel
from src.processing.data_serving import get_preprocess_data
import src.config.core as cfg
import pandas as pd


logging.basicConfig(
    level=logging.INFO,
    format="API - %(asctime)s - %(levelname)s - %(module)s - %(message)s",
)

logger = logging.getLogger(__name__)

app = FastAPI(
    title="FastAPIModelServing",
    version=cfg.MODEL_SERVING_API_VERSION,
    description="FastAPI model serving application",
)

model_loader: ModelLoader = ModelLoader()
model: Callable = model_loader.get_model()


@app.get("/")
def index() -> HTMLResponse:
    return HTMLResponse("<h1><i>FastAPIModelServing</i></h1")


@app.post("/predict")
def predict(
    response: Response, received_data: DataModel, background_tasks: BackgroundTasks
) -> JSONResponse:
    try:
        features_df = pd.DataFrame(
            data=received_data.rows, columns=received_data.columns
        )
        preprocessed_features = get_preprocess_data(features_df)
        predictions = model.predict(preprocessed_features)
        content = {
            "id": received_data.id,
            "predictions": predictions.tolist(),
        }
        logger.info(content)
        return JSONResponse(content=content)
    except Exception as e:
        response.status_code = 500
        logging.error(e, exc_info=True)
        return JSONResponse(
            content={
                "error_msg": str(e),
            }
        )
