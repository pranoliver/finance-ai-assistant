import pandas as pd

from ..db import SessionLocal
from ..models import Transaction

from ..finance.anomaly_detection import detect_anomalies
from ..finance.forecasting import predict_spending
from ..finance.clustering import cluster_users
from ..finance.categorizer import predict_category


class FinanceService:
    def __init__(self):
        self.db = SessionLocal()

    def load_transactions_dataframe(self):
        """
        Load all transactions from DB into pandas dataframe
        """
        db = SessionLocal()

        try:
            rows = db.query(Transaction).all()
            # rows = self.db.query(Transaction).all()

            data = []

            for r in rows:
                data.append({
                    "transaction_id": r.transaction_id,
                    "user_id": r.user_id,
                    "date": r.date,
                    "amount": r.amount,
                    "merchant": r.merchant,
                    "category": r.category,
                    "payment_method": r.payment_method,
                    "city": r.city,
                    "currency": r.currency,
                    "is_fraud": r.is_fraud
                })

            df = pd.DataFrame(data)

            return df

        finally:
            db.close()

    def get_spending_summary(self):
        """
        Aggregated spending by category
        """

        df = self.load_transactions_dataframe()

        if df.empty:
            return {}

        result = df.groupby("category")["amount"].sum()

        return result.to_dict()


    def detect_fraud_transactions(self):
        """
        Run anomaly detection model
        """

        df = self.load_transactions_dataframe()

        if df.empty:
            return []

        df = detect_anomalies(df)

        anomalies = df[df["anomaly"] == -1]

        return anomalies.head(20).to_dict(orient="records")


    def predict_future_spending(self):
        """
        Predict next transaction spending trend
        """

        df = self.load_transactions_dataframe()

        if df.empty:
            return None

        amounts = df["amount"].values

        prediction = predict_spending(amounts)

        return prediction


    def cluster_customer_segments(self):
        """
        Segment users based on spending behavior
        """

        df = self.load_transactions_dataframe()

        if df.empty:
            return []

        result = cluster_users(df)

        return result


    def auto_categorize_transaction(self, merchant, amount):
        """
        Predict category for new transaction
        """

        category = predict_category(merchant, amount)

        return category


    def create_transaction(self, data):
        """
        Insert new transaction into DB
        """

        tx = Transaction(
            transaction_id=data.get("transaction_id"),
            user_id=data.get("user_id"),
            date=data.get("date"),
            amount=data.get("amount"),
            merchant=data.get("merchant"),
            category=data.get("category"),
            payment_method=data.get("payment_method"),
            city=data.get("city"),
            currency=data.get("currency"),
            is_fraud=data.get("is_fraud", 0)
        )

        self.db.add(tx)

        self.db.commit()

        return {"status": "created"}