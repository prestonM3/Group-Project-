from fastapi.testclient import TestClient
from fastapi import HTTPException
from sqlalchemy.exc import SQLAlchemyError
from ..controllers import orders as controller
from ..main import app
import pytest
from ..models import orders as model
from sqlalchemy import null
from datetime import datetime

# Create a test client for the app
client = TestClient(app)


@pytest.fixture
def db_session(mocker):
    return mocker.Mock()


def test_order(db_session):
    # Create a sample order
    order_data = {
        "customer_name": "John Doe",
        "phone_number": "1234567890",
        "delivery_or_takeout": "delivery",
        "delivery_address": "123 Street Rd.",
        "summary": "Test order",

    }

    order_object = model.Order(**order_data)

    # Call the create function
    created_order = controller.create(db_session, order_object)

    # Assert that the database returned success
    order_get = client.get(f"/orders/")
    assert order_get.status_code == 200

    # Assert that the post was accurate and reading works
    assert created_order is not None
    assert created_order.customer_name == "John Doe"
    assert created_order.summary == "Test order"
    assert created_order.phone_number == "1234567890"
    assert created_order.delivery_or_takeout == "delivery"
    assert created_order.delivery_address == "123 Street Rd."
    db_session.add.assert_called_once()
    db_session.commit.assert_called_once()
    db_session.refresh.assert_called_once()
