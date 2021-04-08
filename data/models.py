from dataclasses import dataclass, field
from uuid import uuid4


def get_id() -> str:
    return uuid4().hex[:5]


@dataclass()
class User:
    username: str
    personality: str
    usr_id: str = field(default_factory=get_id)


@dataclass()
class Chatroom:
    name: str
    users: list[str] = field(default=[])
    messages: list[str] = field(default=[])
    room_id: str = field(default_factory=get_id)


@dataclass()
class Content:
    message: str
    action: str


@dataclass()
class Message:
    sender: str
    content: Content
    msg_type: str = "CHAT"
    msg_id: str = field(default_factory=get_id)