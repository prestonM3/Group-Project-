from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base

class PromoCode(Base):
    __tablename__ = "promo_codes"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    promo_code = Column(String(20), nullable=False, unique=True)
    discount = Column(Integer, index=True, nullable=False)
    expiration_date = Column(DATETIME, nullable=False)

    # Functions

    # Validation method to return true if promo code is still valid
    def validation(self):
        return self.expiration_date >= datetime.now()

    # Applies the discounted amount to the order total
    def apply_discount(self, total):
        if not self.validation():
            return total

        discount_total = total * (self.discount / 100)

        return total - discount_total

    orders = relationship("Order", back_populates="promo_code")
