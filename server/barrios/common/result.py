from typing import TypedDict
from typing import Any


class Result(TypedDict):
    ok: bool
    value: Any
    error: str
