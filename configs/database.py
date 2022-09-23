from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

from configs.env import env


"""
|--------------------------------------------------------------------------
| Database - SQLAlchemy session
|--------------------------------------------------------------------------
|
| Creating a database session.
|
"""

db = None

if env("DB_CONNECTION") == "pgsql":
    db_uri = (
        "postgresql://"
        + env("DB_USERNAME", "postgres")
        + ":"
        + env("DB_PASSWORD", "")
        + "@"
        + env("DB_HOST", "localhost")
        + "/"
        + env("DB_DATABASE")
    )

    engine = create_engine(db_uri, pool_pre_ping=True, pool_size=32, max_overflow=64)

    session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    db = scoped_session(session)


"""
|--------------------------------------------------------------------------
| Database - SQLAlchemy declarative base
|--------------------------------------------------------------------------
|
| Creating a declarative_base object.
|
"""


Base = declarative_base()
