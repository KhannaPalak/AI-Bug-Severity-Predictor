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

## ☸️ Production Deployment & Orchestration (Kubernetes)

To prepare this application for enterprise-scale traffic, the microservices are orchestrated using **Kubernetes**. This decouples the frontend user interface from the heavy machine learning inference backend, ensuring high availability, fault tolerance, and isolated scaling.

### System Architecture
The application is split into two primary workloads:
1. **Frontend Pod (`bug-frontend`)**: Runs the Streamlit dashboard, exposed externally via a `NodePort` service.
2. **Backend Pod (`bug-backend`)**: Runs the FastAPI server hosting the trained ML model, kept secure inside the cluster using a `ClusterIP` service.

### Key Architectural Benefits
* **Decoupled Scaling**: If prediction traffic spikes, the backend pod can be scaled independently of the frontend UI.
* **Service Discovery**: The Streamlit container securely communicates with the backend API using Kubernetes internal DNS routing (`http://bug-backend-service:8000`).
* **Self-Healing (Fault Tolerance)**: If a backend container crashes, the Kubernetes Control Plane immediately detects the failure and provisions a healthy replica within milliseconds to maintain zero downtime.

### How to Run Locally

1. **Enable Kubernetes** in your Docker Desktop settings.
2. **Build the local container images**:
   ```bash
   # Build backend
   docker build -t bug-backend:local -f backend/Dockerfile .
   # Build frontend
   docker build -t bug-frontend:local -f frontend/Dockerfile .