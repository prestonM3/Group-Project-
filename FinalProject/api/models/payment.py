from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base
import random

class Payment(Base):
    __tablename__ = "payment"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    order_id = Column(Integer, ForeignKey("orders.id"), nullable=False, unique=True)
    payment_type = Column(String(8), index=True, nullable=False, default="PENDING")
    payment_status = Column(String(8), index=True, nullable=False)
    card_type = Column(String(8), index=True, nullable=False)
    card_number = Column(String(16), nullable=False)
    card_expiry_date = Column(DATETIME, nullable=False)
    confirmation_code = Column(Integer, index=True, nullable=True)

    # Relationships
    order = relationship("Order", back_populates="payment")

    # Functions
    def submit_payment(self):
        if self.card_expiry_date < datetime.now():
            self.payment_status = "FAILED"
            self.confirmation_code = None
            return False

        self.payment_status = "SUCCESS"
        self.confirmation_code = random.randint(1000, 9999)

        return True

