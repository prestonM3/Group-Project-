from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base

Class PromoCode(Base):
    __tablename__ = "promo_codes"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    promo_code = Column(String(8), index=True, nullable=False)
    discount = Column(Integer, index=True, nullable=False)
    expiration_date = Column(DATETIME, nullable=False)

    orders = relationship("Order", back_populates="promo_code")
