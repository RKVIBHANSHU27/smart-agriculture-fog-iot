#  Smart Agriculture Fog Monitoring System

## Overview

Smart Agriculture Fog Monitoring System is an IoT-based monitoring platform that collects sensor data from multiple agricultural devices, processes data at the fog layer, detects abnormal conditions, and displays real-time information through a web dashboard.

The system uses fog computing to reduce cloud processing delays by performing aggregation and alert detection closer to the edge.

---

## Architecture

IoT Sensors
|
|
Sensor Simulator
|
|
Fog Layer
(Validation + Aggregation + Alert Detection)
|
|
AWS SQS
|
|
DynamoDB
|
|
FastAPI Backend
|
|
React Dashboard


---

## Features

- Real-time agriculture sensor monitoring
- Multiple IoT devices simulation
- Fog layer data processing
- Sensor data aggregation
- Alert detection system
- Warning and critical monitoring
- Live dashboard updates
- Sensor analytics charts
- Latest telemetry table

---

## Sensors Used

Each device contains:

- Temperature sensor
- Humidity sensor
- Soil moisture sensor
- Light sensor
- CO₂ sensor

Current simulation:

- 5 IoT devices
- 5 sensor types
- 25 telemetry readings per cycle

---

## Technologies Used

### Backend
- Python
- FastAPI
- AWS DynamoDB
- AWS SQS

### Frontend
- React.js
- Recharts
- CSS

### Cloud Services
- AWS DynamoDB
- AWS SQS
- AWS EC2

---

## Project Structure
smart-agriculture-fog-iot

├── backend
│ ├── app.py
│ ├── routes.py
│ └── database.py
│
├── dashboard
│ ├── src
│ ├── components
│ └── services
│
├── fog
│ ├── fog_node.py
│ ├── alert_manager.py
│ └── aggregator.py
│
├── sensors
│ ├── simulator.py
│ └── device.py
│
├── config
│ └── config.py



---

## Running the Project

### 1. Start Backend

Create virtual environment: python -m venv venv

Activate: source venv/bin/activate

Install dependencies: pip install -r requirements.txt

Run FastAPI: uvicorn backend.app:app --host 0.0.0.0 --port 8080

### 2. Start Sensor Simulator

Run: python -m sensors.simulator


The simulator generates sensor readings and sends processed data through the fog layer.

---

### 3. Start Dashboard

Go to dashboard folder: cd dashboard


Install packages: npm install

Run: npm run dev 


---

## Dashboard Capabilities

The dashboard provides:

- Device status
- Sensor summary
- Fog node monitoring
- Active alerts
- Real-time sensor analytics
- Latest processed telemetry

---

## Alert System

The fog layer detects abnormal sensor values:

Examples:

- High CO₂ levels
- High temperature
- Low humidity
- Low soil moisture

Alerts are displayed as:

-  Normal
-  Warning
-  Critical

---

## Future Improvements

- Deploy backend using AWS Elastic Beanstalk
- Add notification service
- Add more IoT devices
- Add machine learning based prediction

---

## Author

Vibhanshu Raju Khobragade
25164589
Fog & Edge Computing
MSc Cloud Computing Project

