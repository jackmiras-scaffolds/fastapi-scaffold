from app.http.controllers.health_check_controller import HealthCheckController
from app.http.controllers.items_controller import ItemsController
from fastapi import APIRouter, Response

api = APIRouter()

health_check_controller = HealthCheckController()


@api.get("/")
@api.get("/health-check", status_code=200)
async def health_check(response: Response):
    return await health_check_controller.health_check(response)


@api.get("/live", status_code=200)
async def live(response: Response):
    return await health_check_controller.live(response)


@api.get("/ready", status_code=200)
async def ready(response: Response):
    return await health_check_controller.ready(response)


@api.get("/items", status_code=200)
async def get_item(aggregator_id: str, response: Response):
    items_controller = ItemsController()
    return await items_controller.show(aggregator_id)
