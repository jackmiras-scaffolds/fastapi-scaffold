from app.services.health_check_service import HealthCheckService
from app.specs.health_check import HealthCheck


class HealthCheckController:
    def __init__(self):
        self.health_check_service = HealthCheckService()

    async def health_check(self) -> HealthCheck:
        health_data = await self.health_check_service.health_data()
        return HealthCheck(**health_data)
