import json
import time
import random
from kafka import KafkaProducer

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

shipment_ids = [f"SHIP{1000 + i}" for i in range(10)]
statuses = ["created", "picked_up", "in_transit", "delayed", "delivered"]

def generate_event():
    return {
        "shipment_id": random.choice(shipment_ids),
        "location": random.choice(["Berlin", "Madrid", "London", "Paris", "Warsaw"]),
        "status": random.choice(statuses),
        "timestamp": int(time.time())
    }

if __name__ == "__main__":
    while True:
        event = generate_event()
        producer.send("logistics", event)
        print(f"Produced: {event}")
        time.sleep(2)

