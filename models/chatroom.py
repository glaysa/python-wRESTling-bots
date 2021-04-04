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

    def __str__(self):
        return f"id: {self.id},\n" \
               f"name: {self.name},\n" \
               f"users: {self.users},\n" \
               f"messages: {self.messages}"

    # not working
    def to_dictionary(self):
        usrs_dictionary = [usr.to_dictionary() for usr in self.users]
        msgs_dictionary = [msg.to_dictionary() for msg in self.messages]
        return {
            'id': self.id,
            'name': self.name,
            'users': usrs_dictionary,
            'messages': msgs_dictionary
        }
