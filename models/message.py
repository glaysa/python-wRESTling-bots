import json


class Message:
    _MSG_ID = 1

    def __init__(self, sender, content, timestamp=None, type=None):
        self.id = self._MSG_ID
        self.__class__._MSG_ID += 1
        self.sender = sender
        self.message = content['message']
        self.action = content['action']
        self.timestamp = timestamp
        self.type = type

    @classmethod
    def json_to_msg(cls, json_str):
        dictionary = json.loads(json_str)
        return cls(**dictionary)

    def __str__(self):
        return f"id : {self.id},\n" \
               f"sender : {self.sender},\n" \
               f"content: {{\n" \
               f"\tmessage: {self.message},\n" \
               f"\taction : {self.action},\n" \
               "},\n" \
               f"timestamp : {self.timestamp},\n" \
               f"type : {self.type},\n"

    def to_dictionary(self):
        return {
            'id': self.id,
            'sender': self.sender,
            'content': {
                'message': self.message,
                'action': self.action
            },
            'timestamp': self.timestamp,
            'type': self.type
        }


class Content:
    def __init__(self, message, action=None):
        self.message = message
        self.action = action
