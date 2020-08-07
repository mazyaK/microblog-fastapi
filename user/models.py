from sqlalchemy import Column, String, DateTime, Integer
from fastapi_users.db import SQLAlchemyBaseUserTable
from core.database import Base


class UserTable(Base, SQLAlchemyBaseUserTable):
    name = Column(String, unique=True)
    date = Column(DateTime)


users = UserTable.__table__

