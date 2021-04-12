
def assign_bot(personality):
    if personality == 'sweet':
        user_bot = bot_1
    elif personality == 'energetic':
        user_bot = bot_2
    elif personality == 'annoying':
        user_bot = bot_3
    else:
        user_bot = bot_4

    return user_bot


def bot_1(actions, first: bool):
    if first:
        return "Wanna cook?"
    else:
        return f"{actions} sounds fun!"


def bot_2(actions, first: bool):
    if first:
        return "Wanna play?"
    else:
        return f"{actions} sounds awesome!"


def bot_3(actions, first: bool):
    if first:
        return "Let's sleep."
    else:
        return f"{actions} sounds boring."


def bot_4(actions, first: bool):
    if first:
        return "I want to watch a movie."
    else:
        return f"{actions} sounds lame."