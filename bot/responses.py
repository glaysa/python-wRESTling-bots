import random

from api_views import user3, user1, user2, user4
from data.models import Message, Content

positive_replies = ['sure', 'okay', 'fine', 'yes']
negative_replies = ['no', 'nope', 'nah', 'busy']
farewell_replies = ['bye', 'see yah', 'next time', 'goodbye', 'farewell']


def choose_sweet_response(message: str) -> Message:
    if 'cook' in message.lower() or any(reply in message for reply in positive_replies):
        return random.choice(sweet_responses['positive'])
    elif any(reply in message for reply in farewell_replies):
        return random.choice(sweet_responses['farewell'])
    else:
        return random.choice(sweet_responses['negative'])


def choose_energetic_response(message: str) -> Message:
    if 'party' in message.lower() or any(reply in message for reply in positive_replies):
        return random.choice(energetic_responses['positive'])
    elif any(reply in message for reply in farewell_replies):
        return random.choice(energetic_responses['farewell'])
    else:
        return random.choice(energetic_responses['negative'])


def choose_annoying_response(message: str) -> Message:
    if 'steal' in message.lower() or any(reply in message for reply in positive_replies):
        return random.choice(annoying_responses['positive'])
    elif any(reply in message for reply in farewell_replies):
        return random.choice(annoying_responses['farewell'])
    else:
        return random.choice(annoying_responses['negative'])


def choose_grumpy_response(message: str) -> Message:
    if 'sleep' in message.lower() or any(reply in message for reply in positive_replies):
        return random.choice(grumpy_responses['positive'])
    elif any(reply in message for reply in farewell_replies):
        return random.choice(grumpy_responses['farewell'])
    else:
        return random.choice(grumpy_responses['negative'])

sweet_responses = {
    'positive': [
        Message(sender=user3, content=Content(message="Cooking with you is so much fun!")),
        Message(sender=user3, content=Content(message="Let's start cooking right away.")),
        Message(sender=user3, content=Content(message="I can't wait to cook you favorite food!.")),
    ],
    'negative': [
        Message(sender=user3, content=Content(message="Whatever. Then I will cook alone.")),
        Message(sender=user3, content=Content(message="I will cook with the others then.")),
        Message(sender=user3, content=Content(message="You will starve without me.")),
    ],
    'farewell': [
        Message(sender=user3, content=Content(message="Okay. Bye. We're gonna cook next time.")),
        Message(sender=user3, content=Content(message="See you around! Farewell!")),
        Message(sender=user3, content=Content(message="I'm out. Bye!")),
    ],
}

energetic_responses = {
    'positive': [
        Message(sender=user4, content=Content(message="The more the merrier.")),
        Message(sender=user4, content=Content(message="Let's party until we drop!")),
        Message(sender=user4, content=Content(message="Partying is a cure. Let's go people!")),
    ],
    'negative': [
        Message(sender=user4, content=Content(message="Fine. I can party with the others.")),
        Message(sender=user4, content=Content(message="I thought we were friends! Come on!")),
        Message(sender=user4, content=Content(message="Won't you at least think about it? Boring people."))
    ],
    'farewell': [
        Message(sender=user4, content=Content(message="See yah guys!")),
        Message(sender=user4, content=Content(message="Let's meet up later. Bye!")),
        Message(sender=user4, content=Content(message="Goodbye forever my boring friends!"))
    ],
}

grumpy_responses = {
    'positive': [
        Message(sender=user1, content=Content(message="I like people who respects my sleeping hours.")),
        Message(sender=user1, content=Content(message="Sleeping is fun with the right people.")),
        Message(sender=user1, content=Content(message="Sleeping is good for the body after all"))],
    'negative': [
        Message(sender=user1, content=Content(message="If I had to choose, I would choose sleeping before you.")),
        Message(sender=user1, content=Content(message="Sleeping is peaceful without you anyway.")),
        Message(sender=user1, content=Content(message="Well, sleeping is not for everybody!"))],
    'farewell': [
        Message(sender=user1, content=Content(message="There won't be a next time.")),
        Message(sender=user1, content=Content(message="Forget I even asked!")),
        Message(sender=user1, content=Content(message="See yah!"))]
}
annoying_responses = {
    'positive': [
        Message(sender=user2, content=Content(message="Nice that you get my drift.")),
        Message(sender=user2, content=Content(message="You're making the right decision.")),
        Message(sender=user2, content=Content(message="Cool! I'm looking forward to it."))],
    'negative': [
        Message(sender=user2, content=Content(message="I'm not forcing you.")),
        Message(sender=user2, content=Content(message="I guess stealing is not everybody's favorite activity.")),
        Message(sender=user2, content=Content(message="Don't mention this to anyone. That the least you could do."))],
    'farewell': [
        Message(sender=user2, content=Content(message="I need brave people anyway. Goodbye!")),
        Message(sender=user2, content=Content(message="I will never invite you next time. Bye!")),
        Message(sender=user2, content=Content(message="Continue you boring life. Bye!"))]
}
