from fastapi import APIRouter, HTTPException
from src.models.base import Article, Category, Type, ArticleName
from typing import List
from tortoise.contrib.pydantic import pydantic_model_creator
from pydantic import BaseModel

router = APIRouter()

# Pydantic models for creation/update
class CategoryCreate(BaseModel):
    name: str

class TypeCreate(BaseModel):
    name: str

class ArticleNameCreate(BaseModel):
    name: str

class ArticleCreate(BaseModel):
    title: str
    content: str
    category_id: int
    type_id: int
    article_name_id: int

# Pydantic models for responses
Category_Pydantic = pydantic_model_creator(Category, name="Category", exclude_readonly=True)
Category_PydanticRead = pydantic_model_creator(Category, name="CategoryRead")
Type_Pydantic = pydantic_model_creator(Type, name="Type", exclude_readonly=True)
Type_PydanticRead = pydantic_model_creator(Type, name="TypeRead")
ArticleName_Pydantic = pydantic_model_creator(ArticleName, name="ArticleName", exclude_readonly=True)
ArticleName_PydanticRead = pydantic_model_creator(ArticleName, name="ArticleNameRead")
Article_Pydantic = pydantic_model_creator(Article, name="Article", exclude_readonly=True)
Article_PydanticRead = pydantic_model_creator(Article, name="ArticleRead")

# --- Category CRUD ---
@router.get("/categories")
async def read_categories() -> List[dict]:
    return await Category_PydanticRead.from_queryset(Category.all())

@router.post("/categories")
async def create_category(category: CategoryCreate) -> dict:
    obj = await Category.create(name=category.name)
    return await Category_PydanticRead.from_tortoise_orm(obj)

@router.put("/categories/{category_id}")
async def update_category(category_id: int, category: CategoryCreate) -> dict:
    obj = await Category.get_or_none(id=category_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Category not found")
    await obj.update_from_dict({"name": category.name})
    await obj.save()
    return await Category_PydanticRead.from_tortoise_orm(obj)

@router.delete("/categories/{category_id}")
async def delete_category(category_id: int):
    obj = await Category.get_or_none(id=category_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Category not found")
    await obj.delete()
    return {"ok": True}


# --- Type CRUD ---
@router.get("/types")
async def read_types() -> List[dict]:
    return await Type_PydanticRead.from_queryset(Type.all())

@router.post("/types")
async def create_type(type_: TypeCreate) -> dict:
    obj = await Type.create(name=type_.name)
    return await Type_PydanticRead.from_tortoise_orm(obj)

@router.put("/types/{type_id}")
async def update_type(type_id: int, type_: TypeCreate) -> dict:
    obj = await Type.get_or_none(id=type_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Type not found")
    await obj.update_from_dict({"name": type_.name})
    await obj.save()
    return await Type_PydanticRead.from_tortoise_orm(obj)

@router.delete("/types/{type_id}")
async def delete_type(type_id: int):
    obj = await Type.get_or_none(id=type_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Type not found")
    await obj.delete()
    return {"ok": True}


# --- Article CRUD ---
@router.get("/articles")
async def read_articles() -> List[dict]:
    return await Article_PydanticRead.from_queryset(Article.all().prefetch_related("category", "type", "article_name"))

@router.get("/articles/{article_id}")
async def read_article(article_id: int) -> dict:
    obj = await Article.get_or_none(id=article_id).prefetch_related("category", "type", "article_name")
    if not obj:
        raise HTTPException(status_code=404, detail="Article not found")
    return await Article_PydanticRead.from_tortoise_orm(obj)

@router.post("/articles")
async def create_article(article: ArticleCreate) -> dict:
    # Verify that related objects exist
    category = await Category.get_or_none(id=article.category_id)
    type_ = await Type.get_or_none(id=article.type_id)
    article_name = await ArticleName.get_or_none(id=article.article_name_id)
    
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")
    if not type_:
        raise HTTPException(status_code=404, detail="Type not found")
    if not article_name:
        raise HTTPException(status_code=404, detail="Article name not found")
    
    obj = await Article.create(
        title=article.title,
        content=article.content,
        category_id=article.category_id,
        type_id=article.type_id,
        article_name_id=article.article_name_id
    )
    return await Article_PydanticRead.from_tortoise_orm(obj)

@router.put("/articles/{article_id}")
async def update_article(article_id: int, article: ArticleCreate) -> dict:
    obj = await Article.get_or_none(id=article_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Article not found")
    
    # Verify that related objects exist
    category = await Category.get_or_none(id=article.category_id)
    type_ = await Type.get_or_none(id=article.type_id)
    article_name = await ArticleName.get_or_none(id=article.article_name_id)
    
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")
    if not type_:
        raise HTTPException(status_code=404, detail="Type not found")
    if not article_name:
        raise HTTPException(status_code=404, detail="Article name not found")
    
    await obj.update_from_dict({
        "title": article.title,
        "content": article.content,
        "category_id": article.category_id,
        "type_id": article.type_id,
        "article_name_id": article.article_name_id
    })
    await obj.save()
    return await Article_PydanticRead.from_tortoise_orm(obj)

@router.delete("/articles/{article_id}")
async def delete_article(article_id: int):
    obj = await Article.get_or_none(id=article_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Article not found")
    await obj.delete()
    return {"ok": True}


# --- ArticleName CRUD ---
@router.get("/article-names")
async def read_article_names() -> List[dict]:
    return await ArticleName_PydanticRead.from_queryset(ArticleName.all())

@router.post("/article-names")
async def create_article_name(article_name: ArticleNameCreate) -> dict:
    obj = await ArticleName.create(name=article_name.name)
    return await ArticleName_PydanticRead.from_tortoise_orm(obj)

@router.put("/article-names/{article_name_id}")
async def update_article_name(article_name_id: int, article_name: ArticleNameCreate) -> dict:
    obj = await ArticleName.get_or_none(id=article_name_id)
    if not obj:
        raise HTTPException(status_code=404, detail="ArticleName not found")
    await obj.update_from_dict({"name": article_name.name})
    await obj.save()
    return await ArticleName_PydanticRead.from_tortoise_orm(obj)

@router.delete("/article-names/{article_name_id}")
async def delete_article_name(article_name_id: int):
    obj = await ArticleName.get_or_none(id=article_name_id)
    if not obj:
        raise HTTPException(status_code=404, detail="ArticleName not found")
    await obj.delete()
    return {"ok": True}


# --- Article CRUD ---
@router.get("/articles")
async def read_articles() -> List[dict]:
    return await Article_PydanticRead.from_queryset(Article.all())

@router.post("/articles")
async def create_article(article: ArticleCreate) -> dict:
    obj = await Article.create(
        title=article.title,
        content=article.content,
        category_id=article.category_id,
        type_id=article.type_id,
        article_name_id=article.article_name_id
    )
    return await Article_PydanticRead.from_tortoise_orm(obj)

@router.put("/articles/{article_id}")
async def update_article(article_id: int, article: ArticleCreate) -> dict:
    obj = await Article.get_or_none(id=article_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Article not found")
    await obj.update_from_dict({
        "title": article.title,
        "content": article.content,
        "category_id": article.category_id,
        "type_id": article.type_id,
        "article_name_id": article.article_name_id
    })
    await obj.save()
    return await Article_PydanticRead.from_tortoise_orm(obj)

@router.delete("/articles/{article_id}")
async def delete_article(article_id: int):
    obj = await Article.get_or_none(id=article_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Article not found")
    await obj.delete()
    return {"ok": True}
