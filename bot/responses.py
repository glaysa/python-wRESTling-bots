import random

from api_views import user3
from data.models import Message, Content


def choose_sweet_response(message: str) -> Message:
    if 'cook' in message.lower():
        return random.choice(sweet_responses['positive'])
    elif 'bye' in message.lower() or 'farewell' in message.lower():
        return random.choice(sweet_responses['farewell'])
    else:
        return random.choice(sweet_responses['negative'])


def choose_energetic_response(message: str) -> Message:
    if 'party' in message.lower():
        return random.choice(sweet_responses['positive'])
    elif 'bye' in message.lower() or 'farewell' in message.lower():
        return random.choice(sweet_responses['farewell'])
    else:
        return random.choice(sweet_responses['negative'])


def choose_annoying_response(message: str) -> Message:
    if 'chill' in message.lower():
        return random.choice(sweet_responses['positive'])
    elif 'bye' in message.lower() or 'farewell' in message.lower():
        return random.choice(sweet_responses['farewell'])
    else:
        return random.choice(sweet_responses['negative'])


def choose_grumpy_response(message: str) -> Message:
    if 'sleep' in message.lower():
        return random.choice(sweet_responses['positive'])
    elif 'bye' in message.lower() or 'farewell' in message.lower():
        return random.choice(sweet_responses['farewell'])
    else:
        return random.choice(sweet_responses['negative'])


sweet_responses = {
    'positive': [
        Message(sender=user3, content=Content(message="Yes")),
        Message(sender=user3, content=Content(message="OK"))
    ],
    'negative': [],
    'farewell': [],
}

energetic_responses = {
    'positive': [],
    'negative': [],
    'farewell': [],
}

grumpy_responses = {
    'positive': [],
    'negative': [],
    'farewell': []
}
annoying_responses = {
    'positive': [],
    'negative': [],
    'farewell': []
}
