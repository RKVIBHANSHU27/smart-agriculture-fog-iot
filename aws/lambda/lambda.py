import json
import boto3
from decimal import Decimal

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table("SmartAgricultureTelemetry")

def lambda_handler(event, context):

    print("Received Event:")
    print(event)

    for record in event["Records"]:

        message = json.loads(
            record["body"],
            parse_float=Decimal
        )

        table.put_item(Item=message)

        print(f"Stored record for {message['device_id']}")

    return {
        "statusCode": 200,
        "body": "Success"
    }