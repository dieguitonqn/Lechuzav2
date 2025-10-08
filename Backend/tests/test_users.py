
import pytest
from main import app
from fastapi.testclient import TestClient
from Backend.models.users import User

client = TestClient(app)
@pytest.mark.skip(reason="Test en desarrollo")

def test_create_user():
    user_data = {
        'email': "prueba6@email.com",
        'password': "password123",
    }
    resp = client.post("/api/user/create", json=user_data)
    assert resp.status_code == 201
    response_data = resp.json()
    user_data = {
        'id': response_data.get('id'),
        'name': None,
        'email': user_data['email'],
        'is_active': True,
        'is_verified': False,
        'is_admin': False
    }
    # The password should not be returned by the API
    # We check that all other fields match
    # This will raise a validation error if the response doesn't match the User model
    user_instance = User.model_validate(resp.json())
    assert isinstance(user_instance, User)

    assert resp.json().get('email') == user_data['email']