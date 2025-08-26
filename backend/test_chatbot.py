import pytest
from fastapi.testclient import TestClient
from chatbot import app

client = TestClient(app)

def test_chat_endpoint():
    """Test the chat endpoint with a simple message"""
    response = client.post(
        "/chat",
        json={"prompt": "Hello, how are you?"}
    )
    
    assert response.status_code == 200
    assert "text" in response.json()
    assert "references" in response.json()
    assert isinstance(response.json()["text"], str)
    assert isinstance(response.json()["references"], list)

def test_chat_endpoint_empty_prompt():
    """Test the chat endpoint with empty prompt"""
    response = client.post(
        "/chat",
        json={"prompt": ""}
    )
    
    # Should still return 200 but with empty response handling
    assert response.status_code == 200
    assert "text" in response.json()

def test_chat_endpoint_missing_prompt():
    """Test the chat endpoint with missing prompt field"""
    response = client.post(
        "/chat",
        json={}
    )
    
    # Should return 422 Unprocessable Entity
    assert response.status_code == 422

def test_health_check():
    """Test that the server is running"""
    response = client.get("/")
    assert response.status_code in [200, 404]  # 200 if React build exists, 404 otherwise

if __name__ == "__main__":
    pytest.main([__file__, "-v"])
