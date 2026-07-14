from pydantic import BaseModel
from datetime import datetime

class PaymentBase(BaseModel):
    payment_type: str
    payment_status: str
    card_type: str
    card_number: int
    card_expiry_date: datetime
    confirmation_code: int

class PaymentCreate(PaymentBase):
    pass


class Payment(PaymentBase):
    id: int
    generated_at: datetime

    class Config:
        from_attributes = True
