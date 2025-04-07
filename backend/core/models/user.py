from .base import Base
from sqlalchemy.orm import Mapped

class User(Base):
    username: Mapped[str]
    password: Mapped[str]
    email: Mapped[str]
    role: Mapped[str]
    first_name: Mapped[str]
    last_name: Mapped[str]
