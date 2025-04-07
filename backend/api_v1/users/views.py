from fastapi import APIRouter, HTTPException, status
from core.models import db_helper
from fastapi.params import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from . import crud
from .schemas import User, UserCreate

router = APIRouter(prefix='/user', tags=['Users'])


@router.get('/', response_model=list[User])
async def get_users(session: AsyncSession = Depends(db_helper.scoped_session_dependency)):
    return await crud.get_users(session=session)


@router.post('/')
async def create_user(user_in: UserCreate, session: AsyncSession = Depends(db_helper.session_dependency)):
    return await crud.create_user(session=session, user_in=user_in)


@router.get('/{user_id}/', response_model=User)
async def get_user_by_id(user_id: int, session: AsyncSession = Depends(db_helper.session_dependency)):
    user = await crud.get_user(session=session, user_id=user_id)
    if user is not None:
        return user

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"user with id {user_id} not found!"
    )
