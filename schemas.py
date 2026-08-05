from pydantic import BaseModel
from pydantic import EmailStr


class RegisterRequest(BaseModel):
    email: EmailStr
    password: str


class LoginRequest(BaseModel):
    email: EmailStr
    password: str


class InvoiceCreate(BaseModel):
    merchant_id: int
    amount: float
    currency: str
    wallet_address: str


class TransactionCreate(BaseModel):
    invoice_id: int
    tx_hash: str
    amount: float