from pydantic import BaseModel
from datetime import datetime

class PaymentBase(BaseModel):
    payment_type: str
    payment_status: str
    card_type: str
    card_status: str
    card_expiry_date: datetime
