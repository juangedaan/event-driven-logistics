import time
import boto3
from boto3.dynamodb.conditions import Attr
from config.dynamodb_config import get_dynamodb_table

# Initialize DynamoDB table
table = get_dynamodb_table()

def check_for_updates():
    # Scan for shipments that are not yet notified (mocked by missing "notified" attribute)
    response = table.scan(
        FilterExpression=Attr('notified').not_exists()
    )
    return response.get('Items', [])

def send_notification(shipment):
    print(f"Sending notification: Shipment {shipment['shipment_id']} is {shipment['status']} at {shipment['location']}")
    # Mark as notified (mock notification)
    table.update_item(
        Key={'shipment_id': shipment['shipment_id']},
        UpdateExpression="SET notified = :val",
        ExpressionAttributeValues={':val': True}
    )

if __name__ == "__main__":
    while True:
        updates = check_for_updates()
        for shipment in updates:
            send_notification(shipment)
        time.sleep(5)

