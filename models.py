from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Float
from sqlalchemy import ForeignKey

from app.database import Base


class Merchant(Base):
    __tablename__ = "merchants"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    email = Column(
        String,
        unique=True,
        nullable=False
    )

    password = Column(
        String,
        nullable=False
    )


class Invoice(Base):
    __tablename__ = "invoices"

    id = Column(Integer, primary_key=True)

    merchant_id = Column(
        Integer,
        ForeignKey("merchants.id")
    )

    amount = Column(Float)

    currency = Column(String)

    wallet_address = Column(String)

    status = Column(
        String,
        default="Pending"
    )


class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True)

    invoice_id = Column(Integer)

    tx_hash = Column(String)

    amount = Column(Float)

    status = Column(String)