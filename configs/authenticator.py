from datetime import datetime, timedelta
from typing import Dict

import jwt
from fastapi import HTTPException, status

from configs.env import env

ALGORITHM = "HS512"
TOKEN_TTL_MINUTES = 60
SECRET_KEY = env("APP_KEY")

TIME_IN_SECONDS = "time_in_seconds"
TIME_IN_MINUTES = "time_in_minutes"


async def authenticate(username: str, password: str) -> bytes:
    if not SECRET_KEY:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid environment variable APP_KEY",
        )

    payload = {
        "exp": datetime.utcnow() + timedelta(minutes=TOKEN_TTL_MINUTES),
        "sub": username + password,
    }

    return jwt.encode(payload=payload, key=SECRET_KEY, algorithm=ALGORITHM)


def decode(token: str) -> Dict:
    try:
        payload = jwt.decode(jwt=token, key=SECRET_KEY, algorithms=[ALGORITHM])

        if payload is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid authentication credentials",
            )
    except jwt.ExpiredSignatureError as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=f"Token has expired: {str(e)}",
        )
    except jwt.DecodeError as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=f"Error decoding token: {str(e)}",
        )

    return payload


async def token_ttl(time_is: str = TIME_IN_MINUTES) -> int:
    if time_is == TIME_IN_MINUTES:
        return TOKEN_TTL_MINUTES

    if time_is == TIME_IN_SECONDS:
        return TOKEN_TTL_MINUTES * 60

    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail=f"Token TTL convertion to '{time_is}' not supported.",
    )
