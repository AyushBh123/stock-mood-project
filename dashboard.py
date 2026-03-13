import streamlit as st
import requests

# 1. Set up the page title and description
st.title("📈 Stock Market Mood Ring")
st.write("Enter a financial news headline to see if the market mood is Positive, Negative, or Neutral!")

# 2. Create a text box for the user to type in
headline = st.text_input("News Headline:", placeholder="e.g., Apple stock surges after new iPhone release...")

# 3. Create a button to trigger the AI
if st.button("Analyze Mood"):
    if headline:
        st.info("Asking the AI...")
        
        # 4. Send the headline to our FastAPI server
        try:
            # We are calling our API just like a web browser would!
            response = requests.get(f"http://127.0.0.1:8000/analyze?text={headline}")
            
            if response.status_code == 200:
                result = response.json()
                # Extract the mood and the confidence score from the AI's response
                mood = result["mood_score"][0]["label"]
                confidence = result["mood_score"][0]["score"]
                
                # Display the results beautifully
                st.success(f"**Market Mood:** {mood}")
                st.write(f"**AI Confidence:** {confidence:.2%}")
            else:
                st.error("Oops! Something went wrong with the API.")
                
        except requests.exceptions.ConnectionError:
            st.error("Error: Could not connect to the AI. Is your FastAPI server running?")
            
    else:
        st.warning("Please enter a headline first!")