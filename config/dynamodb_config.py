import os

import boto3


def get_dynamodb_table(table_name="Shipments"):
    # Dummy credentials: DynamoDB Local accepts anything, no real AWS account needed.
    dynamodb = boto3.resource(
        'dynamodb',
        region_name="us-west-2",
        endpoint_url=os.environ.get("DYNAMODB_ENDPOINT", "http://localhost:8000"),
        aws_access_key_id="local",
        aws_secret_access_key="local",
    )
    return dynamodb.Table(table_name)
