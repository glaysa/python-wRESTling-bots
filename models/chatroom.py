class Chatroom:
    def __init__(self, name):
        self.name = name
        self.users = []

    def set_user(self, user):
        self.users.append(user)
