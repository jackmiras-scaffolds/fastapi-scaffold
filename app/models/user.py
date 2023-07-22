from sqlalchemy import Column, Integer, String

from app.models.model import Model


class User(Model):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    email = Column(String, nullable=False)
    password = Column(String, nullable=False)
