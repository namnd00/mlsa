#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""
@File    :   models.py
@Time    :   2023/11/27 15:21:45
"""

from pydantic import BaseModel, validator
from typing import List, Any, Dict, Union


class DataModel(BaseModel):
    """Data model"""

    id: str
    columns: List[Any]
    rows: List[Any]


class PredictionModel(BaseModel):
    """Data model prediction model"""

    id: str
    predictions: Any
