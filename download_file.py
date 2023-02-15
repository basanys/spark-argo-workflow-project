import logging
import os
import boto3
import glob
from botocore.exceptions import ClientError
from botocore.client import Config

from dotenv import load_dotenv
load_dotenv()

from kaggle.api.kaggle_api_extended import KaggleApi
api = KaggleApi()
api.authenticate()

AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID")
AWS_SECRET_KEY = os.environ.get("AWS_SECRET_KEY")
AWS_REGION_NAME = os.environ.get("AWS_REGION_NAME")
AWS_BUCKET_NAME = os.environ.get("AWS_BUCKET_NAME")
IDENTIFIER = os.environ.get("IDENTIFIER")

def download_file(identifier):   
    api.dataset_download_files(dataset=identifier,
                                path=".",
                                unzip=True)

def upload_file_to_s3(file_name, bucket, key):

    s3_client = boto3.client('s3',
                    aws_access_key_id=AWS_ACCESS_KEY_ID,
                    aws_secret_access_key=AWS_SECRET_KEY,
                    config=Config(signature_version='s3v4'),
                    region_name=AWS_REGION_NAME
                    )
    try:
        response = s3_client.upload_file(file_name, bucket, key)
    except ClientError as e:
        logging.error(e)
        return False
    return True

if __name__ == "__main__":
    download_file(IDENTIFIER)
    file_name = glob.glob("*.csv")[0]
    response = upload_file_to_s3(file_name=file_name, bucket=AWS_BUCKET_NAME, key=file_name)
    print(response)
