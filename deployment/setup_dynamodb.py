import os
import time

import boto3

# Dummy credentials: DynamoDB Local accepts anything, no real AWS account needed.
dynamodb = boto3.resource(
    'dynamodb',
    region_name="us-west-2",
    endpoint_url=os.environ.get("DYNAMODB_ENDPOINT", "http://localhost:8000"),
    aws_access_key_id="local",
    aws_secret_access_key="local",
)


def wait_for_dynamodb(retries=30):
    for attempt in range(retries):
        try:
            dynamodb.meta.client.list_tables()
            return
        except Exception:
            print("Waiting for DynamoDB Local to be ready...")
            time.sleep(2)
    raise RuntimeError("DynamoDB Local not reachable. Is `make run-localstack` running?")


def create_shipments_table():
    table_name = "Shipments"
    existing_tables = dynamodb.meta.client.list_tables()['TableNames']
    if table_name in existing_tables:
        print(f"Table {table_name} already exists.")
        return

    table = dynamodb.create_table(
        TableName=table_name,
        KeySchema=[
            {
                'AttributeName': 'shipment_id',
                'KeyType': 'HASH'  # Partition key
            }
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'shipment_id',
                'AttributeType': 'S'
            }
        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 5,
            'WriteCapacityUnits': 5
        }
    )

    print(f"Creating table {table_name}...")
    table.wait_until_exists()
    print(f"Table {table_name} is ready.")


if __name__ == "__main__":
    wait_for_dynamodb()
    create_shipments_table()
