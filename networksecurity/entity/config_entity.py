from datetime import datetime
import os
from networksecurity.constant import trainning_pipeline

print(trainning_pipeline.PIPELINE_NAME)
print(trainning_pipeline.ARTIFACT_DIR)


class TrainingPipelineConfig:
    def __init__(self, timestamp=None):
        if timestamp is None:
            timestamp = datetime.now()
        timestamp = timestamp.strftime('%m_%d_%Y__%H_%M_%S')

        self.pipeline_name = trainning_pipeline.PIPELINE_NAME
        self.artifact_name = trainning_pipeline.ARTIFACT_DIR
        self.artifact_dir=os.path.join(self.artifact_name, timestamp)
        self.timestamp = timestamp


class DataIngestionConfig:
    def __init__(self, training_pipeline_config: TrainingPipelineConfig):
        self.data_ingestion_dir = os.path.join(
            training_pipeline_config.artifact_dir,
            training_pipeline_config.timestamp,
            trainning_pipeline.DATA_INGESTION_DIR_NAME
        )
        self.feature_store_file_path = os.path.join(
            self.data_ingestion_dir,
            trainning_pipeline.DATA_INGESTION_FEATURE_STORE_DIR,
            trainning_pipeline.FILE_NAME
        )
        self.training_file_path = os.path.join(
            self.data_ingestion_dir,
            trainning_pipeline.DATA_INGESTION_INGESTED_DIR,
            trainning_pipeline.TRAIN_FILE_NAME
        )
        self.testing_file_path = os.path.join(
            self.data_ingestion_dir,
            trainning_pipeline.DATA_INGESTION_INGESTED_DIR,
            trainning_pipeline.TEST_FILE_NAME
        )

        self.train_test_split_ratio = trainning_pipeline.DATA_INGESTION_TRAIN_TEST_SPLIT_RATION
        self.collection_name = trainning_pipeline.DATA_INGESTION_COLLECTION_NAME
        self.database_name = trainning_pipeline.DATA_INGESTION_DATABASE_NAME
