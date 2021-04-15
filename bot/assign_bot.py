from bot.bots import sweet, energetic, annoying, grumpy


def assign_bot(personality):
    if personality == 'sweet':
        user_bot = sweet
    elif personality == 'energetic':
        user_bot = energetic
    elif personality == 'annoying':
        user_bot = annoying
    else:
        user_bot = grumpy
    return user_bot
