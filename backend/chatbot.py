
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import os
import requests  # Using requests for synchronous HTTP requests
from dotenv import load_dotenv
from fastapi.middleware.cors import CORSMiddleware

# Load environment variables from .env file
load_dotenv("openai.env")

# Azure OpenAI configuration
AZURE_API_KEY = os.getenv("AZURE_OPENAI_KEY")
AZURE_ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT")  
AZURE_DEPLOYMENT_NAME = os.getenv("AZURE_DEPLOYMENT_NAME")  # Ensure this is the deployment for GPT-3.5 Turbo
AZURE_API_VERSION = "2023-07-01-preview"  # Ensure this is the correct API version for your use case

# FastAPI instance
app = FastAPI()

# Enable CORS for your frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # React frontend
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
)

# Request model for the chat
class ChatRequest(BaseModel):
    prompt: str

# POST endpoint for chatting with OpenAI (via Azure)
@app.post("/chat")
async def chat_with_openai(request: ChatRequest):
    try:
        print(f"Received user message: {request.prompt}")  # Debugging

        # Build the API request URL for GPT-3.5 Turbo
        url = f"{AZURE_ENDPOINT}/openai/deployments/{AZURE_DEPLOYMENT_NAME}/chat/completions?api-version={AZURE_API_VERSION}"

        # Headers for the API request
        headers = {
            "Content-Type": "application/json",
            "api-key": AZURE_API_KEY
        }

        # Request body payload for GPT-3.5 Turbo (based on the chat model)
        body = {
            "messages": [
                {"role": "system", "content": "You are a helpful academic assistant."},
                {"role": "user", "content": request.prompt}
            ],
            "temperature": 0.7,  # Controls randomness; 0 is deterministic, 1 is more random
            "max_tokens": 400 # Limits response length
        }

        # Send the request to Azure OpenAI (GPT-3.5 Turbo)
        response = requests.post(url, headers=headers, json=body, timeout=10)  # Set timeout to 10 seconds

        print(f"Azure OpenAI Response: {response.json()}")  # Debugging response

        # Check the response status
        if response.status_code != 200:
            raise HTTPException(status_code=response.status_code, detail=f"Error: {response.json()}")

        # Parse the response JSON
        result = response.json()
        message = result["choices"][0]["message"]["content"]

        # Return the message content
        return {"response": message.strip()}

    except requests.exceptions.RequestException as e:
        print(f"Request error: {str(e)}")  # Debugging error
        raise HTTPException(status_code=500, detail=f"Request error: {str(e)}")
    except Exception as e:
        print(f"Internal server error: {str(e)}")  # Debugging error
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")