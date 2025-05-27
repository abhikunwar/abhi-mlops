import src
from src.data_ingestion import get_data
from src.model_training import training
if __name__=="__main__":
#    get the data
   get_data("bucket-1505","hotel_reservation_file.csv","reservation_csv_data.csv")
# model training   
   training()