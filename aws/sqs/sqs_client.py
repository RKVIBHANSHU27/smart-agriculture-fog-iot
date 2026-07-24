import boto3

from config.config import AWS_REGION


class SQSClient:

    def __init__(self):

        self.client = boto3.client(
            "sqs",
            region_name=AWS_REGION
        )