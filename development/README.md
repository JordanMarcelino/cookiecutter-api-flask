# {{cookiecutter.project_name}}

{{cookiecutter.description}}

## Tech Stack

-   Python : https://www.python.org/
-   PostgreSQL (Database) : https://github.com/postgres/postgres
-   Docker (Container) : https://www.docker.com/

## Framework & Library

-   Flask (HTTP Framework) : https://flask.palletsprojects.com/en/3.0.x/
-   Flask Bcrypt (Hashing) : https://pypi.org/project/bcrypt/
-   Flask Cache (Caching) : https://flask.palletsprojects.com/en/2.2.x/patterns/caching/
-   Flask CORS (CORS) : https://flask-cors.readthedocs.io/en/latest/
-   Flask JWT (Authentication) : https://flask-jwt-extended.readthedocs.io/en/stable/
-   Flask Limiter (Rate Limiter) : https://flask-limiter.readthedocs.io/en/stable/
-   Flask Smorest (REST-API) : https://flask-smorest.readthedocs.io/en/latest/quickstart.html
-   Flask SQLAlchemy (ORM) : https://flask-sqlalchemy.palletsprojects.com/en/3.1.x/
-   Pydantic-Settings (Configuration) : https://docs.pydantic.dev/latest/concepts/pydantic_settings/
-   Loguru (Logging) : https://github.com/Delgan/loguru
-   Pytest (Testing) : https://docs.pytest.org/en/8.0.x/
-   Decouple (Env) : https://pypi.org/project/python-decouple/
-   Gunicorn (WSGI) : https://gunicorn.org/

## How To Run / Install on Your Local Machine

--> Build & run docker container :

```bash
docker compose -f .\deploy\docker-compose.yaml up --build
```

--> Stop the container :

```bash
cd ./build/package/
docker-compose down
```
