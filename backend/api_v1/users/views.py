from fastapi import APIRouter
from core.models import db_helper, User
from fastapi.params import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from . import crud
from .dependencies import user_by_id
from .schemas import UserCreate, UserUpdatePartial, UserSchema
from ..auth.config_authx import security

router = APIRouter(prefix='/user', tags=['Users'])


@router.get('/', response_model=list[UserSchema])
async def get_users(session: AsyncSession = Depends(db_helper.scoped_session_dependency)):
    return await crud.get_users(session=session)


@router.post('/')
async def create_user(user_in: UserCreate, session: AsyncSession = Depends(db_helper.session_dependency)):
    return await crud.create_user(session=session, user_in=user_in)


@router.get('/{user_id}/', response_model=UserSchema)
async def get_user_by_id(user: User = Depends(user_by_id)):
    return user


@router.patch('/{user_id}/')
async def update_user(user_update: UserUpdatePartial,
                      user: User = Depends(user_by_id),
                      session: AsyncSession = Depends(db_helper.session_dependency)):
    return await crud.update_user_partial(user_in=user_update, user_up=user, session=session)


@router.delete('/{user_id}/')
async def delete_user(
        user: User = Depends(user_by_id),
        session: AsyncSession = Depends(db_helper.session_dependency)
):
    return await crud.delete_user_by_id(user=user, session=session)