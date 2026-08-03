from fastapi.testclient import TestClient
from fastapi import HTTPException
from sqlalchemy.exc import SQLAlchemyError
from ..controllers import order_tracking as controller
from ..main import app
import pytest
from ..models import order_tracking as model
from sqlalchemy import null

# Create a test client for the app
client = TestClient(app)


@pytest.fixture
def db_session(mocker):
    return mocker.Mock()

def test_order_tracking(db_session):
    # Create a sample order tracker
    order_tracking_data = {
        "status" : "received",
        "estimated_minutes" : 30
    }

    order_tracking_object = model.OrderTracking(**order_tracking_data)

    # Call the create function
    created_order_tracking = controller.create(db_session, order_tracking_object)

    # Assert that the database returned success
    order_tracking_get = client.get(f"/order_tracking/")
    assert order_tracking_get.status_code == 200

    # Assert that the post was accurate and reading works
    assert created_order_tracking is not None
    assert created_order_tracking.status == "received"
    assert created_order_tracking.estimated_minutes == 30

    db_session.add.assert_called_once()
    db_session.commit.assert_called_once()
    db_session.refresh.assert_called_once()

