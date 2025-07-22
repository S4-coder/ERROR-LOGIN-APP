# Use official Python runtime as a parent image
FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y build-essential libssl-dev libffi-dev

# Copy backend requirements
COPY error-logging-app/backend/requirements.txt /app/backend/requirements.txt

# Install backend dependencies
RUN pip install --upgrade pip
RUN pip install -r /app/backend/requirements.txt

# Copy backend source code
COPY error-logging-app/backend /app/backend

# Expose port
EXPOSE 5000

# Set environment variables for Flask
ENV FLASK_APP=/app/backend/src/app.py
ENV FLASK_RUN_HOST=0.0.0.0

# Run the Flask app
CMD ["flask", "run"]
