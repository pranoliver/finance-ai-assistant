from .celery_app import celery

@celery.task
def retrain_models():
    print("Retraining ML models on new transactions")
