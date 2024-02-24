from flask.testing import FlaskClient

from flaskr.core import test_settings


def test_root_endpoint_success(client: FlaskClient):
    response = client.get(f"{test_settings.API_V1_STR}/auth/", follow_redirects=True)

    json = response.get_json()

    assert response.status_code == 200
    assert json["status"]["code"] == 200
    assert json["status"]["message"] == "Auth API"
    assert json["data"] is None


def test_root_endpoint_failed_method_not_allowed(client: FlaskClient):
    response = client.post(f"{test_settings.API_V1_STR}/auth/", follow_redirects=True)

    json = response.get_json()

    assert response.status_code == 405
    assert json["status"]["code"] == 405
    assert json["status"]["message"] == "Method aren't allowed!"
    assert json["data"] is None


def test_login_success(client: FlaskClient):
    payload = {"email": "test@gmail.com", "password": "secret"}
    response = client.post(
        f"{test_settings.API_V1_STR}/auth/login", json=payload, follow_redirects=True
    )

    json = response.get_json()

    assert response.status_code == 200
    assert response.headers.get("Set-Cookie") is not None
    assert json["status"]["code"] == 200
    assert json["status"]["message"] == "Success login!"
    assert json["data"] is not None


def test_login_failed_invalid_email_format(client: FlaskClient):
    payload = {"email": "test", "password": "secret"}
    response = client.post(
        f"{test_settings.API_V1_STR}/auth/login", json=payload, follow_redirects=True
    )

    json = response.get_json()

    assert response.status_code == 422
    assert response.headers.get("Set-Cookie") is None
    assert json["status"]["code"] == 422
    assert json["status"]["message"] == "Unprocessable entity!"
    assert json["data"] is None


def test_jwt_validation_success(client: FlaskClient):
    payload = {"email": "test@gmail.com", "password": "secret"}
    response = client.post(
        f"{test_settings.API_V1_STR}/auth/login", json=payload, follow_redirects=True
    )

    response = client.post(
        f"{test_settings.API_V1_STR}/auth/restricted",
        json=payload,
        follow_redirects=True,
        headers={"Cookie": response.headers.get("Set-Cookie")},
    )

    json = response.get_json()

    assert response.status_code == 200
    assert response.headers.get("Set-Cookie") is None
    assert json["status"]["code"] == 200
    assert json["status"]["message"] == "Success validating JWT!"
    assert json["data"] == payload
    
def test_jwt_validation_failed_missing_jwt(client: FlaskClient):
    payload = {"email": "test@gmail.com", "password": "secret"}

    response = client.post(
        f"{test_settings.API_V1_STR}/auth/restricted",
        json=payload,
        follow_redirects=True
    )

    json = response.get_json()

    assert response.status_code == 401
    assert json["status"]["code"] == 401
    assert json["status"]["message"] == "Unauthorized!"
    assert json["data"] is None
