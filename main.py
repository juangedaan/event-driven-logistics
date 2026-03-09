import time
import queue
import random
import threading

# simple in-memory queue to simulate Kafka
event_queue = queue.Queue()

# producer pushes events

def producer(count=5):
    statuses = ['in_transit', 'delayed', 'delivered']
    for i in range(1, count + 1):
        event = {'shipment_id': i, 'status': random.choice(statuses)}
        print(f"[Producer] emitting event: {event}")
        event_queue.put(event)
        time.sleep(random.uniform(0.1, 0.5))

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
    # run producer and consumer in separate threads to mimic asynchronous flow
    t1 = threading.Thread(target=producer, args=(10,))
    t2 = threading.Thread(target=consumer)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print("Simulation complete.")

