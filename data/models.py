from dataclasses import dataclass, field
from typing import List
from uuid import uuid4


def get_id() -> str:
    return uuid4().hex[:5]


@dataclass()
class User:
    username: str
    password: str = field(default=None)
    user_type: str = field(default="HUMAN")
    personality: str = field(default=None)
    user_id: str = field(default_factory=get_id)

    def check_password(self, password):
        return password == self.password

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
class Content:
    message: str


@dataclass()
class Message:
    content: Content
    sender: User = field(default=None)
    msg_type: str = field(default="CHAT")
    msg_id: str = field(default_factory=get_id)


@dataclass()
class Chatroom:
    name: str
    creator: User
    room_id: str = field(default_factory=get_id)
    users: List[User] = field(default_factory=List)
    messages: List[Message] = field(default_factory=list)


