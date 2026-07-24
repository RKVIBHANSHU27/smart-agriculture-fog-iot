import json

from config.config import SQS_QUEUE_URL
from aws.sqs.sqs_client import SQSClient


class SQSDispatcher:

    def __init__(self):

        self.client = SQSClient().client

    def send(self, data):

        response = self.client.send_message(
            QueueUrl=SQS_QUEUE_URL,
            MessageBody=json.dumps(data)
        )

        print(
            f"Message sent to SQS: {response['MessageId']}"
        )