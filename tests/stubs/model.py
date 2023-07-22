from app.models.model import Model as BaseModel
from sqlalchemy import Column, Integer, String


class Model(BaseModel):
    __tablename__ = "models"

    id = Column(Integer, primary_key=True)
    text = Column(String, nullable=False)
