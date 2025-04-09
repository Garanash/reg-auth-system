from typing import Annotated

from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBasicCredentials, HTTPBasic

from api_v1.users.crud import get_user_by_username
from core.models import db_helper
from sqlalchemy.ext.asyncio import AsyncSession

security = HTTPBasic()

UNAUTH_EXC = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Invalid username or password",
    headers={"WWW-Authenticate": "Basic"}
)


async def get_auth_user_username(
        credentials: Annotated[HTTPBasicCredentials, Depends(security)],
        session: AsyncSession = Depends(db_helper.session_dependency)):
    user = await get_user_by_username(session=session, username=credentials.username)
    if user is not None:
        if user.password == credentials.password:
            return user.__dict__
    raise UNAUTH_EXC
