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


def select_validation(selected: str):
    if selected:
        return None
    else:
        return f"Please select a personality for your bot!"
