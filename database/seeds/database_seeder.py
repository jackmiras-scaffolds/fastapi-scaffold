from database.seeds.items_aliases_table_seeder import ItemAliasesTableSeeder
from database.seeds.items_table_seeder import ItemTableSeeder


class DatabaseSeeder:
    async def execute(self):
        await ItemTableSeeder().execute()
        await ItemAliasesTableSeeder().execute()
