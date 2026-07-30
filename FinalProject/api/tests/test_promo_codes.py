from datetime import datetime
import pytest
from fastapi.testclient import TestClient

from ..controllers import promo_codes
from ..main import app
from ..models import promo_codes as model

# Create a test client for the app
client = TestClient(app)

@pytest.fixture
def db_session(mocker):
    session = mocker.Mock()
    # No existing promo code collides, so generate_promo_code() succeeds on its first attempt.
    session.query.return_value.filter.return_value.first.return_value = None
    return session

# Testing the create promo code method
def test_create_promo_code(db_session):
    promo_code_data = {
        "discount": 30,
        "expiration_date": datetime(2026, 12, 31)
    }

    promo_code_object = model.PromoCode(**promo_code_data)

    # Call the create promocode function
    promo_code = promo_codes.create(promo_code_object, db_session)

    # Assertions
    assert promo_code is not None
    # promo_code is now generated server-side rather than client-supplied
    assert isinstance(promo_code.promo_code, str)
    assert len(promo_code.promo_code) == 15
    assert promo_code.discount == 30


# Test promocode validation success
def test_validation_code_success():
    promo_code_data = model.PromoCode(
        promo_code="PRMCD2026",
        discount=30,
        expiration_date=datetime(2028,12,31)
    )
    assert promo_code_data.validation() is True

# Test promocode validation failure
def test_validation_code_failure():
    promo_code_data = model.PromoCode(
        promo_code="PRMCD2026",
        discount=30,
        expiration_date=datetime(2021, 12, 31)
    )

    assert promo_code_data.validation() is False

# Test the promocode apply discount success
def test_apply_discount_success():
    promo_code_data = model.PromoCode(
        promo_code="PRMCD2026",
        discount=25,
        expiration_date=datetime(2028, 12, 31)
    )

    discounted_amount = promo_code_data.apply_discount(100)
    assert discounted_amount == 75

# Test the promocode apply discount failure
def test_apply_discount_failure():
    promo_code_data = model.PromoCode(
        promo_code="PRMCD2026",
        discount=25,
        expiration_date=datetime(2021,12,31)
    )

    discounted_amount = promo_code_data.apply_discount(100)

    assert discounted_amount == 100
