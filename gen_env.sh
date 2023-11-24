#!/bin/bash

AIRFLOW_DIR="./dockerfiles/airflow"
JUPYTER_DIR="./dockerfiles/jupyter"
MLFLOW_DIR="./dockerfiles/mlflow"

REQUIREMENT_FILE="requirements.txt"

for dir in "$AIRFLOW_DIR" "$JUPYTER_DIR" "$MLFLOW_DIR"; do
    requirement_file="$dir/$REQUIREMENT_FILE"
    echo "---Installing requirement from $requirement_file"
    pip install --upgrade pip
    pip install -r $requirement_file --ignore-installed --no-warn-script-location
    echo "---Done---"
done

echo "Installing requirements successfully!"
