import json
import os
from base64 import b64decode

from botocore.exceptions import (ClientError, NoCredentialsError,
                                 ParamValidationError)

from configs import aws
from configs.logging import logger

"""
Retrieves the value of an env variable from a remote source or a .env file.

:type key: str
:type default_value: str
:return: str
"""


def env(key: str, default_value: str = ""):
    value = get_env(key, default_value)

    if value.lower() == "true":
        return True
    if value.lower() == "false":
        return False
    if value.lower() == "none":
        return None

    return value


"""
Retrieves env variable from .env and AWS Secrets Manager, giving precedence to
remote value. If both sources exist, the remote value is returned; otherwise,
.env value or default_value is used.

:type key: str
:type default_value: str
:return: str
"""


def get_env(key: str, default_value: str = "") -> str:
    local_value = str(os.getenv(key, default_value))
    remote_value = str(remote_environemnt_variable(key))
    return remote_value if remote_value else local_value


"""
Retrieves env variable from AWS Secrets Manager.

:type key: str
:return: str
"""


def remote_environemnt_variable(key: str) -> str:
    secret_id = os.getenv("AWS_SECRETS_MANAGER_SECRET_ID")

    if not secret_id:
        return ""

    try:
        response = aws.secrets_manager.get_secret_value(SecretId=secret_id)
    except (ClientError, NoCredentialsError, ParamValidationError) as error:
        if isinstance(error, (NoCredentialsError, ParamValidationError)):
            logger.debug("AWS Secrets Manager: %s", error)
        else:
            message = f"{error.response['Error']['Code']} to secret"
            logger.error(f"{message} {secret_id}: {error}")

        return ""

    if "SecretString" in response:
        secret_dictionary = json.loads(response["SecretString"])
    else:
        secret_dictionary = json.loads(b64decode(response["SecretBinary"]))

    return secret_dictionary.get(key)
