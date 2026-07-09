from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base

class PromoCode(Base):
    __tablename__ = "promo_codes"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    promo_code = Column(String(8), index=True, nullable=False)
    discount = Column(Integer, index=True, nullable=False)
    expiration_date = Column(DATETIME, nullable=False)

    # Functions
    validation = None
    apply_discount = None

    orders = relationship("Order", back_populates="promo_code")
