FROM python:3-alpine

WORKDIR /app
ENV PYTHONPATH=/app
ENV SQLALCHEMY_TRACK_MODIFICATIONS=False

# Installing some basics
RUN apk add --no-cache curl build-base
RUN pip install --upgrade pip
RUN pip install --no-cache SQLAlchemy

# Installing bash
RUN apk add bash
RUN sed -i 's/bin\/ash/bin\/bash/g' /etc/passwd

# Installing uvcorn
RUN pip install --no-cache uvicorn uvloop

# Installing PostgreSQL
RUN apk add --no-cache postgresql-dev python3-dev musl-dev
RUN pip install --no-cache psycopg2

# Copy pudb config
RUN mkdir -p /root/.config/pudb
RUN ln -sf /app/pudb.cfg /root/.config/pudb/pudb.cfg

# Project setup
COPY . .
RUN find . -type d -name __pycache__ -exec rm -r {} \+ 2>/dev/null
RUN pip install -r requirements.txt

CMD ["uvicorn", "server:app", "--host", "0.0.0.0", "--port", "8000"]
