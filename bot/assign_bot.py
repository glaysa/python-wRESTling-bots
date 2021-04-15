from bots import *


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
