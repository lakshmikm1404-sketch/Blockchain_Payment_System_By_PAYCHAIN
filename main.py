from fastapi import FastAPI

from app.database import Base
from app.database import engine

from app.routes.auth import router as auth_router
from app.routes.invoices import router as invoices_router
from app.routes.transactions import router as transactions_router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="ChainPay API"
)

app.include_router(auth_router)
app.include_router(invoices_router)
app.include_router(transactions_router)


@app.get("/")
def root():
    return {
        "message": "ChainPay API Running"
    }