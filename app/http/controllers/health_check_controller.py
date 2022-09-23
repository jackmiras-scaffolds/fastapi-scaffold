from fastapi import Response, status
from app.services.health_check_service import HealthCheckService


class HealthCheckController:
    def __init__(self):
        self.health_check_service = HealthCheckService()

    async def health_check(self, response: Response):
        is_live = await self.health_check_service.is_live()
        is_ready = await self.health_check_service.is_ready()

        if is_live and is_ready:
            return {"status": "It's health!!!"}

        response.status_code = status.HTTP_417_EXPECTATION_FAILED
        return {"status": "It's NOT health!!!"}

    async def live(self, response: Response):
        if await self.health_check_service.is_live():
            return {"status": "It's live!!!"}

        response.status_code = status.HTTP_417_EXPECTATION_FAILED
        return {"status": "It's NOT live!!!"}

    async def ready(self, response: Response):

        if await self.health_check_service.is_ready():
            return {"status": "It's ready!!!"}

        response.status_code = status.HTTP_417_EXPECTATION_FAILED
        return {"status": "It's NOT ready!!!"}
