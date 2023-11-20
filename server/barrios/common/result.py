from typing import Any, Optional, TypedDict


class Result(TypedDict):
    ok: bool
    value: Optional[Any]
    error: Optional[str]
