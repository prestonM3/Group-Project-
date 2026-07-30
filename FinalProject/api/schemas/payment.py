from pydantic import BaseModel, ConfigDict
from datetime import datetime

class PaymentBase(BaseModel):
    order_id: int
    payment_type: str
    card_type: str
    card_number: str
    card_expiry_date: datetime

class PaymentCreate(PaymentBase):
    pass

class PaymentUpdate(BaseModel):
    order_id: int | None = None
    payment_type: str | None = None
    card_type: str | None = None
    card_number: str | None = None
    card_expiry_date: datetime | None = None

class Payment(PaymentBase):
    id: int
    payment_status: str
    confirmation_code: int | None

    model_config = ConfigDict(from_attributes=True)
