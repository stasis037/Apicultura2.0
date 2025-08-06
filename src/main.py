
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from tortoise.contrib.fastapi import register_tortoise
import os
from src.routes import router as api_router
from src.api.auth import router as auth_router
from sqladmin import Admin, ModelView
from src.db import engine
from src.models.sql import Article, Category, Type, ArticleName

app = FastAPI()

# CORS for frontend - Development settings
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://127.0.0.1:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


# Register Tortoise ORM with SQLite
register_tortoise(
    app,
    db_url="sqlite://apiculture.db",
    modules={"models": ["src.models.base"]},
    generate_schemas=True,
    add_exception_handlers=True,
)

# SQLAdmin setup
admin = Admin(app, engine)

class ArticleAdmin(ModelView, model=Article):
    name = "Article"
    name_plural = "Articles"
    icon = "fa-newspaper"
    column_list = [Article.id, Article.title, Article.content, Article.category, Article.type, Article.article_name, Article.created_at, Article.modified_at]
    column_searchable_list = [Article.title, Article.content]
    column_sortable_list = [Article.id, Article.title, Article.created_at]
    form_excluded_columns = ["created_at", "modified_at"]

class CategoryAdmin(ModelView, model=Category):
    name = "Category"
    name_plural = "Categories"
    icon = "fa-folder"
    column_list = [Category.id, Category.name, Category.created_at, Category.modified_at]
    column_searchable_list = [Category.name]
    column_sortable_list = [Category.id, Category.name, Category.created_at]
    form_excluded_columns = ["created_at", "modified_at"]

class TypeAdmin(ModelView, model=Type):
    name = "Type"
    name_plural = "Types"
    icon = "fa-tag"
    column_list = [Type.id, Type.name, Type.created_at, Type.modified_at]
    column_searchable_list = [Type.name]
    column_sortable_list = [Type.id, Type.name, Type.created_at]
    form_excluded_columns = ["created_at", "modified_at"]

class ArticleNameAdmin(ModelView, model=ArticleName):
    name = "Article Name"
    name_plural = "Article Names"
    icon = "fa-file-alt"
    column_list = [ArticleName.id, ArticleName.name, ArticleName.created_at, ArticleName.modified_at]
    column_searchable_list = [ArticleName.name]
    column_sortable_list = [ArticleName.id, ArticleName.name, ArticleName.created_at]
    form_excluded_columns = ["created_at", "modified_at"]

admin.add_view(ArticleAdmin)
admin.add_view(CategoryAdmin)
admin.add_view(TypeAdmin)
admin.add_view(ArticleNameAdmin)

# Serve React index.html at root
@app.get("/")
def serve_react_index():
    frontend_path = os.path.join(os.path.dirname(__file__), "..", "index.html")
    return FileResponse(frontend_path)


# Register API routers
app.include_router(api_router, prefix="/api")
app.include_router(auth_router, prefix="/api/auth")
