from typing import Dict
from fastapi import Response
from app.models.user import User

class UsersController:
    async def index(response: Response) -> Dict:
        return User().all()
