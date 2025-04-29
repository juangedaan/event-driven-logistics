import boto3

dynamodb = boto3.resource('dynamodb', region_name="us-west-2", endpoint_url="http://localhost:8000")

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
    create_shipments_table()

