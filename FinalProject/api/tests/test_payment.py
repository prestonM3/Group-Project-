from fastapi.testclient import TestClient
from datetime import datetime
from ..controllers import payment
from ..main import app
import pytest
from ..models import payment as model

# Create a test client for the app
client = TestClient(app)

@pytest.fixture
def db_session(mocker):
    return mocker.Mock()

# Test for payment success
def test_submit_payment(db_session):
    # Create a sample payment
    payment1 = {
        "order_id": 1,
        "payment_type": "CREDIT",
        "payment_status": "PENDING",
        "card_type": "DISCOVER",
        "card_number": "1234567893216549",
        "card_expiry_date": datetime(2028, 12, 31),
        "confirmation_code": None
    }

    payment_object = model.Payment(**payment1)

    # Call the create_payment function
    fake_payment1 = payment.create_payment(payment_object, db_session)

    # Assertions
    assert fake_payment1 is not None
    assert fake_payment1.order_id == 1
    assert fake_payment1.payment_type == "CREDIT"
    assert fake_payment1.card_type == "DISCOVER"
    assert fake_payment1.payment_type == "SUCCESS"
    assert fake_payment1.confirmation_code is None

# Test for payment failure
def test_create_payment_failure(db_session):
    payment2 = {
        "order_id": 2,
        "payment_type": "DEBIT",
        "payment_status": "PENDING",
        "card_type": "VISA",
        "card_number": "9876543217894563",
        "card_expiry_date": datetime(2021, 12, 31),
        "confirmation_code": None
    }

    payment_object2 = model.Payment(**payment2)

    fake_payment2 = payment.create_payment(payment_object2, db_session)

    # Assertions
    assert fake_payment2 is not None
    assert fake_payment2.payment_status == "FAILED"
    assert fake_payment2.confirmation_code is None
