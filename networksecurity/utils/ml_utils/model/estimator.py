from networksecurity.constant.trainning_pipeline import SAVED_MODEL_DIR, MODEL_FILE_NAME
from networksecurity.entity.config_entity import TrainingPipelineConfig
import os
import sys

from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging  

class NetworkModel:
    def __init__(self,preprocessor, model):
        try:
            self.processor=preprocessor
            self.model=model

        except Exception as e:
            raise NetworkSecurityException(e, sys)  
        
    def predict(self, x):
        try:
            logging.info("Prediction started")
            x_transform=self.processor.transform(x)
            logging.info("Data transformed successfully")
            y_hat=self.model.predict(x_transform)
            logging.info("Prediction completed successfully")
            return y_hat
        except Exception as e:
            raise NetworkSecurityException(e, sys)  

