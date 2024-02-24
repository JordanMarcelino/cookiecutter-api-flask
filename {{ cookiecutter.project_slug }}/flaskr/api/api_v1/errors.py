from flask_jwt_extended.exceptions import NoAuthorizationError

from flask_smorest import Blueprint

from flaskr.schemas import WebResponse

errors_bp = Blueprint("errors", __name__)


@errors_bp.app_errorhandler(400)
@errors_bp.response(400, WebResponse)
def bad_request(error):
    return WebResponse().load(
        data={"status": {"code": 400, "message": "Bad request!"}, "data": None}
    )


@errors_bp.app_errorhandler(401)
@errors_bp.response(401, WebResponse)
def unauthorized(error):
    return WebResponse().load(
        data={"status": {"code": 401, "message": "Unauthorized!"}, "data": None}
    )

    
@errors_bp.app_errorhandler(NoAuthorizationError)
@errors_bp.response(401, WebResponse)
def jwt_error(error):
    return WebResponse().load(
        data={"status": {"code": 401, "message": "Unauthorized!"}, "data": None}
    )


@errors_bp.app_errorhandler(404)
@errors_bp.response(404, WebResponse)
def not_found(error):
    return WebResponse().load(
        data={"status": {"code": 404, "message": "URL not found!"}, "data": None}
    )


@errors_bp.app_errorhandler(405)
@errors_bp.response(405, WebResponse)
def method_not_allowed(error):
    return WebResponse().load(
        data={
            "status": {"code": 405, "message": "Method aren't allowed!"},
            "data": None,
        }
    )


@errors_bp.app_errorhandler(422)
@errors_bp.response(422, WebResponse)
def unprocessable_entity(error):
    return WebResponse().load(
        data={
            "status": {"code": 422, "message": "Unprocessable entity!"},
            "data": None,
        }
    )


@errors_bp.app_errorhandler(429)
@errors_bp.response(429, WebResponse)
def rate_limit_exceed(error):
    return WebResponse().load(
        data={
            "status": {
                "code": 429,
                "message": "Rate limit exceed, please try again later!",
            },
            "data": None,
        }
    )


@errors_bp.app_errorhandler(500)
@errors_bp.response(500, WebResponse)
def internal_server_error(error):
    return WebResponse().load(
        data={
            "status": {"code": 500, "message": "Internal server errror!"},
            "data": None,
        }
    )
