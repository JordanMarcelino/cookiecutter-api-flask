import bcrypt

from decouple import config

from flask_bcrypt import Bcrypt

from flask_caching import Cache

from flask_jwt_extended import JWTManager

from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

from flask_smorest import Api

from flask_sqlalchemy import SQLAlchemy

from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


api = Api()

bcrypt_ext = Bcrypt()

cache = Cache()

db = SQLAlchemy(model_class=Base)

jwt = JWTManager()

limiter = Limiter(
    get_remote_address,
    default_limits=["200 per day", "50 per hour"],
    storage_uri="memory://",
)

mode = config("MODE", default="dev")
