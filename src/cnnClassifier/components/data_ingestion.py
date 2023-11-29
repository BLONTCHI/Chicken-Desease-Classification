import os
import zipfile
from pathlib import Path
from urllib import request
from cnnClassifier import logger
from cnnClassifier.utils.common import get_size
from cnnClassifier.entity.config_entity import DataIngestionConfig


class DataIngestion:
    def __init__(self, config:DataIngestionConfig):
        self.config = config
    
    
    def download_data(self):
        if not os.path.exists(self.config.local_data_filename):
            filename, headers = request.urlretrieve(url=self.config.source_url,
                                                    filename=self.config.local_data_filename)
            logger.info(f"{filename} downloaded with following info: \n{headers}")
        else:
            logger.info(f"{self.config.local_data_filename} already exists of size: {get_size(Path(self.config.local_data_filename))}")
            
            
    def extract_zipfile(self):
        """
        zip_file_path: str
        Extracts the zip file into the data directory
        Function returns None
        """
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_filename, 'r') as zip_file:
            zip_file.extractall(unzip_path)