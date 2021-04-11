from dataclasses import dataclass, field
from uuid import uuid4


def get_id() -> str:
    return uuid4().hex[:5]


@dataclass()
class User:
    username: str
    personality: str
    user_id: str = field(default_factory=get_id)

    def check_username(self, username):
        return username == self.username

    def get_id(self):
        return self.username

    @staticmethod
    def is_active():
        return True

    @staticmethod
    def is_authenticated():
        return True

    @staticmethod
    def is_anonymous():
        return False


@dataclass()
class Chatroom:
    name: str
    creator: str
    room_id: str = field(default_factory=get_id)
    users: list[str] = field(default=list)
    messages: list[str] = field(default_factory=list)


@dataclass()
class Content:
    message: str
    action: str = field(default=None)


@dataclass()
class Message:
    sender: str
    content: Content
    msg_type: str = field(default="CHAT")
    msg_id: str = field(default_factory=get_id)
