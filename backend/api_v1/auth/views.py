from fastapi import APIRouter, HTTPException, status, Depends, Response

from api_v1.auth.schemas import UserLoginSchema

from api_v1.users.crud import get_user_by_username
from core.models import db_helper

from sqlalchemy.ext.asyncio import AsyncSession

from .config_authx import security, config

router = APIRouter(tags=['login'])


@router.post('/login')
async def login(creds: UserLoginSchema,
                response: Response,
                session: AsyncSession = Depends(db_helper.session_dependency),
                ):
    user = await get_user_by_username(username=creds.username, session=session)
    if user is not None:
        if user.password == creds.password:
            token = security.create_access_token(uid='12345')
            response.set_cookie(config.JWT_ACCESS_COOKIE_NAME, token)
            return {'access token': token}
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Incorrect username or password')
