from models.message import Message
from models.user import User
import json


class Chatroom:
    _ROOM_ID = 1

    def __init__(self, name, users=None, messages=None):
        if messages is None:
            messages = []
        if users is None:
            users = []

        self.id = self._ROOM_ID
        self.__class__._ROOM_ID += 1
        self.name = name
        self.users = users
        self.messages = messages

    def set_user(self, user: User):
        self.users.append(user)

    def set_message(self, message: Message):
        self.messages.append(message)

    @classmethod
    def json_to_room(cls, json_str):
        dictionary = json.loads(json_str)
        return cls(**dictionary)

    @staticmethod
    def to_dictionary(obj):
        usrs_dictionary = [User.to_dictionary(usr) for usr in obj.users]
        msgs_dictionary = [Message.to_dictionary(msg) for msg in obj.messages]
        return {
            'id': obj.id,
            'name': obj.name,
            'users': usrs_dictionary,
            'messages': msgs_dictionary
        }
