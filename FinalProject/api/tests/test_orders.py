from fastapi.testclient import TestClient
from fastapi import HTTPException
from sqlalchemy.exc import SQLAlchemyError
from ..controllers import orders as controller
from ..main import app
import pytest
from ..models import orders as model
from sqlalchemy import null

# Create a test client for the app
client = TestClient(app)


@pytest.fixture
def db_session(mocker):
    return mocker.Mock()


def test_create_order(db_session):
    # Create a sample order
    order_data = {
        "customer_name": "John Doe",
        "phone_number": "1234567890",
        "is_delivery": True,
        "delivery_address": "123 Street Rd.",
        "summary": "Test order",
        "promo_code_id": null()
    }

    order_object = model.Order(**order_data)

    # Call the create function
    created_order = controller.create(db_session, order_object)

    # Assertions
    assert created_order is not None
    assert created_order.customer_name == "John Doe"
    assert created_order.summary == "Test order"
    assert created_order.phone_number == "1234567890"
    assert created_order.is_delivery == True
    assert created_order.delivery_address == "123 Street Rd."
    assert created_order.promo_code_id == null()
    db_session.add.assert_called_once()
    db_session.commit.assert_called_once()
    db_session.refresh.assert_called_once()

def test_create_order_db_error(db_session):
    pass

def test_read_all_orders(db_session):
    pass

def test_read_all_orders_db_error(db_session):
    pass

def test_read_one_order(db_session):
    pass

def test_read_one_order_not_found(db_session):
    pass

def test_read_one_order_db_error(db_session):
    pass

def test_update_order(db_session):
    pass

def test_update_order_not_fount(db_session):
    pass

def test_update_order_db_error(db_session):
    pass

def test_delete_order(db_session):
    pass

def test_delete_order_not_found(db_session):
    pass

def test_delete_order_db_error(db_session):
    pass

