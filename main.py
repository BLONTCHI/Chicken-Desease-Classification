from src.cnnClassifier import logger
from src.cnnClassifier.pipeline.stage_01__data_ingestion import DataIngestionTrainingPipeline
from src.cnnClassifier.pipeline.stage_02__prepare_base_model import PrepareBaseModelTrainingPipeline
from src.cnnClassifier.pipeline.stage_03__training import ModelTrainingPipeline


STAGE_NAME = "Data ingestion"
try:
    logger.info(f">>>>> stage '{STAGE_NAME}' started <<<<<")
    prepare_base_model = DataIngestionTrainingPipeline()
    prepare_base_model.main()
    logger.info(f">>>>> stage '{STAGE_NAME}' completed <<<<<\n\nx===========x")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Prepare base model"
try:
    logger.info(f"********************************")
    logger.info(f">>>>> stage '{STAGE_NAME}' started <<<<<")
    prepare_base_model = PrepareBaseModelTrainingPipeline()
    prepare_base_model.main()
    logger.info(f">>>>> stage '{STAGE_NAME}' completed <<<<<\n\nx===========x")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Training model"
try:
    logger.info(f"********************************")
    logger.info(f">>>>> stage '{STAGE_NAME}' started <<<<<")
    prepare_base_model = ModelTrainingPipeline()
    prepare_base_model.main()
    logger.info(f">>>>> stage '{STAGE_NAME}' completed <<<<<\n\nx===========x")
except Exception as e:
    logger.exception(e)
    raise e