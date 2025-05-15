import google
import os
from google.cloud import storage
import config
import utils
from utils.common_functions import read_yml,create_dir
from src.logger import get_logger
logger = get_logger(__name__)

def get_data(bucket_name,destination_file_name,source_file_name):
    client = storage.Client()
    bucket = client.bucket(bucket_name)
    blob = bucket.blob(source_file_name)

    config_file = read_yml('path_config.yaml')
    logger.info(f"config file name is :{config_file}")
    raw_folder_path = config_file['data_path']['RAW_DIR_PATH']
    logger.info(f"raw data will be stored in :{raw_folder_path}")
    
    raw_file_path = os.path.join(raw_folder_path, destination_file_name)
    blob.download_to_filename(raw_file_path)

    logger.info(f"raw data download from gcp completed")
if __name__=="__main__":
    get_data("abhi-project1-bucket-new-updated","hotel_reservation_file.csv","reservation_csv_data.csv")   