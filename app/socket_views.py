from dataclasses import asdict
from flask_socketio import join_room

from app import socket
from api_views import room_list
from bot.assign_bot import assign_bot
from data.models import Chatroom, User, Message, Content


@socket.on('join_room')
def handle_join_room_event(data):
    join_room(data['room_id'])
    socket.emit('user_joined', data)


@socket.on('send_message')
def handle_send_message_event(data):
    sender = User(username=data['username'], user_id=data['user_id'])
    user_type = data['user_type']
    if user_type == "BOT":
        sender.personality = data['personality']
        sender.user_type = user_type
        bot = assign_bot(personality=sender.personality)
        message = bot()
    else:
        message = Message(sender=sender, content=Content(message=data['msg']))

    data['message'] = asdict(message)
    current_room = get_room(data['room_id'])
    current_room.messages.append(message)

    socket.emit('receive_message', data)


# helper:
def get_room(room_id: str) -> Chatroom:
    for room in room_list:
        if room.room_id == room_id:
            return room




"""
 bot = assign_bot(data['personality'])
    sender = User(username=data['username'], personality=data['personality'], user_id=data['user_id'])
    the_current_room = get_room(data['room_id'])
    last_sender = None
    if len(the_current_room.messages) > 0:
        last_sender = the_current_room.messages[len(the_current_room.messages) - 1].sender
        action = the_current_room.messages[0].content.action
        message = bot(action)
        message.sender = sender
        data['message'] = asdict(message)
    else:
        message = bot(None)
        message.sender = sender
        dct_msg = asdict(message)
        data['message'] = dct_msg

    if last_sender != sender or last_sender is None:
        the_current_room.messages.append(message)  # the post method
        socket.emit('receive_message', data, room=data['room_id'])


"""