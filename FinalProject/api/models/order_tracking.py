from sqlalchemy import Column, ForeignKey, Integer, String, DATETIME
from sqlalchemy.orm import relationship
from ..dependencies.database import Base
from datetime import datetime
from datetime import timedelta

class OrderTracking(Base):
    __tablename__ = "order_tracking"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    order_id = Column(Integer, ForeignKey("orders.id"), nullable=False, unique=True)
    status = Column(String(20), nullable=False, server_default="received")
    order_time = Column(DATETIME, default=datetime.now)
    estimated_minutes = Column(Integer)

    order = relationship("Order", back_populates="order_tracking")
