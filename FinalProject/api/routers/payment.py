from typing import List
from fastapi import APIRouter, Depends, FastAPI, status, Response
from sqlalchemy.orm import Session
from ..controllers import payment
from ..schemas.payment import PaymentCreate, Payment
from ..dependencies.database import get_db

router = APIRouter(
    tags=['Payments'],
    prefix="/payment"
)

@router.post("/", response_model=Payment)
def create_payment(payment_data: PaymentCreate, db: Session = Depends(get_db)):
    return payment.create_payment(payment_data, db)

@router.get("/", response_model=List[Payment])
def get_all_payments(db: Session=Depends(get_db)):
    return payment.get_payments(db)

@router.get("/{payment_id}", response_model=Payment)
def get_one_payment(payment_id: int, db: Session = Depends(get_db)):
    return payment.get_payments_by_order_id(payment_id, db)

@router.put("/{payment_id}", response_model=Payment)
def update_payment(payment_id: int, payment_data: PaymentCreate, db: Session = Depends(get_db)):
    return payment.update_payment(payment_id, payment_data, db)

@router.delete("/{payment_id}")
def delete_payment(payment_id: int, db: Session = Depends(get_db)):
    return payment.delete_payment(payment_id, db)


