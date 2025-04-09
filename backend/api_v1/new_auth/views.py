from typing import Annotated

from fastapi import APIRouter, Depends, Response
from fastapi.security import HTTPBasicCredentials, HTTPBasic

from api_v1.new_auth.utils import get_auth_user_username

router = APIRouter(prefix='/new_auth', tags=['new_auth'])

security = HTTPBasic()


@router.get('/basic_auth')
async def basic_auth_credentials(auth_user: str = Depends(get_auth_user_username)):
    return {
        "props": auth_user,
    }

@router.post('/login-cookie')
def auth_login_cookie(
        response: Response,
        auth_username: str = Depends(get_auth_user_username),
        ):
    pass