from fastapi_users.authentication import JWTAuthentication
from fastapi_users.db import SQLAlchemyUserDatabase
from starlette.requests import Request

from core.database import database
from .models import UserTable
from .schemas import UserDB

users = UserTable.__table__
user_db = SQLAlchemyUserDatabase(UserDB, database, users)

SECRET = "adoibhepibu3e0934hq234jqh89g443g3jkg34y829y34"

auth_backends = []

jwt_authentication = JWTAuthentication(secret=SECRET, lifetime_seconds=3600)

auth_backends.append(jwt_authentication)



