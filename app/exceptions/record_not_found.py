from typing import Dict, NoReturn

from configs.constants import Constants
from fastapi.logger import logger

from app.exceptions.application_exception import ApplicationException
from app.models.error import Error


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

    def detail(self) -> Dict:
        return Error(
            short_message=self.__class__.__name__,
            messages=[f"{self.model} with {self.column} {self.value} not found"],
            help=["Check your searching parameter and try again"],
        ).__dict__
