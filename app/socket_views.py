from dataclasses import asdict
from flask_socketio import join_room

from app import socket
from api_views import room_list
from bot.assign_bot import assign_bot
from data.dict2obj import dict2User
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
    last_sender = None
    prev_msg = None
    if len(current_room.messages) > 0:
        index = len(current_room.messages) - 1
        prev_msg = current_room.messages[index]
        last_sender = prev_msg.sender

    if user_type == "BOT":
        sender.personality = data['personality']
        sender.user_type = user_type
        bot = assign_bot(personality=sender.personality)
        prev_content = prev_msg.content.message if prev_msg else None
        message = bot(prev_content)
    else:
        message = Message(sender=sender, content=Content(message=data['msg']))
        data['ok'] = "DIN TUR"

    if last_sender is None or last_sender.user_id != sender.user_id:
        data['message'] = asdict(message)
        current_room.messages.append(message)
        socket.emit('receive_message', data, to=current_room.room_id)


# helper:
def get_room(room_id: str) -> Chatroom:
    for room in room_list:
        if room.room_id == room_id:
            return room
