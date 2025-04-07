from pydantic import BaseModel, ConfigDict


class UserBase(BaseModel):
    username: str
    password: str
    email: str

class UserCreate(UserBase):
    pass

class UserUpdate(UserBase):
    pass

class UserUpdatePartial(UserBase):
    username: str | None = None
    password: str | None = None
    email: str | None = None

class UserSchema(UserBase):
    model_config = ConfigDict(from_attributes=True)
    id: int
