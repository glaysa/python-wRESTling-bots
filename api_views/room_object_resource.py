from flask import session, redirect, url_for
from flask_restful import Resource
from api_views import room_list
from data.json_serializer import asdict


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
        pass

    def post(self, room_id: int, user_id: int):
        pass

