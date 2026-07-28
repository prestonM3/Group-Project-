from datatime import datetime
import pytest
from fastapi.testclient import TestClient

from ..controllers import promo_codes
from ..main import app
from ..models import promo_codes as model

# Create a test client for the app
client = TestClient(app)

@pytest.fixture
def db_session(mocker):
    return mocker.Mock()

# Testing the create promo code method
def test_create_promo_code(db_session):
    promo_code_data = {
        "promo_code": "PRMCD2026",
        "discount": 30
        "expiration_date": datetime(2026,12,31)
    }

    promo_code_object = model.PromoCode(**promo_code_data)

    # Call the create promocode function
    promo_code = promo_codes.PromoCode(promo_code_object, db_session)

    # Assertions
    assert promo_code is not None
    assert promo_code.promo_code == "PRMCD2026"
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