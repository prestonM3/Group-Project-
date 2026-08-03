from fastapi.testclient import TestClient
from fastapi import HTTPException
from sqlalchemy.exc import SQLAlchemyError
from ..controllers import order_items as controller
from ..main import app
import pytest
from ..models import order_items as model
from sqlalchemy import null

# Create a test client for the app
client = TestClient(app)


@pytest.fixture
def db_session(mocker):
    return mocker.Mock()

def test_order_item(db_session):
    # Create a sample order item
    order_item_data = {
        "quantity" : 3,
        # "order_id" == 1,
        # "menu_item_id" == 1
    }

    order_item_object = model.OrderItem(**order_item_data)

    # Call the create function
    created_order_item = controller.create(db_session, order_item_object)

    # Assert that the database returned success
    order_item_get = client.get(f"/orderitems/")
    assert order_item_get.status_code == 200

    # Assert that the post was accurate and reading works
    assert created_order_item is not None
    assert created_order_item.quantity == 3

    db_session.add.assert_called_once()
    db_session.commit.assert_called_once()
    db_session.refresh.assert_called_once()
