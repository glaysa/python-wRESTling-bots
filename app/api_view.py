from app import api
from flask_restful import Resource, abort
import dummy_data

users = dummy_data.users
rooms = dummy_data.rooms


def abort_if_obj_doesnt_exist(obj_id: int, obj_list: iter, abort_message: str):
    if obj_id not in obj_list:
        abort(404, message=abort_message)


def abort_if_obj_exist(obj_id: int, obj_list: iter, abort_message: str):
    if obj_id in obj_list:
        abort(409, message=abort_message)


# Shows a single user
class User(Resource):

    def get(self, user_id: int = None):
        abort_if_obj_doesnt_exist(user_id, users, "User not found")
        return users[user_id]

    def delete(self, user_id: int = None):
        abort_if_obj_doesnt_exist(user_id, users, "User not found")
        deleted_user = users.pop(user_id)
        return {"deleted user": deleted_user}


# Shows a single room
class Room(Resource):

    def get(self, room_id: int = None):
        abort_if_obj_doesnt_exist(room_id, rooms, "Room not found")
        return rooms[room_id]

    def delete(self, room_id: int = None):
        abort_if_obj_doesnt_exist(room_id, rooms, "Room not found")
        deleted_room = rooms.pop(room_id)
        return {"deleted room": deleted_room}


# Shows a list of users
class UserList(Resource):

    def get(self):
        return users

    def post(self):
        pass


# Shows a list of rooms
class RoomList(Resource):

    def get(self):
        return rooms

    def post(self):
        pass


# Shows a list of users from a specific room
class RoomUserList(Resource):

    def get(self, room_id: int):
        abort_if_obj_doesnt_exist(room_id, rooms, "Room not found")
        return rooms[room_id]["users"]

    def post(self, room_id: int):
        pass


# Shows a list of messages from a specific room
class RoomMessageList(Resource):

    def get(self, room_id: int):
        abort_if_obj_doesnt_exist(room_id, rooms, "Room not found")
        return rooms[room_id]["messages"]


# Shows a list of messages from a user in a specific room
class RoomUserMessageList(Resource):

    def get(self, room_id: int, user_id: int):
        abort_if_obj_doesnt_exist(room_id, rooms, "Room not found")
        abort_if_obj_doesnt_exist(user_id, users, "User not found")
        room_message_list = rooms[room_id]["messages"]
        room_user_list = rooms[room_id]["users"]
        abort_if_obj_doesnt_exist(user_id, room_user_list, "User is not a part of this room")
        for message in room_message_list:
            if message["sender"] == users[user_id]:
                return message
        return {"message": "This user has not sent a message to this room yet."}

    def post(self, room_id: int, user_id: int):
        pass


# API endpoints
api.add_resource(User, "/api/user/<int:user_id>")
api.add_resource(Room, "/api/room/<int:room_id>")
api.add_resource(UserList, "/api/users")
api.add_resource(RoomList, "/api/rooms")
api.add_resource(RoomUserList, "/api/room/<int:room_id>/users")
api.add_resource(RoomMessageList, "/api/room/<int:room_id>/messages")
api.add_resource(RoomUserMessageList, "/api/room/<int:room_id>/<int:user_id>/messages")

