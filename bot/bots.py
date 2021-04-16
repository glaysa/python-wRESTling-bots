from bot import responses
from data.models import Message, Content
from api_views import user1, user2, user3, user4


def sweet(message=None) -> Message:
    if message:
        return responses.choose_sweet_response(message)
    else:
        return Message(sender=user3, content=Content(message="Do you want to cook together?"))


def energetic(message=None) -> Message:
    if message:
        return responses.choose_energetic_response(message)
    else:
        return Message(sender=user4, content=Content(message="Let's party guys! My treat!"))


def annoying(message=None) -> Message:
    if message:
        return responses.choose_annoying_response(message)
    else:
        return Message(sender=user2, content=Content(message="It's time to steal something. You guys in?"))


def grumpy(message=None) -> Message:
    if message:
        return responses.choose_grumpy_response(message)
    else:
        return Message(sender=user1, content=Content(message="Let's sleep at my house. You coming or what?"))
