import pandas as pd

from ..db import SessionLocal
from ..models import Transaction
from ..finance.categorizer import train_category_model

def train():
    db = SessionLocal()
    rows = db.query(Transaction).all()
    df = pd.DataFrame([r.__dict__ for r in rows])
    result = train_category_model(df)

    print(result)


if __name__ == "__main__":
    train()
