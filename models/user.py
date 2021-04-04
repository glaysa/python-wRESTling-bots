import json
class User:
    _USER_ID = 1

    def __init__(self, username, personality):
        self.id = self.__class__._USER_ID
        self.__class__._USER_ID += 1
        self.username = username
        self.personality = personality

    @classmethod
    def json_to_room(cls, json_str):
        dictionary = json.loads(json_str)
        return cls(**dictionary)

    def __str__(self):
        return f"id: {self.id}, username: {self.username}, personality: {self.personality}"

    def to_dictionary(self):
        return {
            'id': self.id,
            'username': self.username,
            'personaity': self.personality
        }