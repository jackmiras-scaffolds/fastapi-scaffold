import os

import boto3

"""
---------------------------------------------------------------------------
AWS session
--------------------------------------------------------------------------

Client session that manages state about a particular configuration/account.
Sessions typically store credentials, AWS regions, and other configurations
related to a given profile.

"""

session_args = {}

region_name = os.getenv("AWS_DEFAULT_REGION")
aws_access_key_id = os.getenv("AWS_ACCESS_KEY_ID")
aws_secret_access_key = os.getenv("AWS_SECRET_ACCESS_KEY")

if not region_name and not aws_access_key_id and not aws_secret_access_key:
    session_args = {
        "region_name": region_name,
        "aws_access_key_id": aws_access_key_id,
        "aws_secret_access_key": aws_secret_access_key,
    }

session = boto3.Session(**session_args)


"""
---------------------------------------------------------------------------
S3 Client
--------------------------------------------------------------------------

Amazon Simple Storage Service (Amazon S3) is an object storage service.

"""

s3 = session.resource("s3")


"""
---------------------------------------------------------------------------
Secrets Manager Client
--------------------------------------------------------------------------


AWS Secrets Manager is service to, retrieve, and rotate database credentials,
API keys, and other secrets throughout their lifecycles.

"""

secrets_manager = session.client("secretsmanager")
