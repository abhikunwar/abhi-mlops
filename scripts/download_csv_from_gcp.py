import google
import os
from google.cloud import storage
import config
import utils
from utils.common_functions import read_yml,create_dir
from src.logger import get_logger
logger = get_logger(__name__)
def download_csv(bucket_name,blob_name):
    client = storage.Client()
    bucket = client.bucket(bucket_name)
    blob = bucket.blob(blob_name)
    
    config_file = read_yml('config','path_config.yaml')
    logger.info(f"config file name is :{config_file}")
    raw_folder_path = config_file['data_path']['RAW_DIR_PATH']
    print(raw_folder_path)
    # will create a raw_data folder in artifacts folder
    raw_data_path = create_dir(raw_folder_path)
    # complete raw file path
    raw_file_path = os.path.join(raw_folder_path, "hotel_reservation_data.csv")
    # download the file
    blob.download_to_filename(raw_file_path)
    logger.info(f"raw data loaded into {raw_file_path}")
    # print(raw_data_path)

download_csv("abhishek-project1-bucket","reservation_csv_data.csv")


