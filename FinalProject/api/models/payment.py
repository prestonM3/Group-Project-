from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base

class Payment(Base):
    __tablename__ = "payment"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    order_id = Column(Integer, ForeignKey("orders.id"), nullable=False, unique=True)
    payment_type = Column(String(8), index=True, nullable=False)
    payment_status = Column(String(8), index=True, nullable=False)
    card_type = Column(String(8), index=True, nullable=False)
    card_number = Column(String(16))
    card_expiry_date = Column(DATETIME, nullable=False)
    confirmation_code = Column(Integer, index=True, nullable=False)

    # Functions
    submit_payment = None

    order = relationship("Order", back_populates="payment")