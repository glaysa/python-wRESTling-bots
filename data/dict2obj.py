from data.models import User, Message, Content


def dict2User(dct):
    username = dct['username']
    personality = dct['personality']
    user_id = dct['user_id']
    return User(username=username, personality=personality, user_id=user_id)


def dict2Msg(dct):
    sender = dict2User(dct['sender'])
    content = dict2Content(dct['content'])
    msg_type = dct['msg_type']
    msg_id = dct['msg_id']
    return Message(sender=sender, content=content,
                   msg_type=msg_type, msg_id=msg_id)


def dict2Content(dct: dict) -> Content:
    msg = dct['message']
    return Content(message=msg)
