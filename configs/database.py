from sqlalchemy import create_engine, event
from sqlalchemy.engine import Engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlite3 import Connection
from sqlalchemy.pool.base import _ConnectionRecord

from configs.constants import Constants
from configs.env import env

"""
---------------------------------------------------------------------------
MySQL Databases
--------------------------------------------------------------------------

MySQL is an open-source relational database management system. Its name is a
combination of "My", the name of co-founder Michael Widenius's daughter My, and
"SQL", the acronym for Structured Query Language. A relational database
organizes data into one or more data tables in which data may be related to
each other; these relations help structure the data.

"""

if env("DB_CONNECTION") == "mysql":
    pass


"""
---------------------------------------------------------------------------
PostgreSQL Databases
--------------------------------------------------------------------------

PostgreSQL, also known as Postgres, is a free and open-source relational
database management system emphasizing extensibility and SQL compliance. It was
originally named POSTGRES referring to its origins as a successor to the Ingres
database developed at the Berkeley University.

"""

if env("DB_CONNECTION") == "postgres":
    dsn = (
        "postgresql+psycopg://"
        + env("DB_USERNAME", "postgres")
        + ":"
        + env("DB_PASSWORD", "")
        + "@"
        + env("DB_HOST", "localhost")
        + "/"
        + env("DB_DATABASE")
    )

    engine = create_engine(
        url=dsn,
        pool_pre_ping=True,
        pool_size=32,
        max_overflow=64,
        execution_options={"isolation_level": "AUTOCOMMIT"},  # Not working
    )

    session = sessionmaker(autoflush=False, bind=engine)
    db = scoped_session(session)


"""
---------------------------------------------------------------------------
SQLite Databases
--------------------------------------------------------------------------

SQLite is a C-language library that implements a small, fast, self-contained,
high-reliability , full-featured , SQL database engine. It is not a standalone
app; rather, it is a library that software developers embed in their apps. As
such, it belongs to the family of embedded databases.

"""

if env("DB_CONNECTION") == "sqlite":
    dsn = f"sqlite+pysqlite:///{Constants.BASE_PATH}/database/database.sqlite"
    engine = create_engine(url=dsn)

    session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    db = scoped_session(session)


"""
---------------------------------------------------------------------------
Database Listeners
--------------------------------------------------------------------------

SQLAlchemy event listeners

"""


@event.listens_for(Engine, "connect")
def database_on_connect(connection: Connection, connection_record: _ConnectionRecord):

    if env("DB_CONNECTION") == "sqlite":
        cursor = connection.cursor()
        cursor.execute("PRAGMA foreign_keys=ON")  # Enforce foreign-key
        cursor.execute("PRAGMA synchronous=OFF")  # Let the OS manage syncing.
        cursor.execute("PRAGMA cache_size=10000")  # 10000 pages, or ~40MB
        cursor.execute("PRAGMA journal_mode=WAL")  # Write-Ahead Logging mode.
        cursor.close()
