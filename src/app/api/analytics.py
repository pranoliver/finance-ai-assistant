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