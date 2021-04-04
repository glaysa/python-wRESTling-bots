from app import api
from flask_restful import Resource, abort, reqparse
from dummy_data import users, rooms, messages

users = users
rooms = rooms


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

        # Data needed to create a user
        # (den skal slettes etter hvert fordi data skal kommer fra en form i nettsiden)

        user_args = reqparse.RequestParser()
        user_args.add_argument("name", type=str, required=True, help="Provide a name for the user")
        user_args.add_argument("personality", type=str, required=True, help="Provide the personality of the user")
        user_data = user_args.parse_args()

        # Add the new user to dict
        user_id = len(users) + 1
        new_user = {user_id: user_data}
        users.update(new_user)
        return {"new user": new_user}


# Shows a list of rooms
class RoomList(Resource):

    def get(self):
        return rooms

    def post(self):

        # Data needed to create a room (skal erstattes med data fra form)
        # (den skal slettes etter hvert fordi data skal kommer fra en form i nettsiden)

        room_args = reqparse.RequestParser()
        room_args.add_argument("name", type=str, required=True, help="Provide a room name")
        room_args.add_argument("creator", type=str, required=True, help="Provide the name of the room creator")
        room_args.add_argument("users", type=dict, default={})
        room_args.add_argument("messages", type=dict, default={})
        room_data = room_args.parse_args()

        # Add the new room to dict
        room_id = len(rooms) + 1
        new_room = {room_id: room_data}
        rooms.update(new_room)
        return {"new room": new_room}


# Shows a list of users from a specific room
class RoomUserList(Resource):

    def get(self, room_id: int):
        abort_if_obj_doesnt_exist(room_id, rooms, "Room not found")
        return rooms[room_id]["users"]

    def post(self, room_id: int):

        # Validate parameters
        abort_if_obj_doesnt_exist(room_id, rooms, "Room not found")

        # Data needed to store a user info in a room
        # (data for den skal ikke komme fra en form, men fra query params kanskje, skal slettes etter hvert)

        user_args = reqparse.RequestParser()
        user_args.add_argument("user_id", type=int, required=True, help="Provide the id of the user")
        user_data = user_args.parse_args()

        # List of users in a room
        room_users = rooms[room_id]["users"]

        # Check if the user id given exists
        abort_if_obj_doesnt_exist(user_data["user_id"], users, "User not found")

        # Check if the user is already a member of the chat room
        abort_if_obj_exist(user_data["user_id"], room_users, "User is already a member of this chat room")

        # Add the user to the room
        new_user = {user_data["user_id"]: users[user_data["user_id"]]}
        room_users.update(new_user)
        return {"User joined": new_user}


# Shows a list of messages from a specific room
class RoomMessageList(Resource):

    def get(self, room_id: int):
        abort_if_obj_doesnt_exist(room_id, rooms, "Room not found")
        return rooms[room_id]["messages"]


# Shows a list of messages from a user in a specific room
class RoomUserMessageList(Resource):

    def get(self, room_id: int, user_id: int):

        # Validate parameters
        abort_if_obj_doesnt_exist(room_id, rooms, "Room not found")
        abort_if_obj_doesnt_exist(user_id, users, "User not found")
        room_users = rooms[room_id]["users"]
        abort_if_obj_doesnt_exist(user_id, room_users, "User is not a part of this room")

        # Room data
        room_messages = rooms[room_id]["messages"]

        # Get the all the messages of one user in a room
        user_messages = filter(lambda message: message["sender"] == room_users[user_id], room_messages)
        return list(user_messages)

    def post(self, room_id: int, user_id: int):

        # Validate parameters
        abort_if_obj_doesnt_exist(room_id, rooms, "Room not found")
        abort_if_obj_doesnt_exist(user_id, users, "User not found")
        room_users = rooms[room_id]["users"]
        abort_if_obj_doesnt_exist(user_id, room_users, "User is not a part of this chatroom room")

        # Data needed to store a message in a room
        # (den skal slettes etter hvert fordi data skal kommer fra en form i nettsiden)

        message_args = reqparse.RequestParser()
        message_args.add_argument("message", type=str, required=True, help="Provide a message content")
        message_args.add_argument("actions", type=list, required=True, help="Provide a message actions")
        user_message = message_args.parse_args()

        # Add the new message to that particular room
        room_messages = rooms[room_id]["messages"]
        new_message = {"sender": users[user_id], "content": user_message}
        room_messages.append(new_message)
        return {"message": f"A new message has been added to {rooms[room_id]['name']}"}


# API endpoints
api.add_resource(User, "/api/user/<int:user_id>")
api.add_resource(Room, "/api/room/<int:room_id>")
api.add_resource(UserList, "/api/users")
api.add_resource(RoomList, "/api/rooms")
api.add_resource(RoomUserList, "/api/room/<int:room_id>/users")
api.add_resource(RoomMessageList, "/api/room/<int:room_id>/messages")
api.add_resource(RoomUserMessageList, "/api/room/<int:room_id>/<int:user_id>/messages")