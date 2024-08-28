from objectClassification.entity.config_entity import DataIngestionConfig
from src.objectClassification.constants import *
from src.objectClassification.utils.common import read_yaml, create_directories

class ConfigurationManager:
    # check in side constant directory see __init__ constructor
    def __init__(
        self,
        config_filepath = CONFIG_FILE_PATH,
        params_filepath = PARAM_FILE_PATH):

        self.config = read_yaml(config_filepath) #return Congif dictionary
        self.params = read_yaml(params_filepath) #return Congif dictionary
        
        # create_directory calling from common.py
        create_directories([self.config.artifacts_root]) 
        


    # check inside config directory check config.yaml 
    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion # this comming from config.yaml
        print(">>>>>>>>>>>>>>>>>.",config)
        create_directories([config.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            source_URL=config.source_URL,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir 
        )

        return data_ingestion_config