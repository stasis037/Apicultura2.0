
"""Base models for the application."""
from tortoise import fields, models
from tortoise.models import Model


class BaseModel(Model):
    id = fields.IntField(pk=True)
    created_at = fields.DatetimeField(auto_now_add=True)
    modified_at = fields.DatetimeField(auto_now=True)

    class Meta:
        abstract = True

class User(BaseModel):
    username = fields.CharField(max_length=20, unique=True)
    password_hash = fields.CharField(max_length=128)

    class Meta:
        table = "users"

    def __str__(self):
        return self.username

class Category(BaseModel):
    name = fields.CharField(max_length=255, unique=True)
    articles: fields.ReverseRelation["Article"]

    class Meta:
        table = "categories"

    def __str__(self):
        return self.name


class Type(BaseModel):
    name = fields.CharField(max_length=255, unique=True)
    articles: fields.ReverseRelation["Article"]

    class Meta:
        table = "types"

    def __str__(self):
        return self.name


class ArticleName(BaseModel):
    name = fields.CharField(max_length=255, unique=True)
    articles: fields.ReverseRelation["Article"]

    class Meta:
        table = "article_names"

    def __str__(self):
        return self.name


class Article(BaseModel):
    title = fields.CharField(max_length=255)
    content = fields.TextField()
    thumbnail_url = fields.CharField(max_length=255, null=True)
    category = fields.ForeignKeyField("models.Category", related_name="articles")
    type = fields.ForeignKeyField("models.Type", related_name="articles")
    article_name = fields.ForeignKeyField("models.ArticleName", related_name="articles")

    class Meta:
        table = "articles"

    def __str__(self):
        return self.title
