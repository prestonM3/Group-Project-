from sqlalchemy import Column, Integer, String, Text, Enum as SQLEnum
from sqlalchemy.ext.declarative import declarative_base
import enum

Base = declarative_base()

class OrderTypeEnum(enum.Enum):
    DELIVERY = "Delivery"
    TAKEOUT = "Takeout"

class GuestCheckout(Base):
    __tablename__ = "guest_checkouts"

    id = Column(Integer, primary_key=True, index=True)
    customer_name = Column(String(100), nullable=False)
    phone_number = Column(String(20), nullable=False)
    
    # Stores the selection as an Enum type in the DB
    delivery_or_takeout = Column(SQLEnum(OrderTypeEnum), nullable=False)
    
    delivery_address = Column(String(255), nullable=True)
    summary = Column(Text, nullable=True)