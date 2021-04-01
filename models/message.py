class Message:
    def __init__(self, sender, content, timestamp):
        self.sender = sender
        self.content = content
        self.timestamp = timestamp

    def __str__(self):
        return f"{{\n" \
               f"\t\"sender\" : \"{self.sender}\",\n" \
               f"\t\"content\" : \"{self.content}\",\n" \
               f"\t\"timestamp\" : \"{self.timestamp}\"\n" \
               f"}}"
