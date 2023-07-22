FROM python:3.11-slim-bullseye

WORKDIR /app

ENV PYTHONPATH=/app
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8
ENV DEBIAN_FRONTEND="noninteractive"
ENV SQLALCHEMY_TRACK_MODIFICATIONS=False

# Setting up locale
RUN apt-get update \
    && apt-get install -y locales locales-all \
    && locale-gen en_US.UTF-8

# Essentials
RUN apt-get update -y && apt-get install -y curl libpq-dev
RUN pip install pipenv

# Project setup
COPY . .
RUN find . -type d -name __pycache__ -exec rm -r {} \+ 2>/dev/null
RUN pipenv install --system --ignore-pipfile --deploy

EXPOSE 8000

CMD ["uvicorn", "server:app", "--host", "0.0.0.0", "--port", "8000"]
