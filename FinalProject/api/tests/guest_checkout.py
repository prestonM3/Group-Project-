import pytest
from fastapi.testclient import TestClient
from ..main import app

# Create a client that talks to your FastAPI app
client = TestClient(app)

def test_guest_checkout_lifecycle():
    # 1. Test Creating a Guest Checkout
    payload = {
        "customer_name": "Test User",
        "phone_number": "555-0199",
        "delivery_or_takeout": "Takeout",
        "delivery_address": "",
        "summary": "1x Test Burger"
    }
    
    # Send the data to your endpoint (adjust the URL path if needed)
    response = client.post("/guest_checkout/", json=payload)
    
    # Assert that the database saved it and returned success
    assert response.status_code == 200 or response.status_code == 201
    data = response.json()
    assert data["customer_name"] == "Test User"
    assert "id" in data
    
    # Grab the ID to check if reading works too
    checkout_id = data["id"]
    
    # 2. Test Reading the Checkout back
    get_response = client.get(f"/guest_checkout/{checkout_id}")
    assert get_response.status_code == 200
    assert get_response.json()["summary"] == "1x Test Burger"