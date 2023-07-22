from abc import ABC, abstractmethod
from typing import Dict, NoReturn


class ApplicationException(ABC, Exception):
    @abstractmethod
    def status_code(self) -> int:
        pass

    @abstractmethod
    def log_message(self) -> NoReturn:
        pass

    @abstractmethod
    def detail(self) -> Dict:
        pass
