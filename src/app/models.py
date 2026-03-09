from sqlalchemy import Column,Integer,String,Float,Date
from .db import Base
import os

class Transaction(Base):

    __tablename__ = os.getenv("MYSQL_TABLE_TRANS")

    id = Column(Integer, primary_key=True, index=True)

    transaction_id = Column(String(64))
    user_id = Column(Integer)

    date = Column(Date)

    amount = Column(Float)

    merchant = Column(String(255))
    category = Column(String(255))

    payment_method = Column(String(50))
    city = Column(String(100))
    currency = Column(String(10))

    is_fraud = Column(Integer)
