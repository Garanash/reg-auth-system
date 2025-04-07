from pydantic import BaseModel, ConfigDict


class UserBase(BaseModel):
    username: str
    password: str
    email: str
    role: str
    first_name: str
    last_name: str

class UserCreate(UserBase):
    pass

class UserUpdate(UserBase):
    pass

class UserUpdatePartial(UserBase):
    username: str | None = None
    password: str | None = None
    email: str | None = None
    role: str | None = None
    first_name: str | None = None
    last_name: str | None = None

class UserSchema(UserBase):
    model_config = ConfigDict(from_attributes=True)
    id: int
