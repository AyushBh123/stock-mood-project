# This imports the open-source AI tool
from transformers import pipeline

print("Loading the AI... (this takes a few seconds)")

# This downloads the specific 'FinBERT' AI model meant for finance
analyzer = pipeline("sentiment-analysis", model="ProsusAI/finbert")

# Here is our test headline
headline = "Apple sales drop by 10% causing panic in the market."

# Let's ask the AI what it thinks of the headline!
result = analyzer(headline)

print(f"Headline: {headline}")
print(f"AI Market Mood: {result}")