from pydantic import BaseModel, Field, ConfigDict
from typing import Optional
from enum import Enum

class OrderType(str, Enum):
    DELIVERY = "Delivery"
    TAKEOUT = "Takeout"

class GuestCheckoutBase(BaseModel):
    customer_name: str
    phone_number: str
    delivery_or_takeout: OrderType
    delivery_address: Optional[str] = None
    summary: Optional[str] = None

class GuestCheckoutCreate(GuestCheckoutBase):
    pass

class GuestCheckoutUpdate(BaseModel):
    customer_name: Optional[str] = None
    phone_number: Optional[str] = None
    delivery_or_takeout: Optional[OrderType] = None
    delivery_address: Optional[str] = None
    summary: Optional[str] = None

class GuestCheckoutResponse(GuestCheckoutBase):
    id: int

    model_config = ConfigDict(from_attributes=True)
