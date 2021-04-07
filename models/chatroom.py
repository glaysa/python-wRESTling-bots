from models.message import Message
from models.user import User
import json


class Chatroom:
    _ROOM_ID = 1

    def __init__(self, name, users=None, messages=None):
        if messages is None:
            messages: list[int] = list
        if users is None:
            users: list[int] = list

        self.room_id = self._ROOM_ID
        self.__class__._ROOM_ID += 1
        self.name = name
        self.users = users
        self.messages = messages

    def set_user(self, user: int):
        self.users.append(user)

    def set_message(self, message: int):
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
            'room_id': obj.room_id,
            'name': obj.name,
            'users': usrs_dictionary,
            'messages': msgs_dictionary
        }
