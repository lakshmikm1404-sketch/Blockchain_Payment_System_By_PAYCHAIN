from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import Invoice
from app.schemas import InvoiceCreate

router = APIRouter(prefix="/invoices")

@router.post("/")
def create_invoice(
    invoice: InvoiceCreate,
    db: Session = Depends(get_db)
):
    data = Invoice(
        merchant_id=invoice.merchant_id,
        amount=invoice.amount,
        currency=invoice.currency,
        wallet_address=invoice.wallet_address,
    )

    db.add(data)
    db.commit()
    db.refresh(data)

    return data

@router.get("/")
def get_invoices(
    db: Session = Depends(get_db)
):
    return db.query(Invoice).all()