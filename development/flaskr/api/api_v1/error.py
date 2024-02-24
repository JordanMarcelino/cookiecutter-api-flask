from flask import Blueprint

from flaskr.schemas import Status
from flaskr.schemas import WebResponse

error_bp = Blueprint("errors", __name__)


@error_bp.errorhandler(400)
def bad_request(error):
    return WebResponse[None](Status(code=400, message="Bad request!")), 400


@error_bp.errorhandler(404)
def not_found(error):
    return WebResponse[None](Status(code=404, message="URL not found!")), 404


@error_bp.errorhandler(405)
def method_not_allowed(error):
    return WebResponse[None](
        Status(code=405, message="Request method aren't allowed!")
    ), 405


@error_bp.errorhandler(429)
def rate_limit_exceed(error):
    return WebResponse[None](
        Status(code=429, message="Rate limit exceed, please try again later!")
    ), 429


@error_bp.errorhandler(500)
def internal_server_error(error):
    return WebResponse[None](Status(code=500, message="Internal server error!"))
