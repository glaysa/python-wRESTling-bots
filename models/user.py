import json


class User:
    _USER_ID = 1

    def __init__(self, username, personality):
        self.id = self.__class__._USER_ID
        self.__class__._USER_ID += 1
        self.username = username
        self.personality = personality

    @classmethod
    def json_to_user(cls, json_str):
        dictionary = json.loads(json_str)
        return cls(**dictionary)

    @staticmethod
    def to_dictionary(obj):
        return {
            'id': obj.id,
            'username': obj.username,
            'personality': obj.personality
        }