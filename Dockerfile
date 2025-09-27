# Use official Python image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy app code
COPY . .

# Expose both FastAPI (8000) and Gradio (7860)
EXPOSE 8000 7860

# Run both FastAPI & Gradio UI
CMD uvicorn main:app --host 0.0.0.0 --port 8000 & python ui.py
