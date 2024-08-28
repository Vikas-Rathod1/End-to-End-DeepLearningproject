from src.objectClassification.components.data_ingestion import DataIngestion
from src.objectClassification.config.configuration import ConfigurationManager
from src.objectClassification import logger

STAGE_NAME = "Data Ingestion stage"
#Pipeline 

class DataIngestionTrainingpipeline:
    def __init__(self):
        pass
    def main(self):
        try:
            config = ConfigurationManager()
            print("000000000000000000")
            data_ingestion_config = config.get_data_ingestion_config()
            print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>",data_ingestion_config)
            data_ingestion = DataIngestion(config=data_ingestion_config)
            data_ingestion.download_file()
            data_ingestion.extract_zip_file()
        except Exception as e:
            raise e
        
if __name__ == '__main__':

    try:
        logger.info(f">>>stage {STAGE_NAME} started <<<<<<<<<<<")
        obj = DataIngestionTrainingpipeline()
        obj.main()
        logger.info(f">>>stage {STAGE_NAME} completed <<<<<<<<<<<\n\nx==========x")



    except Exception as e:
        logger.exception(e)
        raise e

