from sklearn.linear_model import LinearRegression
import numpy as np

def predict_spending(amounts):
    X = np.arange(len(amounts)).reshape(-1,1)
    model = LinearRegression()
    model.fit(X,amounts)
    pred = model.predict([[len(amounts)+1]])
    return float(pred[0])
