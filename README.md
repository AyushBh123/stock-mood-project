---
title: Stock Mood Ring
emoji: 📈
colorFrom: blue
colorTo: green
sdk: docker
pinned: false
---

# 📈 Stock Market Mood Ring: DevOps for AI Deployment

**Capstone Project 5 - Unit V: DevOps for AI**

## 🎯 Project Overview
This project demonstrates a complete, end-to-end DevOps pipeline for an Artificial Intelligence application. Rather than simply training a standalone machine learning model, this capstone focuses on the **deployment, containerization, and automation** of an AI service using modern open-source frameworks.

The application itself is a "Market Mood Ring." It analyzes real-time financial news headlines and predicts the market sentiment (Positive, Negative, or Neutral) using a pre-trained Natural Language Processing (NLP) model.

## 🛠️ Technology Stack
We utilized entirely open-source frameworks to build this pipeline:
* **AI Model:** FinBERT (via Hugging Face `transformers` & `torch`)
* **Backend API:** FastAPI & Uvicorn (Python)
* **Frontend Dashboard:** Streamlit
* **Containerization:** Docker
* **CI/CD Automation:** GitHub Actions
* **Version Control:** Git & GitHub

## ⚙️ DevOps Pipeline, MLOps, & Architecture
Our team implemented a professional MLOps workflow to ensure the AI model can be safely updated and monitored in production:

1. **Version Control:** All code and infrastructure blueprints are tracked in Git.
2. **Continuous Integration (CI):** GitHub Actions automatically checks out the code and builds the Docker image to test for breaking changes.
3. **Continuous Deployment (CD) - "The Final Mile":** If the CI tests pass, GitHub Actions automatically force-pushes the stable Docker container to **Hugging Face Spaces**. Minutes after a developer writes code, it is live on the internet without manual intervention.
4. **Containerization:** The application is packaged into an isolated Docker container, eliminating the "it works on my machine" problem.
5. **MLOps Telemetry & Monitoring:** To monitor model degradation and "data drift" in the real world, the FastAPI backend implements secure logging. Every prediction's input, output, and confidence score is logged to `ai_telemetry.log` to evaluate the AI's health during volatile market conditions.

## 🚀 How to Run the Project Locally

### Prerequisites
* Python 3.9 or higher installed.
* Docker Desktop installed (if you want to run the containerized version).

### Option 1: Running the Full Stack Locally (Two Terminals)
1. **Clone this repository:**
   ```bash
   git clone [https://github.com/YOUR_USERNAME/stock-mood-project.git](https://github.com/YOUR_USERNAME/stock-mood-project.git)
   cd stock-mood-project
   ```

2. **Install the required dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Start the AI Backend API (Terminal 1):**
   ```bash
   uvicorn main:app --reload
   ```

4. **Start the User Interface Dashboard (Terminal 2):**
   Open a second terminal window and run:
   ```bash
   streamlit run dashboard.py
   ```

### Option 2: Running the API via Docker (Containerized)
1. **Build the Docker Image:**
   ```bash
   docker build -t stock-mood-api .
   ```

2. **Run the Container:**
   ```bash
   docker run -p 8000:8000 stock-mood-api
   ```
   *Visit `http://127.0.0.1:8000/docs` in your browser to test the API!*

## 👥 Team Members
* **[Your Name Here]** * **[Teammate 1 Name Here]** * **[Teammate 2 Name Here]** ---
*Built for Unit V: DevOps for AI.*