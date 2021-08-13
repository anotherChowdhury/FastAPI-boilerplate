from sqlalchemy import Column, Integer, String
from .base_model import BaseModel


class Book(BaseModel):
    __tablename__ = "books"
    name = Column(String, nullable=False)
    author = Column(String, nullable=False)
    release_year = Column(Integer, nullable=False)
