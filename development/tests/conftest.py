from typing import Generator

from flask import Flask
from flask.testing import FlaskClient

import pytest

from flaskr import create_app
from flaskr.core import test_settings


@pytest.fixture
def app() -> Generator[Flask, None, None]:
    app = create_app(test_settings)

    with app.app_context():
        yield app

        # db.drop_all()


@pytest.fixture
def client(app: Flask) -> FlaskClient:
    return app.test_client()
