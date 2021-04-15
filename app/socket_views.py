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
    current_room = get_room(data['room_id'])
    if user_type == "BOT":
        sender.personality = data['personality']
        sender.user_type = user_type
        bot = assign_bot(personality=sender.personality)
        if len(current_room.messages) > 0:
            prev_msg = current_room.messages[1].content.message
        else:
            prev_msg = None
        message = bot(prev_msg)
        print("30 : ", type(message))

    else:
        message = Message(sender=sender, content=Content(message=data['msg']))
        print("34 : ", type(message))
        data['ok'] = "DIN TUR"

    data['message'] = asdict(message)
    current_room.messages.append(message)
    socket.emit('receive_message', data)


# helper:
def get_room(room_id: str) -> Chatroom:
    for room in room_list:
        if room.room_id == room_id:
            return room




