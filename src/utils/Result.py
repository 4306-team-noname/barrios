from typing import TypedDict
from typing import Optional

class Result(TypedDict):
    ok: bool
    value: Optional[any]
    error: Optional[any]