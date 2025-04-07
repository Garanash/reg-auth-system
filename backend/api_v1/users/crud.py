from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession
from .schemas import UserCreate, UserUpdatePartial, UserSchema
from core.models import User


async def get_users(session: AsyncSession):
    stmt = select(User).order_by(User.id)
    result: Result = await session.execute(stmt)
    users = result.scalars().all()
    return list(users)


async def get_user(session: AsyncSession, user_id: int):
    return await session.get(User, user_id)


async def create_user(session: AsyncSession, user_in: UserCreate):
    user = User(**user_in.model_dump())
    session.add(user)
    await session.commit()
    return user


async def update_user_partial(session: AsyncSession, user_up: UserSchema, user_in: UserUpdatePartial):
    for name, value in user_in.model_dump(exclude_unset=True).items():
        setattr(user_up, name, value)
    await session.commit()
    return user_up

async def delete_user_by_id(session: AsyncSession, user: User):
    await session.delete(user)
    await session.commit()
    return user