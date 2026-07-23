from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response
from sqlalchemy.exc import SQLAlchemyError

from ..models.payment import Payment
from ..schemas.payment import PaymentCreate

# Create new payment to submit and store in database
def create(payment: PaymentCreate, db: Session):
    db_payment = Payment(
        order_id=payment.order_id,
        payment_type=payment.payment_type,
        card_type=payment.card_type,
        card_number=payment.card_number,
        card_expiry_date=payment.card_expiry_date,
        payment_status="PENDING"
    )

    db_payment.submit_payment()

    try:
        db.add(db_payment)
        db.commit()
        db.refresh(db_payment)

    except SQLAlchemyError as e:
        error = str(e)
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=error
        )

    return db_payment

# Get all payments in database
def read_all(db: Session):
    try:
        results = db.query(Payment).all()

    except SQLAlchemyError as e:
        error = str(e)
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=error
        )

    return results

# Get payment based on order ID
def read_one(payment_id: int, db: Session):
    try:
        db_payment = db.query(Payment).filter(Payment.id == payment_id).first()

        if db_payment is None:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Id not found")

    except SQLAlchemyError as e:
        error = str(e)
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)

    return db_payment

# Update payment data saved in database
def update(payment_id: int, payment_data: PaymentCreate, db: Session):
    try:
        db_payment = db.query(Payment).filter(Payment.id == payment_id)

        if db_payment.first() is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Id not found!")

        update_payment = payment_data.model_dump(exclude_unset=True)
        db_payment.update(update_payment, synchronize_session=False)
        db.commit()

    except SQLAlchemyError as e:
        error = str(e)
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)

    return db_payment.first()

# Delete a payment
def delete(payment_id: int, db: Session):
    try:
        payment = db.query(Payment).filter(Payment.id == payment_id).first()

        if payment is None:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Id not found!")

        db.delete(payment)
        db.commit()

    except SQLAlchemyError as e:
        error = str(e)
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)

    return Response(status_code=status.HTTP_204_NO_CONTENT)