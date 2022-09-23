from sqlalchemy.sql.expression import func

from app.exceptions.record_not_found import RecordNotFound
from app.models.sqlalchemy.item_alias import ItemAlias
from app.repositories.base_repository import BaseRepository, db


class ItemAliasRepository(BaseRepository):
    async def find_by_aggregator_id(self, aggregator_id: str) -> ItemAlias:
        item_alias = (
            db.query(self.model)
            .filter(self.model.alias_aggregator_id == aggregator_id)
            .first()
        )
        if not item_alias:
            raise RecordNotFound("ItemAlias", "aggregator_id", aggregator_id)
        return item_alias

    async def random_item(self) -> ItemAlias:
        item_alias = (
            db.query(self.model)
            .order_by(func.random())  # for PostgreSQL and SQLite
            .first()
        )
        if not item_alias:
            raise RecordNotFound("Random ItemAlias")

        return item_alias
