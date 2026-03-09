import time
import queue

# simple in-memory queue to simulate Kafka
event_queue = queue.Queue()

# producer pushes events

def producer():
    for i in range(1, 6):
        event = {'shipment_id': i, 'status': 'in_transit'}
        print(f"[Producer] emitting event: {event}")
        event_queue.put(event)
        time.sleep(0.5)

# consumer processes events

def consumer():
    while True:
        try:
            event = event_queue.get(timeout=2)
        except queue.Empty:
            break
        print(f"[Consumer] processing event: {event}")
        event_queue.task_done()

if __name__ == "__main__":
    print("Starting event-driven logistics simulation...")
    producer()
    consumer()
    print("Simulation complete.")

