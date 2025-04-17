# 🚨 AI-Powered Fraud Detection API

A containerized, cloud-ready fraud detection system powered by machine learning. Designed for high-performance transaction monitoring in financial systems, this API provides real-time fraud predictions and can be seamlessly integrated with banking platforms.

---

## 📊 Dataset Overview

The project uses a preprocessed version of the [Online Payments Fraud Detection Dataset]([https://www.kaggle.com/datasets/ealaxi/paysim1](https://www.kaggle.com/datasets/rupakroy/online-payments-fraud-detection-dataset)), simulating mobile money transactions.

**Dataset columns:**

- `step`: Time step in the simulation
- `type`: Transaction type (`TRANSFER`, `CASH_OUT`, etc.)
- `amount`: Transaction amount
- `oldbalanceOrg`, `newbalanceOrig`: Originator account balances
- `oldbalanceDest`, `newbalanceDest`: Beneficiary account balances
- `isFraud`: Ground truth (0/1)
- `isFlaggedFraud`: Flag indicating suspicious transfers

---

## 🧠 Model Training Pipeline

The ML pipeline was developed using **Scikit-learn**, featuring:

1. **Exploratory Data Analysis** (EDA)
2. **Feature Engineering** & cleaning
3. **Data Balancing** (SMOTE / under-sampling)
4. **Model Training** with:
   - Random Forest
   - LSTM
5. **Evaluation** (Precision, Recall, F1, ROC-AUC)
6. Exported using `joblib` or `pickle`

---

## 🚀 Deployment Options

- 🐳 **Docker**: Containerized REST API
- ☁️ **Kubernetes**: Production-ready, auto-scaled
- 🌍 **Cloud Providers**:
  - AWS (ECS or EKS)
  - GCP (Cloud Run/GKE)
  - Azure (App Services or AKS)

---

## 🔒 API Security

- ✅ Optional JWT-based authentication for endpoints
- 🔐 CORS control enabled
- 🛡️ Can integrate OAuth2.0 for production systems

---

## 🧪 Local Testing

### 🧰 Prerequisites

- Python 3.12
- Docker Desktop with WSL2 (Windows) or Docker Engine (Linux/macOS)

### 🧪 Run Django App Locally (without Docker)

```bash
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
