from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from .db import Base,engine
from .api import transactions,analytics

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(transactions.router)
app.include_router(analytics.router)

app.mount("/frontend", StaticFiles(directory="frontend"), name="frontend")
