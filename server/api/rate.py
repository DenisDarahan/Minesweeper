from typing import Annotated, Any

from asyncpg import Connection
from fastapi import APIRouter, Body, Query, Depends, status

from server.db import db
from server.utils import get_current_user
from server.schemas import User, RateCreate, RateRecord


router = APIRouter(prefix='/rate', tags=['rate'])


@router.post('/create', status_code=status.HTTP_200_OK, response_model=list[RateRecord])
async def create(user: Annotated[User, Depends(get_current_user)], rate: Annotated[RateCreate, Body()],
                 con: Annotated[Connection, Depends(db.connector().get)]):
    rate_id = await db.rate.poor_create(con, user.id, **rate.dict())
    return await db.rate.poor_rate(con, rate_id)


@router.get('/me', status_code=status.HTTP_200_OK, response_model=list[RateRecord])
async def me(user: Annotated[User, Depends(get_current_user)]):
    return await db.rate.me(user.id)


@router.get('/top', status_code=status.HTTP_200_OK, dependencies=[Depends(get_current_user)],
            response_model=dict[str, Any])
async def top(limit: int = Query(10), offset: int = Query(0)):
    return await db.rate.top(limit, offset)
