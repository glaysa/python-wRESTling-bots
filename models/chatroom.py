class Chatroom:
    _ROOM_ID = 1

    def __init__(self, name):
        self.id = self._ROOM_ID
        self.__class__._ROOM_ID += 1
        self.name = name
        self.users = []

    def set_user(self, user):
        self.users.append(user)

    def __str__(self):
        return f"{{\n" \
               f"\t\"id\" : \"{self.id}\",\n" \
               f"\t\"name\" : \"{self.name}\",\n" \
               f"\t\"users\" : \"{self.users}\",\n" \
               f"}}"
