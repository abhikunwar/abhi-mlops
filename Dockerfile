# Use an official Python runtime as a parent image
FROM python:3.9-slim
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV GOOGLE_APPLICATION_CREDENTIALS="/tmp/gcp-key.json"
WORKDIR /app
RUN apt-get update && apt-get install -y \
    libgomp1 \
    && rm -rf /var/lib/apt/lists/*
COPY requirements.txt /app/
RUN pip install --upgrade pip && pip install -r requirements.txt
COPY . /app/
RUN pip install -e .
EXPOSE 8080

# Run both model training and prediction in the same container
CMD ["bash", "-c", "python pipeline/model_training_pipeline.py && python pipeline/model_prediction.py"]
