from .base import Base
from sqlalchemy.orm import Mapped

class User(Base):
    username: Mapped[str]
    password: Mapped[str]
    email: Mapped[str]