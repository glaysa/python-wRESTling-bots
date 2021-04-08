import json
from data.models import User, Message, Content, Chatroom


def json2Msg(jsn: str) -> Message:
    dct = json.loads(jsn)
    sender = dct['sender']
    content = dict2Content(dct['content'])
    msg_type = dct['msg_type']
    msg_id = dct['msg_id']
    return Message(sender=sender, content=content,
                   msg_type=msg_type, msg_id=msg_id)


def dict2Content(dct: dict) -> Content:
    msg = dct['message']
    act = dct['action']
    return Content(message=msg, action=act)


def json2Chatroom(jsn: str) -> Chatroom:
    dct = json.loads(jsn)
    name = dct['name']
    users = dct['users']
    messages = dct['messages']
    room_id = dct['room_id']
    return Chatroom(name=name, users=users,
                    messages=messages, room_id=room_id)


def json2User(jsn: str) -> User:
    dct = json.loads(jsn)
    username = dct['username']
    personality = dct['personality']
    usr_id = dct['usr_id']
    return User(username=username, personality=personality,
                usr_id=usr_id)
