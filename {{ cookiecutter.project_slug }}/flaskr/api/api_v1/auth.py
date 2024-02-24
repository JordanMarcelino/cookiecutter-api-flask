from flask import jsonify

from flask_jwt_extended import create_access_token
from flask_jwt_extended import set_access_cookies
from flask_jwt_extended import jwt_required

from flask_smorest import Blueprint

from flaskr.core import prod_settings
from flaskr.schemas import AuthResponse
from flaskr.schemas import UserLoginRequest
from flaskr.schemas import WebResponse

auth_bp = Blueprint("auth", __name__, url_prefix=f"{prod_settings.API_V1_STR}/auth")


@auth_bp.get("/")
@auth_bp.response(200, WebResponse)
def root():
    return WebResponse().load(
        data={"status": {"code": 200, "message": "Auth API"}, "data": None}
    )


@auth_bp.post("/login")
@auth_bp.arguments(UserLoginRequest, location="json")
@auth_bp.response(200, WebResponse)
def login(args):
    access_token = create_access_token(args["email"])

    res = jsonify(
        WebResponse().load(
            data={
                "status": {"code": 200, "message": "Success login!"},
                "data": AuthResponse().load(data={"token": access_token}),
            }
        )
    )

    set_access_cookies(res, access_token)

    return res


@jwt_required()
@auth_bp.post("/restricted")
@auth_bp.arguments(UserLoginRequest, location="json")
@auth_bp.response(200, WebResponse)
def restricted(args):
    return WebResponse().load(
        data={
            "status": {"code": 200, "message": "Success validating JWT!"},
            "data": args,
        }
    )
