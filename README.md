
# 💰 Finance AI Assistant

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-API-green?logo=fastapi)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Database-blue?logo=postgresql)
![Docker](https://img.shields.io/badge/Docker-Containerization-blue?logo=docker)
![Redis](https://img.shields.io/badge/Redis-Cache-red?logo=redis)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-ML-orange?logo=scikit-learn)
![License](https://img.shields.io/badge/License-MIT-green)

A **containerized machine learning powered personal finance analytics platform** built using Python.

The system ingests large financial transaction datasets and applies machine learning to perform:

- Transaction categorization
- Fraud detection
- Spending prediction
- Customer segmentation

Everything runs locally using **Docker**, including the database, API, ML models, and frontend dashboard.

---

# 🚀 Features

## 📥 Transaction Ingestion
- Upload large CSV datasets
- Store transactions in PostgreSQL
- Handle **100k+ transaction datasets**

## 🤖 Machine Learning Models

| Model | Purpose |
|------|------|
| Logistic Regression | Transaction categorization |
| Isolation Forest | Fraud detection |
| Linear Regression | Spending prediction |
| KMeans | Customer segmentation |

## 📊 Analytics APIs

```
GET /analytics/spending
GET /analytics/fraud
GET /analytics/predict
GET /analytics/cluster
```

## 🖥 Web Interface

- CSV upload interface
- Dashboard for analytics
- Built with **HTML + jQuery + TailwindCSS**

---

# 🏗 Architecture

```
Browser
   │
Frontend (HTML + jQuery + Tailwind)
   │
FastAPI Backend
   │
Service Layer
   │
Machine Learning Models
   │
PostgreSQL Database
   │
Redis Queue + Celery Workers
```

This architecture mimics the design used in many **modern fintech analytics platforms**.

---

# 🗂 Project Structure

```
finance-ai-assistant
│
├── docker-compose.yml
├── requirements.txt
├── README.md
│
├── docker
│   ├── web.Dockerfile
│   └── worker.Dockerfile
│
├── src
│   ├── app
│   │   ├── main.py
│   │   ├── db.py
│   │   ├── models.py
│   │   │
│   │   ├── api
│   │   │   ├── transactions.py
│   │   │   └── analytics.py
│   │   │
│   │   ├── finance
│   │   │   ├── anomaly_detection.py
│   │   │   ├── forecasting.py
│   │   │   ├── clustering.py
│   │   │   └── categorizer.py
│   │   │
│   │   └── services
│   │       └── finance_service.py
│   │
│   └── workers
│       ├── celery_app.py
│       └── tasks.py
│
├── frontend
│   ├── index.html
│   ├── dashboard.html
│   ├── js
│   └── css
│
└── data
    ├── csv
    └── models
```

---

# 🧰 Technology Stack

## Backend
- Python
- FastAPI
- SQLAlchemy
- PostgreSQL

## Machine Learning
- Pandas
- NumPy
- Scikit-Learn
- Joblib

## Infrastructure
- Docker
- Docker Compose
- Redis
- Celery

## Frontend
- HTML
- jQuery
- TailwindCSS

---

# 📂 Dataset Format

Example transaction dataset format:

```
transaction_id,user_id,date,amount,merchant,category,payment_method,city,currency,is_fraud
a1,101,2024-01-01,20,Starbucks,Food,UPI,Chennai,INR,0
b2,101,2024-01-02,150,Amazon,Shopping,Credit Card,Bangalore,INR,0
```

The system can easily process **100,000+ transactions**.

---

# ⚙️ Running the Project

## 1️⃣ Install Requirements

You only need:

- Docker
- Docker Compose

---

## 2️⃣ Start the Application

```
docker compose up --build
```

---

## 3️⃣ Access the Application

Frontend

```
http://localhost:8000/frontend/index.html
```

API Docs

```
http://localhost:8000/docs
```

---

# 📊 Example APIs

### Spending Summary

```
GET /analytics/spending
```

### Fraud Detection

```
GET /analytics/fraud
```

### Spending Prediction

```
GET /analytics/predict
```

### Customer Segmentation

```
GET /analytics/cluster
```

---

# 🧠 Machine Learning Pipeline

### Transaction Categorization
Uses **Logistic Regression** with merchant name features.

### Fraud Detection
Uses **Isolation Forest** for anomaly detection.

### Spending Forecasting
Uses **Linear Regression** on spending trends.

### Customer Segmentation
Uses **KMeans clustering** to group users based on spending.

---

# 🧪 Development Commands

Start system

```
docker compose up
```

Stop system

```
docker compose down
```

Rebuild containers

```
docker compose up --build
```

---

# 📈 Future Enhancements

Possible improvements include:

- Real-time transaction ingestion with Kafka
- Advanced fraud detection models
- Feature engineering pipelines
- Interactive dashboards
- Model monitoring and retraining

---

# 📜 License

MIT License

---

# ⭐ Contributing

Pull requests are welcome!  
If you would like to contribute improvements or features, feel free to fork the repository.

---

# 🧑‍💻 Author

Developed as a **machine learning + backend engineering project** demonstrating how financial data analytics systems can be built using Python and modern infrastructure tools.

