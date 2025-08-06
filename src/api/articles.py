
from fastapi import APIRouter, Request, HTTPException, status, Depends
from tortoise.contrib.pydantic import pydantic_model_creator
from src.models.base import Article
from src.api.auth import authenticate_user

router = APIRouter(dependencies=[Depends(authenticate_user)])

Article_Pydantic = pydantic_model_creator(Article, name="Article")
ArticleIn_Pydantic = pydantic_model_creator(Article, name="ArticleIn", exclude_readonly=True)

@router.get("/health")
async def health_check():
    return {"status": "ok", "message": "API is running"}

@router.get("/articles", response_model=list[Article_Pydantic])
async def get_articles():
    return await Article_Pydantic.from_queryset(Article.all())

@router.post("/articles", response_model=Article_Pydantic, status_code=status.HTTP_201_CREATED)
async def create_article(article: ArticleIn_Pydantic):
    article_obj = await Article.create(**article.dict(exclude_unset=True))
    return await Article_Pydantic.from_tortoise_orm(article_obj)

@router.put("/articles/{article_id}", response_model=Article_Pydantic)
async def update_article(article_id: int, article: ArticleIn_Pydantic):
    await Article.filter(id=article_id).update(**article.dict(exclude_unset=True))
    article_obj = await Article.filter(id=article_id).first()
    if not article_obj:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Article not found")
    return await Article_Pydantic.from_tortoise_orm(article_obj)

@router.delete("/articles/{article_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_article(article_id: int):
    deleted_count = await Article.filter(id=article_id).delete()
    if not deleted_count:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Article not found")
    return
