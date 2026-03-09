from celery import Celery
import os

celery = Celery(
    os.getenv("REDIS_TOPIC"),
    broker=os.getenv("REDIS_URL"),
    backend=os.getenv("REDIS_URL")
)
