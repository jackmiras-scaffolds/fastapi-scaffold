from datetime import datetime

from app.models.item_aliases import ItemAliases


class ItemAliasesTableSeeder:
    async def execute(self):
        await ItemAliases(
            id=31,
            item_aggregator_id="1042777",
            alias_aggregator_id="1679485",
            created_at=datetime.now(),
            updated_at=datetime.now(),
            deleted_at=None,
        ).save()
