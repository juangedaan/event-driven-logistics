# Event-Driven Logistics Tracking Platform

This project implements a real-time event-driven logistics tracking platform leveraging **Kafka**, **Python**, **DynamoDB**, and **Flask**.  
It enables merchants to monitor shipments, warehouse movements, and receive customer notifications across multiple geographies with minimal latency.

Built around an **event-driven architecture** (#SupplyChainTechnology, #EventDrivenArchitecture), the system is designed for **high-throughput**, **low-latency** operations and transparent, real-time merchant-facing dashboards.

---

## 📈 Architecture Overview

The system processes shipment events through the following components:

- **Event Source**: Producers emit shipment and warehouse events into Kafka topics.
- **Kafka Broker**: Handles event streaming and distribution.
- **Consumer Service**: Processes events and writes shipment updates to DynamoDB.
- **DynamoDB**: Stores real-time shipment and warehouse states.
- **Notifier Service**: Sends real-time customer notifications.
- **Dashboard**: Flask-based merchant dashboard for shipment visibility.

<br>

![Architecture Diagram](architecture-diagram.png)

---

## 🗂️ Project Structure

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
├── scripts/
│   └── generate_mock_events.py
├── main.py
├── Makefile
└── run-tmux.sh
```

---

## 🚀 How to Run

### 1. Prerequisites
- Python 3.7+
- Docker
- Docker Compose
- Tmux

Install Python libraries:

```bash
pip3 install -r deployment/requirements.txt
```

---

### 2. Start Local Services

Spin up **Kafka**, **Zookeeper**, and **DynamoDB Local**:

```bash
docker-compose -f deployment/docker-compose.yml up -d
```

Create the **DynamoDB Shipments table**:

```bash
python3 deployment/setup_dynamodb.py
```

---

### 3. Launch Platform using Tmux

All components (consumer, producer, notifier, dashboard) can be launched automatically in isolated Tmux windows:

```bash
TMUX="" ./run-tmux.sh
```

This script will:
- Start Docker containers
- Launch consumer service
- Launch producer service
- Launch notifier
- Launch Flask dashboard
- Open a DynamoDB scanner window
- Attach to a unified Tmux session (`logistics`)

**💡** You can reattach to the Tmux session anytime:

```bash
tmux attach -t logistics
```

---

### 4. Access the Dashboard

Once everything is running, open:

```
http://localhost:5000
```

You will see a live dashboard updating with shipment statuses.

---

## 🛠️ Key Technologies

- **Apache Kafka** (event streaming)
- **Python 3** (services and dashboard)
- **Amazon DynamoDB Local** (shipment state storage)
- **Flask** (dashboard web app)
- **Docker Compose** (local environment setup)
- **Tmux** (multi-service orchestration)

---

## 📸 Screenshots

### 🧪 Terminal: Event Producer and Consumer in Action

Real-time processing of shipment events flowing through Kafka into DynamoDB:

![Producer & Consumer Screenshot](screenshot.png)

---

### 📊 Real-Time Merchant Dashboard

Dynamic view of shipment tracking and status visibility for merchants:

![Dashboard Screenshot](dashboard.png)

---

## 📜 License

This project is licensed under the [MIT License](LICENSE).

---

## ✨ Future Enhancements

- Integrate Schema Registry for Kafka payload validation.
- Add authentication to merchant dashboard.
- Extend event source to external IoT device simulation.
- Deploy scalable version on AWS Managed Kafka + DynamoDB Global Tables.

