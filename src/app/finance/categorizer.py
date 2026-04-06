# src/app/finance/categorizer.py

import os
import joblib
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler

from ..db import SessionLocal
from ..models import Transaction

MODEL_PATH = "data/models/category_pipeline.joblib"


def _fetch_training_dataframe():
    """
    Read transactions from DB into a DataFrame suitable for training.
    """
    db = SessionLocal()
    try:
        rows = db.query(Transaction).all()
    finally:
        db.close()

    data = []
    for r in rows:
        # ensure required fields exist; skip if missing
        if r.merchant is None or r.amount is None or r.category is None:
            continue
        data.append(
            {"merchant": r.merchant, "amount": r.amount, "category": r.category}
        )

    if not data:
        return pd.DataFrame(columns=["merchant", "amount", "category"])

    df = pd.DataFrame(data)
    return df


def train_category_model(save_path: str = MODEL_PATH):
    """
    Train the category classification pipeline and save it.
    Returns a dict with status and accuracy.
    """
    df = _fetch_training_dataframe()

    if df.empty:
        raise RuntimeError("No training data available to train categorizer.")

    # features and target
    X = df[["merchant", "amount"]]
    y = df["category"]

    # ColumnTransformer that applies TF-IDF to merchant and scaler to amount
    preprocessor = ColumnTransformer(
        transformers=[
            ("merchant_tfidf", TfidfVectorizer(), "merchant"),
            ("amount_scaler", StandardScaler(), ["amount"]),
        ],
        remainder="drop",
        sparse_threshold=0.0,
    )

    pipeline = Pipeline(
        steps=[
            ("preprocess", preprocessor),
            ("classifier", LogisticRegression(max_iter=1000)),
        ]
    )

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.15,
        random_state=42,
        stratify=y if len(y.unique()) > 1 else None,
    )

    pipeline.fit(X_train, y_train)

    accuracy = (
        pipeline.score(X_test, y_test)
        if len(y_test) > 0
        else pipeline.score(X_train, y_train)
    )

    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    joblib.dump(pipeline, save_path)

    return {"status": "trained", "accuracy": float(accuracy)}


def load_model(save_path: str = MODEL_PATH):
    """
    Load the saved pipeline from disk. If not present, train from DB.
    Returns: trained Pipeline object
    """
    if not os.path.exists(save_path):
        # lazy-train on demand
        train_category_model(save_path=save_path)

    pipeline = joblib.load(save_path)
    return pipeline


def predict_category(merchant: str, amount: float):
    """
    Predict category for a new transaction using the saved pipeline.
    Accepts merchant (str) and amount (float).
    Returns a single category label (string).
    """
    pipeline = load_model()

    # Create a single-row DataFrame with the exact columns pipeline expects
    df = pd.DataFrame(
        [
            {
                "merchant": merchant if merchant is not None else "",
                "amount": float(amount) if amount is not None else 0.0,
            }
        ]
    )

    pred = pipeline.predict(df)
    return pred[0]
