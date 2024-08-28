from src.objectClassification import logger
from src.objectClassification.pipeline.stage_01_data_ingestion import DataIngestionTrainingpipeline

# logger.info("welcome to our custome logs")

STAGE_NAME = "Data Ingestion stage"
try:
    logger.info(f">>>stage {STAGE_NAME} started <<<<<<<<<<<")
    obj = DataIngestionTrainingpipeline()
    obj.main()
    logger.info(f">>>Stage {STAGE_NAME} Is Completed <<<<<<<<<<<\nx==========x")



except Exception as e:
    logger.exception(e)
    raise e
