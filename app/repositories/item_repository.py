from sqlalchemy import or_
from sqlalchemy.sql.expression import func

from app.exceptions.record_not_found import RecordNotFound
from app.models.sqlalchemy.item import Item
from app.repositories.base_repository import BaseRepository, db
from app.repositories.item_alias_repository import ItemAliasRepository


class ItemRepository(BaseRepository):
    async def find_by_aggregator_id_or_alias(self, aggregator_id: str) -> Item:
        item = (
            db.query(self.model)
            .filter(
                or_(
                    self.model.inventory_id == aggregator_id,
                    self.model.aggregator_id == aggregator_id,
                )
            )
            .first()
        )
        if not item:
            repository = ItemAliasRepository()
            item = (await repository.find_by_aggregator_id(aggregator_id)).item
        if not item:
            raise RecordNotFound("Item", "aggregator_id", aggregator_id)
        return item

    async def random_item(self) -> Item:
        item = (
            db.query(self.model)
            .order_by(func.random())  # for PostgreSQL and SQLite
            .first()
        )
        if not item:
            repository = ItemAliasRepository()
            item = (await repository.random_item()).item
        if not item:
            raise RecordNotFound("Random Item")
        return item
