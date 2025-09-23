import os
import sys
import numpy as np
import pandas as pd

"""
defining common constant for training pipeline
"""

TARGET_COLUMN = "Result"
PIPELINE_NAME = "NetworkSecurity"
ARTIFACT_DIR = "Artifacts"
FILE_NAME = "phishingData.csv"

TRAIN_FILE_NAME:str = "train.csv"
TEST_FILE_NAME:str = "test.csv"


SCHEMA_FILE_PATH=os.path.join("data_schema","schema.yaml")
SAVED_MODEL_DIR=os.path.join("saved_models")
MODEL_FILE_NAME="model.pkl"


'''
Data ingestieon related constant used for data ingestion component
'''

DATA_INGESTION_COLLECTION_NAME = "NetworkDat"
DATA_INGESTION_DATABASE_NAME = "Anirban"
DATA_INGESTION_DIR_NAME:str = "data_ingestion"
DATA_INGESTION_FEATURE_STORE_DIR:str = "feature_store"
DATA_INGESTION_INGESTED_DIR:str = "ingested"
DATA_INGESTION_TRAIN_TEST_SPLIT_RATION = 0.2


'''
Data validation related constant start with DATA_VALIDATION VAR NAME

'''

DATA_VALIDATION_DIR_NAME:str = "data_validation"
DATA_VALIDATION_VALID_DIR:str = "validated"
DATA_VALIDATION_INVALID_DIR:str = "invalid"
DATA_VALIDATION_DRIFT_REPORT_DIR:str = "drift_report"
DATA_VALIDATION_DRIFT_REPORT_FILE_NAME:str = "report.yaml"
PREPROSSING_OBJECT_FILE_NAME:str = "preprocessing.pkl"

"""
Data transformation related constant start with DATA_TRANSFORMATION VAR NAME
"""
DATA_TRANSFORMATION_DIR_NAME:str = "data_transformation"
DATA_TRANSFORMATION_TRANSFORMED_DATA_DIR:str = "transformed"
DATA_TRANSFORMATION_TRANSFORMED_OBJECT_DIR:str = "transformed_object"

#KNN IMPUTER FOR MISSING VALUES
DATA_TRANSFORMATION_INPUTER_PARAMS:dict={
    "missing_values" : np.nan,    
    "n_neighbors" : 3,
    "weights" : 'uniform',
}


"""Model trainer related constant start with MODEL_TRAINER VAR NAME

"""
MODEL_TRAINER_DIR_NAME:str="MODEL_TRAINER"
MODEL_TRAINER_TRAINED_MODEL_DIR:str="trained_model"
MODEL_TRAINER_TRAINED_MODEL_FILE_NAME:str="model.pkl"
MODEL_TRAINER_EXPECTED_SCORE:float=0.6
MODEL_TRAINER_OVER_FITTING_UNDER_FITTING_THRESHOLD:float=0.05
