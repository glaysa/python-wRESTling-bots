import json
from typing import Any
from dataclasses import asdict
from data.models import Chatroom, User, Message


class ModelEncoder(json.JSONEncoder):
    def default(self, o: Any) -> Any:
        if isinstance(o, User):
            return asdict(o)
        elif isinstance(o, Message):
            return asdict(o)
        elif isinstance(o, Chatroom):
            return asdict(o)
        else:
            return super().default(o)
