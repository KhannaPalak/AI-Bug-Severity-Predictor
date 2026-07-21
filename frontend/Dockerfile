FROM python:3.10-slim

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends curl && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir uv

COPY frontend/pyproject.toml frontend/uv.lock ./
RUN uv sync --frozen --no-dev --no-editable

COPY frontend/ ./frontend/
COPY models/label_encoder.pkl ./models/

EXPOSE 8501

CMD ["uv", "run", "streamlit", "run", "frontend/app.py", "--server.port=8501", "--server.address=0.0.0.0"]
