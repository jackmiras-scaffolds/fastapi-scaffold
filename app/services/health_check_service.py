from configs import aws
from configs.cache import cache
from configs.env import env
from psycopg.pq import PGconn, Ping


class HealthCheckService:
    async def health_data(self):
        return {
            "is_cache_connection_ok": await self.is_cache_connection_ok(),
            "is_database_connection_ok": await self.is_database_connection_ok(),
            "is_file_storage_ok": await self.is_file_storage_ok(),
            "is_secret_manager_ok": await self.is_scret_manager_ok(),
        }

    async def is_cache_connection_ok(self):
        return cache.ping()

    async def is_database_connection_ok(self):
        dsn = (
            "postgresql://"
            + env("DB_USERNAME", "postgres")
            + ":"
            + env("DB_PASSWORD", "")
            + "@"
            + env("DB_HOST", "localhost")
            + "/"
            + env("DB_DATABASE")
        )

        status = PGconn.ping(conninfo=dsn.encode())

        return status == Ping.OK

    async def is_file_storage_ok(self):
        return aws.s3.buckets.all() is not None

    async def is_scret_manager_ok(self):
        return aws.secrets_manager.list_secrets() is not None
