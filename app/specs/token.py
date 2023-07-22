from configs import authenticator
from pydantic import BaseModel, validator


class Token(BaseModel):
    ttl: int
    token: str

    @validator("token")
    def validate_token(cls, token):
        authenticator.decode(token)
        return token
