# 1. Start with a computer that already has Python 3.9 installed
FROM python:3.9-slim

# 2. Create a folder inside our container called /app
WORKDIR /app

# 3. Copy our packing list into the container first
COPY requirements.txt .

# 4. Tell the container to install all our "Free Legos" 
# (Warning: Downloading the AI brain inside Docker takes a few minutes!)
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copy the rest of our code (main.py, etc.) into the container
COPY . .

# 6. Tell the container how to start our "waiter" when it turns on
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]