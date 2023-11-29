from cnnClassifier.config.configuration import ConfigurationManager
from cnnClassifier.components.data_ingestion import DataIngestion
from cnnClassifier import logger


STAGE_NAME = "Data ingestion"

class DataIngestionTrainingPipeline:
    def __init__(self):
        pass
    
    
    def main(self):
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_config)
        data_ingestion.download_data()
        data_ingestion.extract_zipfile()
        

if __name__ == '__main__':
    try:
        logger.info(f">>>>> stage '{STAGE_NAME.upper()}' started <<<<<")
        obj = DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f">>>>> stage '{STAGE_NAME.upper()}' completed <<<<<\n\nx===========x")
    except Exception as e:
        logger.exception(e)
        raise e