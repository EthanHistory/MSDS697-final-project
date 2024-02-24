import os
import json
import datetime
from pathlib import Path

from airflow.decorators import task
from airflow.models.dag import DAG
from airflow.operators.python import PythonOperator
from airflow.providers.google.cloud.transfers.gcs_to_local import GCSToLocalFilesystemOperator
from pymongo import MongoClient

# GCS related constants
BUCKET_NAME = "msds697-jobs"
FILE_NAME = "jobs/jobs.json"

# airflow environment variable (do not change)
AIRFLOW_HOME = Path(os.environ.get('AIRFLOW_HOME'))

# local file path
PATH_TO_SAVED_FILE = AIRFLOW_HOME / "airflow" / "jobs.json"

# Mongo DB configuration
DATABASE_NAME = "msds697"
COLLECTION_NAME = "jobs"
MONGODB_HOST = 'localhost'
MONGODB_PORT = 27017

def upload_to_mongo():
    client = MongoClient(host=MONGODB_HOST, port=MONGODB_PORT)
    db = client[DATABASE_NAME]
    collection = db[COLLECTION_NAME]
    with open(PATH_TO_SAVED_FILE, "r") as file:
        documents = json.load(file)
        collection.insert_many(documents)

with DAG(
    dag_id="example",
    start_date=datetime.datetime(2024, 2, 1),
    catchup=False,
    schedule="@daily",
    tags=["example"],
) as dag:
    
    download_file = GCSToLocalFilesystemOperator(
        task_id="download_file",
        object_name=FILE_NAME,
        bucket=BUCKET_NAME,
        filename=PATH_TO_SAVED_FILE
    )

    upload_file_to_mongodb = PythonOperator(
        task_id='upload_mongodb',
        python_callable=upload_to_mongo
    )

    download_file >> upload_file_to_mongodb