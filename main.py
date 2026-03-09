import time
import queue
import random
import threading
import json
import os
from dataclasses import dataclass, asdict
from typing import List, Dict
from enum import Enum

class EventType(Enum):
    SHIPMENT_UPDATE = "shipment_update"
    INVENTORY_CHANGE = "inventory_change"
    ORDER_PLACED = "order_placed"

@dataclass
class Event:
    id: str
    type: EventType
    data: Dict
    timestamp: float
    retries: int = 0

class EventBus:
    def __init__(self):
        self.queues = {
            "shipments": queue.Queue(),
            "inventory": queue.Queue(),
            "orders": queue.Queue()
        }
        self.consumers = {}
        self.metrics = {"processed": 0, "failed": 0, "retries": 0}
        self.persistence_file = "events.log"

    def publish(self, topic: str, event: Event):
        if topic in self.queues:
            self.queues[topic].put(event)
            print(f"📤 Published {event.type.value} to {topic}: {event.id}")
            self.persist_event(event)
        else:
            print(f"⚠️ Unknown topic: {topic}")

    def subscribe(self, topic: str, consumer_func):
        if topic not in self.consumers:
            self.consumers[topic] = []
        self.consumers[topic].append(consumer_func)

    def persist_event(self, event: Event):
        with open(self.persistence_file, "a") as f:
            f.write(json.dumps(asdict(event)) + "\n")

    def load_events(self):
        if os.path.exists(self.persistence_file):
            with open(self.persistence_file, "r") as f:
                for line in f:
                    try:
                        data = json.loads(line.strip())
                        event = Event(**data)
                        self.queues["shipments"].put(event)  # Replay to shipments
                    except:
                        pass

    def process_topic(self, topic: str):
        while True:
            try:
                event = self.queues[topic].get(timeout=1)
                success = False
                for consumer in self.consumers.get(topic, []):
                    try:
                        consumer(event)
                        success = True
                    except Exception as e:
                        print(f"❌ Consumer error: {e}")
                        event.retries += 1
                        self.metrics["retries"] += 1
                        if event.retries < 3:
                            self.queues[topic].put(event)  # Retry
                        else:
                            self.metrics["failed"] += 1
                if success:
                    self.metrics["processed"] += 1
                    self.queues[topic].task_done()
            except queue.Empty:
                break

def shipment_producer(bus: EventBus, count=10):
    statuses = ['in_transit', 'delayed', 'delivered', 'cancelled']
    for i in range(1, count + 1):
        event = Event(
            id=f"ship-{i}",
            type=EventType.SHIPMENT_UPDATE,
            data={"shipment_id": i, "status": random.choice(statuses), "location": f"Hub-{random.randint(1,5)}"},
            timestamp=time.time()
        )
        bus.publish("shipments", event)
        time.sleep(random.uniform(0.2, 0.8))

def inventory_producer(bus: EventBus, count=5):
    for i in range(1, count + 1):
        event = Event(
            id=f"inv-{i}",
            type=EventType.INVENTORY_CHANGE,
            data={"product_id": i, "change": random.randint(-10, 10), "warehouse": f"Warehouse-{random.randint(1,3)}"},
            timestamp=time.time()
        )
        bus.publish("inventory", event)
        time.sleep(random.uniform(0.5, 1.5))

def order_producer(bus: EventBus, count=3):
    for i in range(1, count + 1):
        event = Event(
            id=f"order-{i}",
            type=EventType.ORDER_PLACED,
            data={"order_id": i, "customer_id": random.randint(100, 999), "items": random.randint(1, 5)},
            timestamp=time.time()
        )
        bus.publish("orders", event)
        time.sleep(random.uniform(1, 2))

def shipment_consumer(event: Event):
    print(f"🚚 Processing shipment: {event.data['shipment_id']} - {event.data['status']}")
    # Simulate processing
    time.sleep(0.1)

def inventory_consumer(event: Event):
    print(f"📦 Inventory change: Product {event.data['product_id']} by {event.data['change']}")
    time.sleep(0.1)

def order_consumer(event: Event):
    print(f"🛒 Order placed: {event.data['order_id']} for customer {event.data['customer_id']}")
    time.sleep(0.1)

if __name__ == "__main__":
    print("Starting advanced event-driven logistics simulation...")
    bus = EventBus()
    bus.load_events()  # Replay persisted events

    # Subscribe consumers
    bus.subscribe("shipments", shipment_consumer)
    bus.subscribe("inventory", inventory_consumer)
    bus.subscribe("orders", order_consumer)

    # Start producers
    producers = [
        threading.Thread(target=shipment_producer, args=(bus, 15)),
        threading.Thread(target=inventory_producer, args=(bus, 8)),
        threading.Thread(target=order_producer, args=(bus, 5))
    ]

    # Start consumers
    consumers = [
        threading.Thread(target=bus.process_topic, args=("shipments",)),
        threading.Thread(target=bus.process_topic, args=("inventory",)),
        threading.Thread(target=bus.process_topic, args=("orders",))
    ]

    for p in producers:
        p.start()
    for c in consumers:
        c.start()

    for p in producers:
        p.join()
    for c in consumers:
        c.join()

    print("\n📊 Final Metrics:")
    print(f"  Processed: {bus.metrics['processed']}")
    print(f"  Failed: {bus.metrics['failed']}")
    print(f"  Retries: {bus.metrics['retries']}")
    print("Simulation complete.")

