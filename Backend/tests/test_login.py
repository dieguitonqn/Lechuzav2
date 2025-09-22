import pytest
from main import app
from fastapi.testclient import TestClient
from Backend.models.users import User
from schemas import UserCreate


client = TestClient(app)

def test_login():
    userData = {
        "email": "admin@email.com",
        "password": "admin-password"
    }
    response = client.post("api/auth/login", json=userData)
    assert response.status_code == 200
    assert response.json()=={
        "access_token": userData["email"],
        "token_type": "bearer",
        "message": "Login successful"
    }

    # assert "access_token" in response.json()