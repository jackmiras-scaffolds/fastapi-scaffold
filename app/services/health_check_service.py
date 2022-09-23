class HealthCheckService:
    async def is_live(self):
        # TODO: [Thu Mar 31 18:03:30 2022] API call to the other app
        return False

    async def is_ready(self):
        return (
            await self.is_cache_connection_ok()
            and await self.is_database_connection_ok()
            and await self.is_azure_storage_service_ok()
        )

    async def is_cache_connection_ok(self):
        # TODO: [Thu Mar 31 10:07:14 2022] Run a search against the Cache
        return True

    async def is_database_connection_ok(self):
        # TODO: [Thu Mar 31 10:06:57 2022] Run a query against the DB
        return True

    async def is_azure_storage_service_ok(self):
        # TODO: [Thu Mar 31 10:07:30 2022] Retrieve a dummy file from storage
        return True
