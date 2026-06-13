# BugSight AI Architecture

GitHub Issues / JIRA
        |
        V
Bug Ingestion Layer
        |
        V
PostgreSQL
        |
        V
Feature Engineering
(Text + Metadata)
        |
        V
Severity Prediction Model
(TF-IDF → DistilBERT)
        |
        V
FastAPI
        |
        V
React Dashboard
        |
        V
Monitoring Stack
(Prometheus + Grafana)