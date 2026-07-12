from pydantic import BaseModel
from datetime import datetime

class PromoCodeBase(BaseModel):
    promo_code: str
    discount: int
    expiration_date: datetime


