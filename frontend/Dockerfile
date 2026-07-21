FROM python:3.10-slim

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends curl && rm -rf /var/lib/apt/lists/*

# Copy and install frontend dependencies
COPY frontend/requirements.txt ./frontend/
RUN pip install --no-cache-dir -r frontend/requirements.txt

# Copy frontend code preserving directory structure
COPY frontend/ ./frontend/

# Copy label encoder for 16->5 severity mapping
COPY models/label_encoder.pkl ./models/

EXPOSE 8501

CMD ["streamlit", "run", "frontend/app.py", "--server.port=8501", "--server.address=0.0.0.0"]
