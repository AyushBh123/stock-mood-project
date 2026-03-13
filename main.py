from fastapi import FastAPI
from transformers import pipeline

# 1. Create the API application (This is our "waiter")
app = FastAPI()

# 2. Load the AI Brain (This is our "kitchen")
# We do this up here so it only has to load once when the server starts!
print("Waking up the AI...")
analyzer = pipeline("sentiment-analysis", model="ProsusAI/finbert")

# 3. Create a route to test if the server is awake
@app.get("/")
def home():
    return {"message": "Hello! The Stock Mood AI is awake and ready."}

# 4. Create the route where we send the headlines
@app.get("/analyze")
def analyze_headline(text: str):
    # The AI looks at the text and gives a score
    prediction = analyzer(text)
    return {
        "headline": text,
        "mood_score": prediction
    }