import os
import json
import boto3

from setup.settings import (
    S3_AWS_REGION,
    S3_ACCESS_KEY,
    S3_SECRET_KEY,
    S3_BUCKET_NAME,
    MS_NAME
)


def get_resource():
    resource = boto3.resource(
        's3',
        region_name=S3_AWS_REGION,
        aws_access_key_id=S3_ACCESS_KEY,
        aws_secret_access_key=S3_SECRET_KEY
    )
    return resource


def put_file_in_s3(resource: boto3, data: dict, **kwargs) -> str:

    rut = kwargs.get('rut')
    json_path = f'./temp/{rut}-upload.json'
    json_string = json.dumps(data)
    json_file = open(json_path, "w")
    json_file.write(json_string)
    json_file.close()

    # It can be modified to upload to a specific folder
    path_to_upload_s3 = f'{MS_NAME}/{rut}/data.json'

    resource.meta.client.upload_file(
        json_file.name,
        S3_BUCKET_NAME,
        path_to_upload_s3
    )

    # La url que se va a guardar en la DB
    url_for_db = f'https://{S3_BUCKET_NAME}.s3.amazonaws.com/{path_to_upload_s3}'

    os.remove(json_path)

    return url_for_db


def download_file_from_s3(resource: boto3, **kwargs) -> dict:

    rut = kwargs.get('rut')
    json_download_path = f'./temp/{rut}-downloaded.json'

    # It can be modified to download from a specific folder
    path_to_download_s3 = f'{MS_NAME}/{rut}/data.json'

    resource.meta.client.download_file(
        S3_BUCKET_NAME,
        path_to_download_s3,
        json_download_path
    )

    json_file = open(json_download_path, "r")
    json_data = json.loads(json_file.read())
    json_file.close()

    os.remove(json_file.name)

    return json_data
