# BugSight AI
---
title: BugSight AI
emoji: 🐞
colorFrom: blue
colorTo: purple
sdk: streamlit
sdk_version: "1.45.0"
python_version: "3.10"
app_file: app.py
pinned: false
---

# BugSight AI

AI-Powered Bug Severity Prediction and Automated Triage Platform

## Team Members
- Palak Khanna
- Ahana Arora 

## Tech Stack
- Python
- FastAPI
- React
- PostgreSQL
- Scikit-Learn
- Transformers (BERT)
- Docker
- GitHub Actions
- MLflow
- DVC
- Prometheus
- Grafana

## Project Goal
Automatically predict bug severity levels (Critical, High, Medium, Low) using NLP and metadata analysis to improve software bug triage and prioritization.

# 🐞 AI-Driven Bug Severity Predictor

An end-to-end MLOps pipeline that classifies the severity of incoming software bug reports using Machine Learning, containerized with **Docker**, and deployed live on the cloud using **Render** via a multi-service blueprint framework.

---

## 🏗️ System Architecture

This project utilizes a decoupled cloud microservices architecture to ensure the machine learning inference backend can scale independently of the user interface.

* **Frontend Cloud Service**: A **Streamlit** dashboard providing an interactive UI for developers to submit bug reports. Deployed as a public web service.
* **Backend Cloud Service**: An asynchronous **FastAPI** service that loads the trained scikit-learn model weights and exposes a REST API endpoint. 
* **Infrastructure as Code (IaC)**: Managed via a unified `render.yaml` blueprint configuration, connecting the microservices automatically upon code pushes.
* **Experiment Tracking**: Managed via **MLflow** to monitor hyperparameter runs and version control model binaries.

---

## 🛠️ Tech Stack

* **ML / NLP**: Python, Scikit-Learn, Pandas
* **Model Tracking**: MLflow
* **APIs & UI**: FastAPI, Streamlit
* **Cloud & DevOps**: Render Platform, Docker, GitHub Actions (CI/CD)

---

## 🚀 Cloud Deployment Architecture

We leverage Render's declarative blueprint layout to deploy both components straight from our Git repository context:

### Key Engineering Benefits
* **Continuous Deployment (CD)**: Any push to the `main` branch of this repository triggers an automated Docker rebuild and zero-downtime rolling update on Render.
* **Isolated Environments**: Both the UI and ML inference engine run in independent, isolated Linux containers, reducing resource contention.

### Live Application URLs
* **Frontend UI**: `https://bug-frontend-service.onrender.com` *(Replace with your actual URL)*
* **Backend API**: `https://bug-backend-service.onrender.com` *(Replace with your actual URL)*