from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import Merchant
from app.schemas import MerchantCreate
from app.security import hash_password

router = APIRouter(
    prefix="/merchants",
    tags=["Merchants"]
)


@router.post("/")
def create_merchant(
    merchant: MerchantCreate,
    db: Session = Depends(get_db)
):

    new_merchant = Merchant(
        company_name=merchant.company_name,
        email=merchant.email,
        password=hash_password(
            merchant.password
        )
    )

    db.add(new_merchant)

    db.commit()

    db.refresh(new_merchant)

    return new_merchant


@router.get("/")
def get_merchants(
    db: Session = Depends(get_db)
):
    return db.query(Merchant).all()