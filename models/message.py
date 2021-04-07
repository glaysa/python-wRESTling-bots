import json


class Message:
    _MSG_ID = 1

    def __init__(self, sender, content, timestamp=None, msg_type=None):
        self.msg_id = self._MSG_ID
        self.__class__._MSG_ID += 1
        self.sender = sender
        self.content = content
        self.timestamp = timestamp
        self.msg_type = msg_type

    @classmethod
    def json_to_msg(cls, json_str):
        dictionary = json.loads(json_str)
        return cls(**dictionary)

    @staticmethod
    def to_dictionary(obj):
        return {
            'msg_id': obj.room_id,
            'sender': obj.sender,
            'content': Content.to_dictionary(obj.content),
            'timestamp': obj.timestamp,
            'type': obj.msg_type
        }


class Content:
    def __init__(self, message, action=None):
        self.message = message
        self.action = action

    @staticmethod
    def to_dictionary(obj):
        return {
            'message': obj.message,
            'action': obj.action
        }
