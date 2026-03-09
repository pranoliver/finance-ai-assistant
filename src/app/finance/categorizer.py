import pandas as pd
import joblib
import os

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler
from ..db import SessionLocal
from ..models import Transaction

MODEL_PATH = "data/models/category_model.pkl"
VECTORIZER_PATH = "data/models/vectorizer.pkl"

def train_model():

    db = SessionLocal()

    try:
        rows = db.query(Transaction).all()
    finally:
        db.close()

    data = []

    for r in rows:
        data.append({
            "merchant": r.merchant,
            "category": r.category
        })

    df = pd.DataFrame(data)

    X = df["merchant"]
    y = df["category"]

    vectorizer = TfidfVectorizer()

    X_vec = vectorizer.fit_transform(X)

    model = LogisticRegression(max_iter=1000)

    model.fit(X_vec, y)

    os.makedirs("data/models", exist_ok=True)

    joblib.dump(model, MODEL_PATH)
    joblib.dump(vectorizer, VECTORIZER_PATH)

    return model, vectorizer

def train_category_model(df: pd.DataFrame):
    """
    Train a category classification model.
    """

    df = df.dropna(subset=["merchant", "amount", "category"])

    X = df[["merchant", "amount"]]
    y = df["category"]

    text_features = "merchant"
    numeric_features = ["amount"]

    preprocessor = ColumnTransformer(
        transformers=[
            ("merchant_tfidf", TfidfVectorizer(), text_features),
            ("amount_scaler", StandardScaler(), numeric_features),
        ]
    )

    model = Pipeline(
        steps=[
            ("preprocess", preprocessor),
            ("classifier", LogisticRegression(max_iter=1000)),
        ]
    )

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model.fit(X_train, y_train)

    accuracy = model.score(X_test, y_test)

    os.makedirs("data/models", exist_ok=True)

    joblib.dump(model, MODEL_PATH)

    return {"status": "trained", "accuracy": float(accuracy)}


def load_model():
    """
    Load trained model from disk.
    """
    if not os.path.exists(MODEL_PATH):
        return train_model()
    
    model = joblib.load(MODEL_PATH)
    vectorizer = joblib.load(VECTORIZER_PATH)

    return model, vectorizer


def predict_category(merchant: str, amount: float):
    """
    Predict category for a new transaction.
    """

    model, vectorizer = load_model();
    X = vectorizer.transform(df["merchant"]);
    prediction = model.predict(X)[0];

    # df = pd.DataFrame([{"merchant": merchant, "amount": amount}])

    # prediction = model.predict(df)[0]

    return prediction
