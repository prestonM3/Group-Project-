from pydantic import BaseModel, ConfigDict
from datetime import datetime

class PromoCodeBase(BaseModel):
    discount: int
    expiration_date: datetime

class PromoCodeCreate(PromoCodeBase):
    pass

class PromoCodeUpdate(BaseModel):
    discount: int | None = None
    expiration_date: datetime | None = None

class PromoCode(PromoCodeBase):
    id: int
    promo_code: str

    model_config = ConfigDict(from_attributes=True)
