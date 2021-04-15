import random

from api_views import user3
from data.models import Message, Content


def choose_sweet_response(message: str):
    if 'cook' in message.lower():
        random.choice(sweet_responses['positive'])
    else:
        random.choice(sweet_responses['negative'])


def choose_energetic_response(message: str):
    if 'party' in message.lower():
        random.choice(sweet_responses['positive'])
    else:
        random.choice(sweet_responses['negative'])


def choose_annoying_response(message: str):
    if 'chill' in message.lower():
        random.choice(sweet_responses['positive'])
    else:
        random.choice(sweet_responses['negative'])


def choose_grumpy_response(message: str):
    if 'sleep' in message.lower():
        random.choice(sweet_responses['positive'])
    else:
        random.choice(sweet_responses['negative'])


sweet_responses = {
    'positive': [Message(sender=user3, content=Content(message="Yes"))],
    'negative': []
}


energetic_responses = {
    'positive': [],
    'negative': []
}

grumpy_responses = {
    'positive': [],
    'negative': []
}
annoying_responses = {
    'positive': [],
    'negative': []
}
