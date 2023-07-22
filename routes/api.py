from app.controllers.auths_controller import AuthsController
from app.controllers.health_check_controller import HealthCheckController
from app.controllers.users_controller import UsersController
from app.specs.auth import Auth
from app.specs.health_check import HealthCheck
from app.specs.token import Token
from app.specs.user import User
from configs.authenticator import authenticate
from fastapi import APIRouter, Depends, Request, Response, status

api = APIRouter()
health_check_controller = HealthCheckController()
auths_controller = AuthsController()
users_controller = UsersController()


@api.get("/health", status_code=status.HTTP_200_OK)
async def health_check() -> HealthCheck:
    return await health_check_controller.health_check()


@api.post("/signin", status_code=status.HTTP_200_OK)
async def auth(auth: Auth) -> Token:
    return await auths_controller.signin(auth)


@api.get("/users", status_code=status.HTTP_200_OK, dependencies=[Depends(authenticate)])
async def get_users(response: Response):
    return await users_controller.index()
