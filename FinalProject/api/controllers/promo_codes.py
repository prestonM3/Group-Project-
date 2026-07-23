from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response
from sqlalchemy.exc import SQLAlchemyError

from ..models.promo_codes import PromoCode
from ..schemas.promo_codes import PromoCodeCreate

# Create a promo code
def create(promo: PromoCodeCreate, db: Session):
    db_promo = PromoCode(
        promo_code=promo.promo_code,
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
def update(promo_id: int, promo_data: PromoCodeCreate, db: Session):
    try:
        db_promo = db.query(PromoCode).filter(
            PromoCode.id == promo_id
        ).first()

        if db_promo is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Id not found")

        db_promo.promo_code = promo_data.promo_code
        db_promo.discount = promo_data.discount
        db_promo.expiration_date = promo_data.expiration_date

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