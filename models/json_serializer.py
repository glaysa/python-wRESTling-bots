import json
from typing import Any

from models.chatroom import Chatroom
from models.message import Message
from models.user import User


class ModelEncoder(json.JSONEncoder):
    def default(self, o: Any) -> Any:
        if isinstance(o, User):
            return User.to_dictionary(o)
        elif isinstance(o, Message):
            return Message.to_dictionary(o)
        elif isinstance(o, Chatroom):
            return Chatroom.to_dictionary(o)
        else:
            super().default(o)
