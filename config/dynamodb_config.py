import boto3

def get_dynamodb_table(table_name="Shipments"):
    dynamodb = boto3.resource('dynamodb', region_name="us-west-2", endpoint_url="http://localhost:8000")
    return dynamodb.Table(table_name)

