from src.cnnClassifier import logger
from src.cnnClassifier.pipeline.stage_01__data_ingestion import DataIngestionTrainingPipeline
from src.cnnClassifier.pipeline.stage_02__prepare_base_model import PrepareBaseModelTrainingPipeline
from src.cnnClassifier.pipeline.stage_03__training import ModelTrainingPipeline
from src.cnnClassifier.pipeline.stage_04__evaluation import EvaluationPipeline


STAGE_NAME = "Data ingestion"
try:
    logger.info(f">>>>> stage '{STAGE_NAME}' started <<<<<")
    data_ingestor = DataIngestionTrainingPipeline()
    data_ingestor.main()
    logger.info(f">>>>> stage '{STAGE_NAME}' completed <<<<<\n\nx===========x")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Prepare base model"
try:
    logger.info(f"********************************")
    logger.info(f">>>>> stage '{STAGE_NAME}' started <<<<<")
    base_model_preparator = PrepareBaseModelTrainingPipeline()
    base_model_preparator.main()
    logger.info(f">>>>> stage '{STAGE_NAME}' completed <<<<<\n\nx===========x")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Model training"
try:
    logger.info(f"********************************")
    logger.info(f">>>>> stage '{STAGE_NAME}' started <<<<<")
    model_trainer = ModelTrainingPipeline()
    model_trainer.main()
    logger.info(f">>>>> stage '{STAGE_NAME}' completed <<<<<\n\nx===========x")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Model evaluation"
try:
    logger.info(f"********************************")
    logger.info(f">>>>> stage '{STAGE_NAME}' started <<<<<")
    model_evaluator = EvaluationPipeline()
    model_evaluator.main()
    logger.info(f">>>>> stage '{STAGE_NAME}' completed <<<<<\n\nx===========x")
except Exception as e:
    logger.exception(e)
    raise e