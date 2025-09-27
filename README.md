# 🐳 – AI Bot

An AI-powered pizza ordering assistant with a FastAPI backend and Gradio frontend. Run locally using Docker for easy setup.

---

## 🔨 Build & Run with Docker

```bash
# Build Docker image
docker build -t pizzabot .

# Run container
docker run -p 8000:8000 -p 7860:7860 pizzabot
