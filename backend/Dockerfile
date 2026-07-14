FROM python:3.10-slim

WORKDIR /app

# Copy requirements first to leverage caching
COPY backend/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# COPY THE MODEL DIRECTORY FROM THE ROOT CONTEXT INTO THE BACKEND
COPY models/ /app/models/

# Copy the rest of the backend application code
COPY backend/ .

EXPOSE 8000

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]