FROM python:3.11-slim

RUN pip install --no-cache-dir pandas

WORKDIR /app

COPY simulate_data.py .
COPY ALL_DATA_BY_DEP_FINAL_2022.csv .
COPY ALL_DATA_BY_DEP_FINAL_PREDICT_2025.csv .

CMD ["python", "simulate_data.py"]
