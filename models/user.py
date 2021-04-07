
class User:

    _USER_ID = 1

    def __init__(self, username, personality):
        self.usr_id = self.__class__._USER_ID
        self.__class__._USER_ID += 1
        self.username = username
        self.personality = personality

    @classmethod
    def json_to_user(cls, username, personality):
        # dictionary = json.loads(json_str)
        # return cls(**dictionary)
        user = cls(username, personality)
        return User.to_dictionary(user)

    @staticmethod
    def to_dictionary(obj):
        return {
            "user_id": obj.usr_id,
            "username": obj.username,
            "personality": obj.personality
        }
