class Message:
    _MSG_ID = 1

    def __init__(self, sender, content, timestamp):
        self.id = self._MSG_ID
        self.__class__._MSG_ID += 1
        self.sender = sender
        self.content = content
        self.timestamp = timestamp

    def __str__(self):
        return f"{{\n" \
               f"\t\"id\" : \"{self.id}\",\n" \
               f"\t\"sender\" : \"{self.sender}\",\n" \
               f"\t\"content\" : \"{self.content}\",\n" \
               f"\t\"timestamp\" : \"{self.timestamp}\"\n" \
               f"}}"
