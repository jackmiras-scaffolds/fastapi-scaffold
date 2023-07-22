from configs import authenticator

from app.specs.auth import Auth
from app.specs.token import Token


class AuthsController:
    async def signin(self, auth: Auth) -> Token:
        return Token(
            ttl=await authenticator.token_ttl(authenticator.TIME_IN_SECONDS),
            token=await authenticator.authenticate(auth.email, auth.password),
        )
