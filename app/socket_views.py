from app import socket, app
from flask_socketio import join_room


@socket.on('join_room')
def handle_join_room_event(data):
    print(f"{data['username']} joined {data['room_name']}")
    join_room(data['room_id'])
    socket.emit('user_joined', data)
