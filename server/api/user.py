from typing import Annotated

from fastapi import APIRouter, Path, HTTPException, Depends, status

from server.db import db
from server.utils import get_current_user
from server.schemas import User, UserInfo


router = APIRouter(prefix='/user', tags=['user'])


@router.get('/get/{user_id}', dependencies=[Depends(get_current_user)], status_code=status.HTTP_200_OK,
            response_model=UserInfo)
async def get_user(user_id: Annotated[int, Path()]) -> UserInfo:
    user_info = await db.user.get_info(user_id)
    if not user_info:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='User with such ID not exists')
    return user_info


@router.get('/me', status_code=status.HTTP_200_OK, response_model=UserInfo)
async def me(user: Annotated[User, Depends(get_current_user)]):
    return await db.user.get_info(user.id)
