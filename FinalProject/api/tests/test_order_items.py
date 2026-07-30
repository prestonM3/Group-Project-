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

def test_create_order_item(db_session):
    pass

def test_create_order_item_db_error(db_session):
    pass

def test_read_all_order_items(db_session):
    pass

def test_read_all_order_items_db_error(db_session):
    pass

def test_read_one_order_item(db_session):
    pass

def test_read_one_order_item_not_found(db_session):
    pass

def test_read_one_order_item_db_error(db_session):
    pass

def test_update_order_item(db_session):
    pass

def test_update_order_item_not_fount(db_session):
    pass

def test_update_order_item_db_error(db_session):
    pass

def test_delete_order_item(db_session):
    pass

def test_delete_order_item_not_found(db_session):
    pass

def test_delete_order_item_db_error(db_session):
    pass
