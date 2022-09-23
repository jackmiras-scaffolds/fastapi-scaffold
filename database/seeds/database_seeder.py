from database.seeds.items_table_seeder import ItemTableSeeder
from database.seeds.items_alias_table_seeder import ItemAliasTableSeeder


class DatabaseSeeder:
    async def execute(self):
        await ItemTableSeeder().execute()
        await ItemAliasTableSeeder().execute()
