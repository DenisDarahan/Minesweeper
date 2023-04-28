from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm

from server.db import db
from server.utils import Auth, IncorrectUsernameError, IncorrectPasswordError
from server.schemas import Token, UserCreate, UserDB


router = APIRouter(prefix=f'/auth', tags=['auth'])


@router.post('/sign-up', response_model=Token)
async def sign_up(user: UserCreate):
    user_id = await db.user.create(user.username, Auth.hash_password(user.password))
    return Auth.create_token(user_id, user.username)


@router.post('/sign-in', response_model=Token)
async def sign_in(form_data: OAuth2PasswordRequestForm = Depends()):
    user = await db.user.get_by_username(form_data.username)
    if not user:
        raise IncorrectUsernameError

    user = UserDB.parse_obj(user)
    if not Auth.verify_password(form_data.password, user.password_hash):
        raise IncorrectPasswordError

    return Auth.create_token(user.id, user.username)
