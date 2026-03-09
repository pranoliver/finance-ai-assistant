from sklearn.cluster import KMeans

def cluster_users(df):
    data = df.groupby("user_id")["amount"].sum().reset_index()
    X = data[["amount"]]
    model = KMeans(n_clusters=5)
    data["cluster"] = model.fit_predict(X)
    return data.head(20).to_dict()
