from pydantic import BaseModel
from datetime import datetime

class PaymentBase(BaseModel):
    order_id: int
    payment_type: str
    payment_status: str
    card_type: str
    card_number: str
    card_expiry_date: datetime
    confirmation_code: int

class PaymentCreate(PaymentBase):
    pass

class Payment(PaymentBase):
    id: int
    payment_status: str
    confirmation_code: int | None

    class Config:
        from_attributes = True
