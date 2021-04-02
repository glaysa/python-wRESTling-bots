class User:
    _USER_ID = 1

    def __init__(self, username):
        self.id = self.__class__._USER_ID
        self.__class__._USER_ID += 1
        self.username = username

    def __str__(self):
        return f"{{\n" \
               f"\t\"id\" : \"{self.id}\",\n" \
               f"\t\"username\" : \"{self.username}\"\n" \
               f"}}"
