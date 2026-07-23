from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..controllers import promo_codes
from ..schemas.promo_codes import PromoCode, PromoCodeCreate
from ..dependencies.database import get_db

router = APIRouter(
    tags=["Promo Codes"],
    prefix="/promo_codes",
)

@router.post("/", response_model=PromoCode)
def create_promo_code(promo_data: PromoCodeCreate, db: Session = Depends(get_db)):
    return promo_codes.create(promo_data, db)

@router.get("/", response_mode=List[PromoCode])
def get_all_promo_codes(db: Session = Depends(get_db)):
    return promo_codes.read_all(db)

@router.get("/[{promo_id}]", response_model=PromoCode)
def get_one_promo_code(promo_id: int, db: Session = Depends(get_db)):
    return promo_codes.read_one(promo_id, db)

@router.put("/{promo_id}", response_model=PromoCode)
def update_promo_code(promo_id: int, promo_code: PromoCodeCreate, db: Session = Depends(get_db)):
    return promo_codes.update(promo_id, promo_code, db)

@router.delete("/{promo_id}", status_code=204)
def delete_promo_code(promo_id: int, db: Session = Depends(get_db)):
    return promo_codes.delete(promo_id, db)