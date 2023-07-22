from datetime import datetime

from app.models.item import Item


class ItemTableSeeder:
    async def execute(self):
        await Item(
            id=1,
            name="Cerveja",
            price=9,
            inventory_id="40000010019",
            aggregator_id="1042777",
            item_type="BEBIDAS",
            subtype="",
            ncm="2203.00.00",
            created_at=datetime.now(),
            updated_at=datetime.now(),
            deleted_at=None,
        ).save()
