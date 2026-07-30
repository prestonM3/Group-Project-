import random
import string

from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response
from sqlalchemy.exc import SQLAlchemyError

from ..models.promo_codes import PromoCode
from ..schemas.promo_codes import PromoCodeCreate, PromoCodeUpdate

# Generate a unique promo code
def generate_promo_code(db: Session, length: int = 15) -> str:
    chars = string.ascii_letters + string.digits
    max_attempts = 5

    for attempt in range(max_attempts):
        code = "".join(random.choices(chars, k=length))

        existing_code = db.query(PromoCode).filter(
            PromoCode.promo_code == code
        ).first()

        if existing_code is None:
            return code

    raise HTTPException(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        detail="Failed to generate a unique promo code"
    )

# Create a promo code
def create(promo: PromoCodeCreate, db: Session):
    db_promo = PromoCode(
        promo_code=generate_promo_code(db),
        discount=promo.discount,
        expiration_date=promo.expiration_date,
    )

    try:
        db.add(db_promo)
        db.commit()
        db.refresh(db_promo)

    except SQLAlchemyError as e:
        error = str(e)
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)

    return db_promo

# Read all the promo codes in the database
def read_all(db: Session):
    try:
        results = db.query(PromoCode).all()

    except SQLAlchemyError as e:
        error = str(e)
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)

    return results

# Read one promo code in the database based on the entered Id
def read_one(promo_id: int, db: Session):
    try:
        db_promo = db.query(PromoCode).filter(
            PromoCode.id == promo_id
        ).first()

        if db_promo is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Id not found")

    except SQLAlchemyError as e:
        error = str(e)
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)

    return db_promo

# Update a promo code in the database
def update(promo_id: int, promo_data: PromoCodeUpdate, db: Session):
    try:
        db_promo = db.query(PromoCode).filter(
            PromoCode.id == promo_id
        ).first()

        if db_promo is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Id not found")

        for field, value in promo_data.model_dump(exclude_unset=True).items():
            setattr(db_promo, field, value)

        db.commit()
        db.refresh(db_promo)

    except SQLAlchemyError as e:
        error = str(e)
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)

    return db_promo

# Delete a promo code from the database
def delete(promo_id: int, db: Session):
    try:
        db_promo = db.query(PromoCode).filter(
            PromoCode.id == promo_id
        ).first()

        if db_promo is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Id not found")

        db.delete(db_promo)
        db.commit()

    except SQLAlchemyError as e:
        error = str(e)
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)

    return Response(status_code=status.HTTP_204_NO_CONTENT)