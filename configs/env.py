import base64
import json
import os

import boto3
from botocore.exceptions import ClientError, NoCredentialsError
from fastapi.logger import logger


def env(env_name: str, default_value: str = ""):
    value = get_env(env_name, default_value)

    if value == "True" or value == "true":
        return True
    if value == "False" or value == "false":
        return False

    return value


def get_env(env_name: str, default_value: str = "") -> str:
    value = remote_environemnt_variables(env_name)

    if value:
        return value

    return os.getenv(env_name, default_value)


def remote_environemnt_variables(env_name: str) -> str:
    session = boto3.session.Session()
    env_group = "FASTAPI_ENVIRONMENT_VARIABLES"

    client = session.client(region_name="us-east-1", service_name="secretsmanager")

    try:
        get_secret_value_response = client.get_secret_value(SecretId=env_group)
    except (ClientError, NoCredentialsError) as error:
        if isinstance(error, NoCredentialsError):
            return ""
        if error.response["Error"]["Code"] == "DecryptionFailureerror":
            message = "DecryptionFailureerror to secret"
            logger.error(f"{message} {env_group}: {error}")
            return ""
        elif error.response["Error"]["Code"] == "InternalServiceErrorerror":
            message = "InternalServiceErrorerror to secret"
            logger.error(f"{message} {env_group}: {error}")
            return ""
        elif error.response["Error"]["Code"] == "InvalidParametererror":
            message = "InvalidParametererror to secret"
            logger.error(f"{message} {env_group}: {error}")
            return ""
        elif error.response["Error"]["Code"] == "InvalidRequesterror":
            message = "InvalidRequesterror to secret"
            logger.error(f"{message} {env_group}: {error}")
            return ""
        elif error.response["Error"]["Code"] == "ResourceNotFounderror":
            message = "ResourceNotFounderror to secret"
            logger.error(f"{message} {env_group}: {error}")
            return ""
    else:
        if "SecretString" in get_secret_value_response:
            secret_string = get_secret_value_response["SecretString"]
            secret_dictionary = json.loads(secret_string)
            return secret_dictionary.get(env_name)
        else:
            secret_value = get_secret_value_response["SecretBinary"]
            secret_decoded = base64.b64decode(secret_value)
            secret_dictionary = json.loads(secret_decoded)
            return secret_dictionary.get(env_name)
