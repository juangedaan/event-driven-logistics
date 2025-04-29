import json
import boto3
from kafka import KafkaConsumer
from config.dynamodb_config import get_dynamodb_table

# Initialize Kafka Consumer
consumer = KafkaConsumer(
    'logistics',
    bootstrap_servers='localhost:9092',
    value_deserializer=lambda m: json.loads(m.decode('utf-8')),
    group_id='logistics-consumer-group'
)

# Get DynamoDB Table
table = get_dynamodb_table()

def process_event(event):
    shipment_id = event.get('shipment_id')
    if not shipment_id:
        print("Invalid event, missing shipment_id.")
        return

    table.put_item(Item=event)
    print(f"Stored event: {event}")

if __name__ == "__main__":
    for message in consumer:
        process_event(message.value)

