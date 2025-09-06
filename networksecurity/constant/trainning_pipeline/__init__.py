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





'''
Data ingestieon related constant used for data ingestion component
'''

DATA_INGESTION_COLLECTION_NAME = "NetworkDat"
DATA_INGESTION_DATABASE_NAME = "Anirban"
DATA_INGESTION_DIR_NAME:str = "data_ingestion"
DATA_INGESTION_FEATURE_STORE_DIR:str = "feature_store"
DATA_INGESTION_INGESTED_DIR:str = "ingested"
DATA_INGESTION_TRAIN_TEST_SPLIT_RATION = 0.2

