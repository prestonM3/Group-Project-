from typing import List
from fastapi import APIRouter, Depends
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
    return payment.create(payment_data, db)

@router.get("/", response_model=List[Payment])
def get_all_payments(db: Session=Depends(get_db)):
    return payment.read_all(db)

@router.get("/{payment_id}", response_model=Payment)
def get_one_payment(payment_id: int, db: Session = Depends(get_db)):
    return payment.read_one(payment_id, db)

@router.put("/{payment_id}", response_model=Payment)
def update_payment(payment_id: int, payment_data: PaymentCreate, db: Session = Depends(get_db)):
    return payment.update(payment_id, payment_data, db)

@router.delete("/{payment_id}")
def delete_payment(payment_id: int, db: Session = Depends(get_db)):
    return payment.delete(payment_id, db)


