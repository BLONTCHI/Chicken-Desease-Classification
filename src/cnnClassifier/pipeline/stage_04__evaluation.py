from cnnClassifier.config.configuration import ConfigurationManager
from cnnClassifier.components.evaluation import Evaluation
from cnnClassifier import logger


STAGE_NAME = "Model evaluation"


class EvaluationPipeline:
    def __init__(self):
        pass

    
    def main(self):
        config = ConfigurationManager()
        val_config = config.get_validation_config()
        evaluation = Evaluation(config=val_config)
        evaluation.evaluation()
        evaluation.save_score()
        
    
if __name__ == '__main__':
    try:
        logger.info(f'********************************')
        logger.info(f">>>>> stage '{STAGE_NAME.upper()}' started <<<<<")
        obj = EvaluationPipeline()
        obj.main()
        logger.info(f">>>>> stage '{STAGE_NAME.upper()}' completed <<<<<\n\nx===========x")
    except Exception as e:
        logger.exception(e)
        raise e