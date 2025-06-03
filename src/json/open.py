import json
from typing import Any, Optional

from common.exception import UnknownError


def read_json_file(file_name: str) -> Optional[dict[str, Any]]:
    with open(file_name, "r") as file:
        data = json.load(file)

    if data:
        return data
    raise UnknownError(f"Couldnt open file {file_name}")
