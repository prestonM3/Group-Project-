from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from ..models.guest_checkout import GuestCheckout  
from ..schemas.guest_checkout import GuestCheckoutCreate, GuestCheckoutUpdate


def create(db: Session, request: GuestCheckoutCreate):
    new_guest = GuestCheckout(
        customer_name=request.customer_name,
        phone_number=request.phone_number,
        delivery_or_takeout=request.delivery_or_takeout,
        delivery_address=request.delivery_address,
        summary=request.summary
    )
    db.add(new_guest)
    db.commit()
    db.refresh(new_guest)
    return new_guest


def read_all(db: Session):
    return db.query(GuestCheckout).all()


def read_one(db: Session, item_id: int):
    guest = db.query(GuestCheckout).filter(GuestCheckout.id == item_id).first()
    if not guest:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail=f"Guest checkout record with id {item_id} not found"
        )
    return guest


def update(db: Session, request: GuestCheckoutUpdate, item_id: int):
    guest = db.query(GuestCheckout).filter(GuestCheckout.id == item_id).first()
    if not guest:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail=f"Guest checkout record with id {item_id} not found"
        )
    
    # Dynamically update provided fields
    update_data = request.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(guest, key, value)
        
    db.commit()
    db.refresh(guest)
    return guest


def delete(db: Session, item_id: int):
    guest = db.query(GuestCheckout).filter(GuestCheckout.id == item_id).first()
    if not guest:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail=f"Guest checkout record with id {item_id} not found"
        )
    db.delete(guest)
    db.commit()
    return {"detail": f"Guest checkout record {item_id} successfully deleted"}