from app.repositories.item_repository import ItemRepository


class ItemsController:
    async def show(self, aggregator_id):
        item_repository = ItemRepository()
        return await item_repository.find_by_aggregator_id_or_alias(aggregator_id)
