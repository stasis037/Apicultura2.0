from fastapi import APIRouter, HTTPException, Depends
from tortoise.contrib.fastapi import HTTPNotFoundError
from src.models.base import Category, Type, ArticleName
from typing import List
from pydantic import BaseModel
from src.api.auth import authenticate_user

router = APIRouter(dependencies=[Depends(authenticate_user)])

# Pydantic models for request/response
class CategoryCreate(BaseModel):
    name: str

class CategoryResponse(BaseModel):
    id: int
    name: str

    class Config:
        from_attributes = True

class TypeCreate(BaseModel):
    name: str

class TypeResponse(BaseModel):
    id: int
    name: str

    class Config:
        from_attributes = True

class ArticleNameCreate(BaseModel):
    name: str

class ArticleNameResponse(BaseModel):
    id: int
    name: str

    class Config:
        from_attributes = True

# Category endpoints
@router.post("/categories/", response_model=CategoryResponse)
async def create_category(category: CategoryCreate):
    category_obj = await Category.create(**category.dict())
    return await CategoryResponse.from_orm(category_obj)

@router.get("/categories/", response_model=List[CategoryResponse])
async def get_categories():
    return await Category.all()

@router.get("/categories/{category_id}", response_model=CategoryResponse, responses={404: {"model": HTTPNotFoundError}})
async def get_category(category_id: int):
    return await Category.get(id=category_id)

@router.put("/categories/{category_id}", response_model=CategoryResponse, responses={404: {"model": HTTPNotFoundError}})
async def update_category(category_id: int, category: CategoryCreate):
    await Category.filter(id=category_id).update(**category.dict())
    return await CategoryResponse.from_orm(await Category.get(id=category_id))

@router.delete("/categories/{category_id}", responses={404: {"model": HTTPNotFoundError}})
async def delete_category(category_id: int):
    deleted_count = await Category.filter(id=category_id).delete()
    if not deleted_count:
        raise HTTPException(status_code=404, detail=f"Category {category_id} not found")
    return {"message": f"Category {category_id} deleted successfully"}

# Type endpoints
@router.post("/types/", response_model=TypeResponse)
async def create_type(type_data: TypeCreate):
    type_obj = await Type.create(**type_data.dict())
    return await TypeResponse.from_orm(type_obj)

@router.get("/types/", response_model=List[TypeResponse])
async def get_types():
    return await Type.all()

@router.get("/types/{type_id}", response_model=TypeResponse, responses={404: {"model": HTTPNotFoundError}})
async def get_type(type_id: int):
    return await Type.get(id=type_id)

@router.put("/types/{type_id}", response_model=TypeResponse, responses={404: {"model": HTTPNotFoundError}})
async def update_type(type_id: int, type_data: TypeCreate):
    await Type.filter(id=type_id).update(**type_data.dict())
    return await TypeResponse.from_orm(await Type.get(id=type_id))

@router.delete("/types/{type_id}", responses={404: {"model": HTTPNotFoundError}})
async def delete_type(type_id: int):
    deleted_count = await Type.filter(id=type_id).delete()
    if not deleted_count:
        raise HTTPException(status_code=404, detail=f"Type {type_id} not found")
    return {"message": f"Type {type_id} deleted successfully"}

# ArticleName endpoints
@router.post("/article_names/", response_model=ArticleNameResponse)
async def create_article_name(article_name_data: ArticleNameCreate):
    article_name_obj = await ArticleName.create(**article_name_data.dict())
    return await ArticleNameResponse.from_orm(article_name_obj)

@router.get("/article_names/", response_model=List[ArticleNameResponse])
async def get_article_names():
    return await ArticleName.all()

@router.get("/article_names/{article_name_id}", response_model=ArticleNameResponse, responses={404: {"model": HTTPNotFoundError}})
async def get_article_name(article_name_id: int):
    return await ArticleName.get(id=article_name_id)

@router.put("/article_names/{article_name_id}", response_model=ArticleNameResponse, responses={404: {"model": HTTPNotFoundError}})
async def update_article_name(article_name_id: int, article_name_data: ArticleNameCreate):
    await ArticleName.filter(id=article_name_id).update(**article_name_data.dict())
    return await ArticleNameResponse.from_orm(await ArticleName.get(id=article_name_id))

@router.delete("/article_names/{article_name_id}", responses={404: {"model": HTTPNotFoundError}})
async def delete_article_name(article_name_id: int):
    deleted_count = await ArticleName.filter(id=article_name_id).delete()
    if not deleted_count:
        raise HTTPException(status_code=404, detail=f"ArticleName {article_name_id} not found")
    return {"message": f"ArticleName {article_name_id} deleted successfully"}

