from datetime import datetime
from datetime import timedelta

from flask import Flask
from flask import Response

from flask_cors import CORS

from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import set_access_cookies

from flask_smorest import Api

from flaskr.api.api_v1 import error_bp
from flaskr.core import dev_settings
from flaskr.core import logger
from flaskr.core import prod_settings
from flaskr.core import Settings
from flaskr.extensions import api
from flaskr.extensions import bcrypt_ext
from flaskr.extensions import cache
from flaskr.extensions import db
from flaskr.extensions import limiter
from flaskr.extensions import mode
from flaskr.extensions import jwt


def create_app(
    config: Settings = prod_settings if mode == "production" else dev_settings,
) -> Flask:
    app = Flask(__name__)

    app.config.from_object(config)

    register_extensions(app)
    register_blueprints(app)
    init_db(app)

    @app.after_request
    def refresh_expiring_jwts(response: Response) -> Response:
        try:
            exp_timestamp = get_jwt()["exp"]
            now = datetime.now()
            target_timestamp = datetime.timestamp(now + timedelta(minutes=30))
            if target_timestamp > exp_timestamp:
                access_token = create_access_token(identity=get_jwt_identity())
                set_access_cookies(response, access_token)
            return response
        except (RuntimeError, KeyError):
            # Case where there is not a valid JWT. Just return the original response
            return response

    return app


def register_extensions(app: Flask):
    """Register Flask extensions."""
    CORS(
        app,
        resources={
            # update to FE or production link
            r"/*": {"origins": ["http://localhost:5000", "https://example.com"]}
        },
    )

    api.init_app(app)
    bcrypt_ext.init_app(app)
    cache.init_app(
        app,
        config={
            "CACHE_TYPE": app.config.get("CACHE_TYPE", "SimpleCache"),
            "CACHE_DEFAULT_TIMEOUT": app.config.get("CACHE_DEFAULT_TIMEOUT", 300),
        },
    )
    db.init_app(app)
    limiter.init_app(app)
    jwt.init_app(app)


def register_blueprints(app: Api):
    """Register Flask blueprints."""

    app.register_blueprint(error_bp)


def init_db(app: Flask):
    with app.app_context():
        try:
            db.create_all()

        except Exception as exc:
            logger.error(exc)


app = create_app()
