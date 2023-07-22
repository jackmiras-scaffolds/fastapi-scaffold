from typing import List


class Error:
    def __init__(
        self, short_message: str = "", messages: List[str] = [], helps: List[str] = []
    ):
        self.short_message = short_message
        self.messages = messages
        self.helps = helps
