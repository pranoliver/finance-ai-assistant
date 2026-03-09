from fastapi import APIRouter
from ..services.finance_service import FinanceService

router = APIRouter()

service = FinanceService()

@router.get("/analytics/spending")
def spending():
    return service.get_spending_summary()


@router.get("/analytics/fraud")
def fraud():
    return service.detect_fraud_transactions()


@router.get("/analytics/predict")
def predict():
    return {"prediction": service.predict_future_spending()}


@router.get("/analytics/cluster")
def cluster():
    return service.cluster_customer_segments()


@router.get("/analytics/predict-category")
def predict_category(merchant:str, amount:float):
    service = FinanceService()
    category = service.auto_categorize_transaction(merchant,amount)
    return {"category":category}


@router.get("/stats")
def stats():
    from sqlalchemy import func
    from ..db import SessionLocal
    from ..models import Transaction

    db = SessionLocal()

    try:
        total_transactions = db.query(func.count(Transaction.id)).scalar()
        total_spending = db.query(func.sum(Transaction.amount)).scalar()
        total_users = db.query(func.count(func.distinct(Transaction.user_id))).scalar()
        total_merchants = db.query(func.count(func.distinct(Transaction.merchant))).scalar()
        total_categories = db.query(func.count(func.distinct(Transaction.category))).scalar()

        return {
            "transactions": total_transactions,
            "spending": float(total_spending or 0),
            "users": total_users,
            "merchants": total_merchants,
            "categories": total_categories
        }

    finally:
        db.close()