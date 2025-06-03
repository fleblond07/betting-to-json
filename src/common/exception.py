from typing import Optional


class UnknownError(Exception):
    def __init__(self, message: Optional[str]):
        if message:
            self.message = message
        else:
            self.message = "Unknown error occured"
