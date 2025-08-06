from fastapi import APIRouter, HTTPException, Response, Request, Depends, status
from pydantic import BaseModel
from passlib.hash import pbkdf2_sha256
from src.models.base import User

router = APIRouter()

class LoginRequest(BaseModel):
    username: str
    password: str

class RegisterRequest(BaseModel):
    username: str
    password: str

@router.post("/register", status_code=status.HTTP_201_CREATED)
async def register(user_data: RegisterRequest):
    hashed_password = pbkdf2_sha256.hash(user_data.password)
    try:
        user = await User.create(username=user_data.username, password_hash=hashed_password)
        return {"status": "success", "message": "User registered successfully"}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Username already exists or other registration error")

@router.post("/login")
async def login(login_data: LoginRequest, response: Response):
    user = await User.get_or_none(username=login_data.username)
    if not user or not pbkdf2_sha256.verify(login_data.password, user.password_hash):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
    
    response.set_cookie(
        key="session",
        value=user.username, # Store username in session for simplicity
        httponly=True,
        samesite='lax',
        max_age=3600  # 1 hour
    )
    return {"status": "success", "message": "Login successful"}

@router.post("/logout")
async def logout(response: Response):
    response.delete_cookie(key="session")
    return {"status": "success", "message": "Logged out successfully"}

async def authenticate_user(request: Request):
    session_id = request.cookies.get("session")
    if not session_id:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Not authenticated")
    user = await User.get_or_none(username=session_id)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid session")
    return user
