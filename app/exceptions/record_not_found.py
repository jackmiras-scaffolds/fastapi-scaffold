from typing import NoReturn

from fastapi.logger import logger

from app.exceptions.application_exeception import ApplicationException
from app.helpers.constants import Constants
from app.models.pydantic.error import Error


class RecordNotFound(ApplicationException):
    def __init__(self, model: str, column: str, value: str) -> None:
        self.model = model
        self.value = value
        self.column = column

    def status_code(self) -> int:
        return Constants.HTTP_NOT_FOUND

    def log_message(self) -> NoReturn:
        message = f"{self.model} with {self.column} {self.value} not found"
        logger.exception(f"ERROR:    RecordNotFound ==> {message}")

    def detail(self) -> str:
        error = Error(
            short_message="record_not_found",
            message=f"{self.model} with {self.column} {self.value} not found",
            help="Check your searching parameter and try again",
        )

        return error.dict()
