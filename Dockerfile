FROM python:3.13.2-slim

WORKDIR /app

RUN python -m pip install --upgrade pip wheel setuptools poetry --no-cache-dir

COPY ./pyproject.toml .

RUN poetry config virtualenvs.create false && poetry install --no-root --without dev --no-cache

COPY ./src/ .

COPY ./.env .
