import time
import json
import boto3

from setup.settings import (
    CLOUDWATCH_AWS_REGION,
    CLOUDWATCH_ACCESS_KEY,
    CLOUDWATCH_SECRET_KEY,
    CLOUDWATCH_GROUP_NAME
)


def get_client():
    client = boto3.client(
        'logs',
        region_name=CLOUDWATCH_AWS_REGION,
        aws_access_key_id=CLOUDWATCH_ACCESS_KEY,
        aws_secret_access_key=CLOUDWATCH_SECRET_KEY,
    )
    return client


def put_log(message, http_message):
    client = get_client()
    try:
        client.create_log_group(
            logGroupName=CLOUDWATCH_GROUP_NAME)
    except client.exceptions.ResourceAlreadyExistsException:
        pass
    try:
        client.create_log_stream(
            logGroupName=CLOUDWATCH_GROUP_NAME,
            logStreamName=http_message
        )
    except client.exceptions.ResourceAlreadyExistsException:
        pass

    response = client.describe_log_streams(
        logGroupName=CLOUDWATCH_GROUP_NAME,
        logStreamNamePrefix=http_message
    )

    event_log = {
        "logGroupName": CLOUDWATCH_GROUP_NAME,
        "logStreamName": http_message,
        "logEvents": [
            {
                'timestamp': int(round(time.time() * 1000)),
                'message': json.dumps(message, separators=(',', ':'))
            }
        ]
    }
    if 'uploadSequenceToken' in response['logStreams'][0]:
        event_log.update(
            {'sequenceToken': response['logStreams'][0]['uploadSequenceToken']})
    response = client.put_log_events(**event_log)
