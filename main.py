from fastapi import FastAPI
from transformers import pipeline
import logging # <-- NEW: This is the built-in Python tool for keeping a diary

# NEW: Set up the diary (Telemetry)
# It will save everything into a file called "ai_telemetry.log"
logging.basicConfig(
    filename="ai_telemetry.log", 
    level=logging.INFO, 
    format="%(asctime)s - %(message)s"
)

app = FastAPI()

print("Waking up the AI...")
analyzer = pipeline("sentiment-analysis", model="ProsusAI/finbert")

@app.get("/")
def home():
    return {"message": "Hello! The Stock Mood AI is awake and ready."}

@app.get("/analyze")
def analyze_headline(text: str):
    prediction = analyzer(text)
    
    # Extract the exact mood and score
    mood = prediction[0]['label']
    score = prediction[0]['score']
    
    # NEW: Write this prediction into our MLOps diary!
    logging.info(f"Input: '{text}' | Prediction: {mood} | Confidence: {score:.4f}")
    
    return {
        "headline": text,
        "mood_score": prediction
    }