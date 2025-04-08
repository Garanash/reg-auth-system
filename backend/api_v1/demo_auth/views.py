from typing import Annotated

from fastapi import APIRouter, Depends
from fastapi.security import HTTPBasicCredentials, HTTPBasic

router = APIRouter(prefix='/new_auth', tags=['new_auth'])

security = HTTPBasic()


@router.get('/basic_auth')
def demo_basic_auth_credentials(credentials: Annotated[HTTPBasicCredentials, Depends(security)]):
    return {
        "message": "Hi!",
        "username": credentials.username,
        "password": credentials.password
    }
