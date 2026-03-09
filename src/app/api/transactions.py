from fastapi import APIRouter, UploadFile
import pandas as pd
from ..db import SessionLocal
from ..models import Transaction

router = APIRouter()

@router.post("/transactions/upload")
async def upload(file: UploadFile):

    df = pd.read_csv(file.file)

    db = SessionLocal()

    for _, row in df.iterrows():
        tx = Transaction(
            transaction_id=row["transaction_id"],
            user_id=row["user_id"],
            date=row["date"],
            amount=row["amount"],
            merchant=row["merchant"],
            category=row["category"],
            payment_method=row["payment_method"],
            city=row["city"],
            currency=row["currency"],
            is_fraud=row["is_fraud"],
        )
        db.add(tx)

    db.commit()
    return {"status": "uploaded"}
