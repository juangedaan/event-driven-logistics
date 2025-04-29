# Event-Driven Logistics Tracking Platform

Designed a real-time logistics event processing system (#SupplyChainTechnology, #EventDrivenArchitecture) to track shipments, warehouse movements, and customer notifications. Built using Kafka, Python, and DynamoDB to ensure high-throughput, low-latency operations across multiple geographies.

Delivered a merchant-facing dashboard to provide real-time shipment visibility, enhancing platform reliability and operational transparency.

## Architecture Overview

- **Event Source**: Producers emit shipment and warehouse events into Kafka topics.
- **Kafka Broker**: Manages event streaming and distribution.
- **Consumer Service**: Listens to events, processes data, and writes into DynamoDB.
- **DynamoDB**: Stores shipment and warehouse state information.
- **Notifier Service**: Sends real-time updates to customers.
- **Dashboard**: Flask app allowing merchants to view shipment status.

![Architecture Diagram](architecture-diagram.png)

## Project Structure

```
event-driven-logistics/
├── app/
│   ├── producer.py
│   ├── consumer.py
│   ├── notifier.py
│   └── dashboard/
│       ├── app.py
│       ├── templates/
│       │   └── dashboard.html
│       └── static/
│           └── style.css
├── config/
│   ├── kafka_config.py
│   └── dynamodb_config.py
├── deployment/
│   ├── setup_dynamodb.py
│   ├── docker-compose.yml
│   └── requirements.txt
└── scripts/
    └── generate_mock_events.py
```

## How to Run

1. **Set up Kafka and DynamoDB**:
   - Use the provided `docker-compose.yml` to spin up local Kafka and DynamoDB services.

2. **Install dependencies**:
   ```bash
   pip install -r deployment/requirements.txt
   ```

3. **Start the services**:
   - Start Kafka producers (`producer.py`) to simulate shipment events.
   - Start the consumer (`consumer.py`) to process incoming events.
   - Start the notifier (`notifier.py`) to send updates.
   - Launch the dashboard (`dashboard/app.py`) to visualize the shipment status.

4. **(Optional)** Generate mock events:
   ```bash
   python scripts/generate_mock_events.py
   ```

## Key Technologies

- Apache Kafka (event streaming)
- Python (event processing and dashboard)
- Amazon DynamoDB (state storage)
- Flask (dashboard web app)

