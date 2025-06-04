from typing import Optional


class UnknownError(Exception):
    def __init__(self, message: Optional[str]):
        if message is not None:
            self.message = message
        else:
            self.message = "Unknown error occurred"
