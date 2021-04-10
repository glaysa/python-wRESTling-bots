from flask import session, redirect, url_for, request
from flask_restful import Resource
from api_views import room_list
from dataclasses import asdict
from data.models import Content, Message


# Shows a list of users from a specific room
class RoomUserList(Resource):

    def get(self, room_id: str):
        for room in room_list:
            if room.room_id == room_id:
                return room.users
        return {"message": "Room not found"}, 404

    def post(self, room_id: str):
        for room in room_list:
            if room.room_id == room_id:
                user = session['user']
                room.users.append(user)
                return redirect(url_for('get_home'))
        return {"message": "Room not found"}, 404


# Shows a list of messages from a specific room
class RoomMessageList(Resource):

    def get(self, room_id: str):
        for room in room_list:
            if room.room_id == room_id:
                return room.messages
        return {"message": "Room not found"}, 404


# Shows a list of messages from a user in a specific room
class RoomUserMessageList(Resource):

    def get(self, room_id: int, user_id: int):
        current_room = None
        current_user = None
        message_list = []

        for room in room_list:
            if room.room_id == room_id:
                current_room = room
        if current_room is None:
            return {"message": "Room not found"}, 404

        for user in current_room.users:
            if user['usr_id'] == user_id:
                current_user = user
        if current_user is None:
            return {"message": "User not found"}, 404

        for msg in current_room.messages:
            if msg['sender'] == current_user:
                message_list.append(msg)

        return message_list

    def post(self, room_id: int, user_id: int):
        current_room = None
        current_user = None

        for room in room_list:
            if room.room_id == room_id:
                current_room = room
        if current_room is None:
            return {"message": "Room not found"}, 404

        for user in current_room.users:
            if user['usr_id'] == user_id:
                current_user = user
        if current_user is None:
            return {"message": "User not found"}, 404

        data = request.form['message']
        content = Content(message=data, action="play")
        message = Message(sender=current_user, content=content)
        current_room.messages.append(asdict(message))

        return redirect(url_for('get_room', room_id=current_room.room_id))

