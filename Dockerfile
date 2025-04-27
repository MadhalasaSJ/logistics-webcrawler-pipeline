# Dockerfile

# Use lightweight Python 3.11 slim image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy project files into the container
COPY . /app

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Set environment variables if needed
ENV AIRFLOW_HOME=/app/airflow_home

# Create folders for Airflow logs (if needed)
RUN mkdir -p /app/airflow_logs /app/airflow_plugins

# Default command (can override if needed)
CMD ["airflow", "standalone"]

