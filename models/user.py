class User:
    def __init__(self, username):
        self.username = username

    def __str__(self):
        return f"{{\n" \
            f"\t\"username\" : \"{self.username}\"\n"\
            f"}}"
