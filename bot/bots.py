from bot import responses
from data.models import Message, Content
from api_views import user1, user2, user3, user4
import random


def sweet(message=None):
    if message:
        return responses.choose_sweet_response(message)
    else:
        return Message(sender=user3, content=Content(message="Do you want to cook or go out for a coffee?"))


def energetic(action=None):
    if action:
        message = f"{action} sounds awesome!"
    else:
        message = "Wanna play?"
        action = "play"
    return Message(content=Content(message=message, action=action))


def annoying(action=None):
    if action:
        message = f"{action} sounds boring."
    else:
        message = "Let's sleep."
        action = "sleep"
    return Message(content=Content(message=message, action=action))


def grumpy(action=None):
    if action:
        message = f"{action} sounds lame."
    else:
        message = "I want to watch a movie."
        action = "watch"
    return Message(content=Content(message=message, action=action))
