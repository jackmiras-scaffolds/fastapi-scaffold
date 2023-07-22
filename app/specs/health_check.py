from pydantic import BaseModel, Field


class HealthCheck(BaseModel):
    is_cache_connection_ok: bool = Field(
        True,
        const=True,
        title="Cache connection failed.",
        description="Check your cache credentials and your cache client definition at configs/cache.py and try again.",
    )
    is_database_connection_ok: bool = Field(
        True,
        const=True,
        title="Database connection failed",
        description="Check your database credentials and your database client definition at configs/database.py and try again",
    )
    is_file_storage_ok: bool = Field(
        True,
        const=True,
        title="S3 connection failed",
        description="Check your AWS credentials and storage definition at configs/aws.py and try again",
    )
    is_secret_manager_ok: bool = Field(
        True,
        const=True,
        title="AWS Secrets Manager connection failed",
        description="Check your AWS credentials and secrets manager definition at configs/aws.py and try again",
    )
