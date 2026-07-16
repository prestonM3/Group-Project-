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
        card_type=payment.card_type,
        card_number=payment.card_number,
        card_expiry_date=payment.card_expiry_date,
        payment_status="PENDING"
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
    payment = db.query(Payment).filter(Payment.id == payment_id).first()

    if payment is None:
        raise HTTPException(status_code=404, detail="Payment not found")

    return payment

# Update payment data saved in database
def update_payment(payment_id: int, payment_data: PaymentCreate, db: Session):
    db_payment = db.query(Payment).filter(Payment.id == payment_id).first()

    if db_payment is None:
        raise HTTPException(status_code=404, detail="Payment not found")

    db_payment.payment_type = payment_data.payment_type
    db_payment.payment_status = payment_data.payment_status
    db_payment.card_type = payment_data.card_type
    db_payment.card_number = payment_data.card_number
    db_payment.card_expiry_date = payment_data.card_expiry_date
    db_payment.confirmation_code = payment_data.confirmation_code

    db.commit()
    db.refresh(db_payment)

    return db_payment

# Delete a payment
def delete_payment(payment_id: int, db: Session):
    payment = db.query(Payment).filter(Payment.id== payment_id).first()

    if payment is None:
        raise HTTPException(status_code=404, detail="Payment not found")

    db.delete(payment)
    db.commit()

    return {"message": "Payment successfully deleted"}