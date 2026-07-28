from pydantic import BaseModel
from datetime import datetime

class PromoCodeBase(BaseModel):
    discount: int
    expiration_date: datetime

class PromoCodeCreate(PromoCodeBase):
    pass

class PromoCode(PromoCodeBase):
    id: int
    promo_code: str

    class Config:
        from_attributes = True
