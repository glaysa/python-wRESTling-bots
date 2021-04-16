import re


def room_name_validation(name: str):
    if name is None or len(name.strip()) == 0:
        return "No room name given. Please give your room a name!"
    return None


def name_validation(name: str):
    if re.match("^[A-ZÆÅØ][a-zåæø]{3,10}", name):
        return None
    if name is None:
        return "No input is given, please write the input fields!"
    else:
        return f"The name is not valid. It should contain between 3 to 10 characters beginning " \
               f"with a capital one and followed with small ones."


def password_validation(password: str):
    if len(password) < 3:
        return f"The password must be at least 4 characters!"
    else:
        return None


def select_validation(selected: str):
    if len(selected) == 0:
        return "You should choose a room_type for creating a room"
    else:
        return None
