from fastapi import APIRouter
from fastapi.responses import JSONResponse

from utils.jwt_manager import create_token
from schemas.user import User

user_router = APIRouter()


@user_router.post('/login', tags=['auth'], response_model=str, status_code=200)
def login(user: User):
    if user.email == 'admin@gmail.com' and user.password == 'admin':
        token: str = create_token(user.dict())
        return JSONResponse(content=token, status_code=200)