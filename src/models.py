from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from src.db import Base

class Category(Base):
    __tablename__ = "categories"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    articles = relationship("Article", back_populates="category")

class Type(Base):
    __tablename__ = "types"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    articles = relationship("Article", back_populates="type")

class ArticleName(Base):
    __tablename__ = "article_names"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    articles = relationship("Article", back_populates="article_name")

class Article(Base):
    __tablename__ = "articles"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    content = Column(String)
    category_id = Column(Integer, ForeignKey("categories.id"))
    type_id = Column(Integer, ForeignKey("types.id"))
    article_name_id = Column(Integer, ForeignKey("article_names.id"))

    category = relationship("Category", back_populates="articles")
    type = relationship("Type", back_populates="articles")
    article_name = relationship("ArticleName", back_populates="articles")
