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

## ⚙️ DevOps Pipeline & Architecture
Our team implemented a professional MLOps workflow to ensure the AI model can be safely and reliably updated:

1. **Version Control:** All application code, infrastructure blueprints (`Dockerfile`), and dependencies (`requirements.txt`) are tracked in this Git repository.
2. **Continuous Integration (CI):** We established an automated CI pipeline using GitHub Actions (`.github/workflows/docker-build.yml`). Every push to the `main` branch automatically triggers a cloud runner to verify the code.
3. **Automated Build & Test:** The CI pipeline automatically checks out the code and attempts to build the Docker image. If the build fails, the pipeline prevents the broken code from being deployed.
4. **Containerization:** The FastAPI backend and heavy AI dependencies are packaged into an isolated Docker container. This guarantees the application runs consistently across any operating system, eliminating the "it works on my machine" problem.

## 🚀 How to Run the Project Locally

### Prerequisites
* Python 3.9 or higher installed.
* Docker Desktop installed (if you want to run the containerized version).

### Option 1: Running the Full Stack Locally (Two Terminals)
Follow these steps to run the frontend and backend on your local machine:

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
   *The dashboard will automatically open in your web browser at `http://localhost:8501`.*

### Option 2: Running the API via Docker (Containerized)
To test our DevOps containerization, you can run the backend entirely inside Docker:

1. **Build the Docker Image:**
   ```bash
   docker build -t stock-mood-api .
   ```

2. **Run the Container:**
   ```bash
   docker run -p 8000:8000 stock-mood-api
   ```

3. **Test the API:**
   Visit `http://127.0.0.1:8000/docs` in your browser to access the automatic interactive API documentation and test the model directly!

## 👥 Team Members
* **Ayush Bhardwaj** * **Swayam Prakash** * **Lakshay Saharan** ---
*Built for Unit V: DevOps for AI.*