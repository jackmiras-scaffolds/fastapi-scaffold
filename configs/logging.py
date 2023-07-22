import logging
import os

"""
---------------------------------------------------------------------------
 Application Logger
--------------------------------------------------------------------------

This is the definition of the application logger that gets used when writing
messages to the log. It's also possible to set the following log levels
CRITICAL, ERROR, WARNING, INFO, DEBUG and NOTSET.

"""

logger = logging.getLogger("fastapi")
logger.addHandler(logging.StreamHandler())


"""
---------------------------------------------------------------------------
 Application Logger Severity
--------------------------------------------------------------------------

Accepetd log levels are CRITICAL, ERROR, WARNING, INFO, DEBUG and NOTSET.

"""

LOG_LEVELS = [
    "CRITICAL",
    "FATAL",
    "ERROR",
    "WARNING",
    "WARN",
    "INFO",
    "DEBUG",
    "NOTSET",
]

LOG_LEVEL = os.getenv("APP_LOG_LEVEL", "INFO")

if LOG_LEVEL not in LOG_LEVELS:
    raise Exception(f"LogError: Log level '{LOG_LEVEL}' not defined")

logger.setLevel(getattr(logging, LOG_LEVEL))
