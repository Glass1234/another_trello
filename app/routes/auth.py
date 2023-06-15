import jwt
from fastapi import APIRouter, WebSocket, WebSocketDisconnect, Request, HTTPException, Depends
from fastapi.responses import HTMLResponse
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from passlib.handlers.pbkdf2 import pbkdf2_sha256
from starlette import status
from tortoise.contrib.pydantic import pydantic_model_creator

from app.db.models import User
from app.schemas import ClientUser

router_auth = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
JWT_SECRET = 'myjwtsecret'


def fake_hash_password(password: str):
    return "fakehashed" + password


async def check_token(token: str = Depends(oauth2_scheme)):
    try:
        user_id = jwt.decode(token, JWT_SECRET, algorithms=['HS256'])['user_id']
        model = await User.filter(id=user_id).first()
    except:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Invalid username or password'
        )
    return model


@router_auth.post('/reg')
async def reg(user: ClientUser):
    model = await User.filter(name=user.user_name).first()
    if model:
        return {'status_code': 1, 'response': 'Данный пользователь уже зарегестрирован'}
    await User(name=user.user_name, passwd=pbkdf2_sha256.hash(user.passwd)).save()
    return {'status_code': 0, 'response': 'Вы успешно зарегестрированы'}


@router_auth.post('/auth')
async def home(user: ClientUser):
    model = await User.filter(name=user.user_name, passwd=user.passwd).first()
    if not model:
        return {'status_code': 1, 'response': 'Неверные данные'}
    return {'status_code': 0, 'response': 'Вы успешно авторизированны'}


@router_auth.post('/token')
async def token(form_data: OAuth2PasswordRequestForm = Depends()):
    model = await User.filter(name=form_data.username).first()
    if not model:
        return {'status_code': 1, 'response': 'Неверные данные'}
    if not pbkdf2_sha256.verify(form_data.password, model.passwd):
        return {'status_code': 1, 'response': 'Неверные данные'}
    token = jwt.encode({"user_id": model.id}, JWT_SECRET)
    return {'access_token': token, 'status_code': 0, 'response': 'Вы успешно авторизированны'}


@router_auth.get('/test')
async def index(token: str = Depends(check_token)):
    return {'the_token': token}
