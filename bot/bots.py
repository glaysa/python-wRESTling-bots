from data.models import Message, Content


def bot_1(action=None):
    if action:
        message = f"{action} sounds fun!"
    else:
        message = "Wanna cook?"
        action = "cook"
    return Message(content=Content(message=message, action=action))


def bot_2(action=None):
    if action:
        message = f"{action} sounds awesome!"
    else:
        message = "Wanna play?"
        action = "play"
    return Message(content=Content(message=message, action=action))


def bot_3(action=None):
    if action:
        message = f"{action} sounds boring."
    else:
        message = "Let's sleep."
        action = "sleep"
    return Message(content=Content(message=message, action=action))


def bot_4(action=None):
    if action:
        message = f"{action} sounds lame."
    else:
        message = "I want to watch a movie."
        action = "watch"
    return Message(content=Content(message=message, action=action))
