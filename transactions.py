from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import Transaction
from app.schemas import TransactionCreate

router = APIRouter(
    prefix="/transactions",
    tags=["Transactions"]
)


@router.post("/")
def create_transaction(
    tx: TransactionCreate,
    db: Session = Depends(get_db)
):

    transaction = Transaction(
        invoice_id=tx.invoice_id,
        tx_hash=tx.tx_hash,
        amount=tx.amount,
        status="Paid"
    )

    db.add(transaction)
    db.commit()
    db.refresh(transaction)

    return transaction


@router.get("/")
def get_transactions(
    db: Session = Depends(get_db)
):
    return db.query(Transaction).all()