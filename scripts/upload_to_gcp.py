import google
from google.cloud import storage
def upload_blob(bucket_name,source_file_name,destination_blob_name):
    client = storage.Client()
    bucket = client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)
    blob.upload_from_filename(source_file_name)
    print(f"file:{source_file_name} uploaded successfully into bucket:{destination_blob_name}")


upload_blob("abhi-project1-bucket-new-latest","F:\mlops-gcp-udemy\DATASET\Hotel Reservations.csv\Hotel Reservations.csv","reservation_csv_data.csv")



