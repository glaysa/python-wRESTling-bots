from flask_socketio import join_room

from app import socket, app
from api_views import room_list, user_list
from data.models import Chatroom, User, Message, Content


# TODO: those methods will handle the http requests in away: I will fix it later


@socket.on('join_room')
def handle_join_room_event(data):
    join_room(data['room_id'])
    socket.emit('user_joined', data)


@socket.on('send_message')
def handle_send_message_event(data):
    content = Content(message=data['message'])
    message = Message(sender=data['sender'], content=content)
    the_current_room = get_room(data['room_id'])
    the_current_room.messages.append(message.msg_id) # the post method
    socket.emit('receive_message', data, room=data['room_id'])


# helper:
def get_room(room_id: str) -> Chatroom:
    for room in room_list:
        if room.room_id == room_id:
            return room

'''
# helpers:
def get_user_by_id(user_id:str) -> User:
    pass


def get_room(room_id: str) -> Chatroom:
    for room in room_list:
        if room.room_id == room_id:
            return room


def is_user_in_room(user_id: str, room_id: str) -> bool:
    if user_id in get_room(room_id=room_id).users:
        return True
    return False


'''
