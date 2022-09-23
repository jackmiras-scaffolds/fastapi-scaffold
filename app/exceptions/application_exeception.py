from abc import ABC, abstractmethod


class ApplicationException(ABC, Exception):
    @abstractmethod
    def status_code(self) -> int:
        pass

    @abstractmethod
    def log_message(self) -> None:
        pass

    @abstractmethod
    def detail(self) -> str:
        pass
