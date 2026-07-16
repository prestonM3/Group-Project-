from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response, Depends
from ..models.payment import Payment
from ..schemas.payment import PaymentCreate
from sqlalchemy.exc import SQLAlchemyError

# Create new payment to submit and sore in database
def create_payment(payment: PaymentCreate, db:Session):
    db_payment = Payment(
        order_id=payment.order_id,
        payment_type=payment.payment_type,
        payment_status=payment.payment_status,
        card_type=payment.card_type,
        card_number=payment.card_number,
        card_expiry=payment.card_expiry,
        confirmation_code=payment.confirmation_code
    )

    db_payment.submit_payment()

    db.add(db_payment)
    db.commit()
    db.refresh(db_payment)

    return db_payment

# Get all payments in database
def get_payments(db:Session):
    return db.query(Payment).all()

# Get payment based on order ID
def get_payments_by_order_id(payment_id: int, db:Session):
    payment = db.query(Paymnet).filter(Payment.id == payment_id).first()

    if payment is None:
        raise HTTPException(status_code=404, detail="Payment not found")

    return payment

