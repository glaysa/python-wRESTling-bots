from bot.bots import bot_1, bot_2, bot_3, bot_4


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
