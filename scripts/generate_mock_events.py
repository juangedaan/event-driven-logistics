import json
import random
import time
from kafka import KafkaProducer

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

shipment_ids = [f"SHIP{2000 + i}" for i in range(50)]
statuses = ["created", "picked_up", "in_transit", "delayed", "delivered"]
locations = ["New York", "Chicago", "Los Angeles", "Miami", "Dallas"]

def generate_mock_event():
    return {
        "shipment_id": random.choice(shipment_ids),
        "location": random.choice(locations),
        "status": random.choice(statuses),
        "timestamp": int(time.time())
    }

if __name__ == "__main__":
    for _ in range(100):
        event = generate_mock_event()
        producer.send("logistics", event)
        print(f"Mock event sent: {event}")
        time.sleep(0.5)  # Send every half a second

