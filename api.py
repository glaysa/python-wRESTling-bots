from flask import Flask
from flask_restful import Api, Resource, abort

app = Flask(__name__)
api = Api(app)

users = {}
rooms = {}


def abort_if_obj_doesnt_exist(obj_id: int, obj_list: iter, abort_message: str):
    if obj_id not in obj_list:
        abort(404, message=abort_message)


def abort_if_obj_exist(obj_id: int, obj_list: iter, abort_message: str):
    if obj_id in obj_list:
        abort(409, message=abort_message)


# Shows a single user
class User(Resource):

    def get(self, user_id: int = None):
        pass

    def delete(self, user_id: int = None):
        pass


# Shows a single room
class Room(Resource):

    def get(self, room_id: int = None):
        pass

    def delete(self, room_id: int = None):
        pass


# Shows a list of users
class UserList(Resource):

    def get(self):
        pass

    def post(self):
        pass


# Shows a list of rooms
class RoomList(Resource):

    def get(self):
        pass

    def post(self):
        pass


# Shows a list of users from a specific room
class RoomUserList(Resource):

    def get(self, room_id: int):
        pass

    def post(self, room_id: int):
        pass


# Shows a list of messages from a specific room
class RoomMessageList(Resource):

    def get(self, room_id: int):
        pass


# Shows a list of messages from a user in a specific room
class RoomUserMessageList(Resource):

    def get(self, room_id: int, user_id: int):
        pass

    def post(self, room_id: int, user_id: int):
        pass


# API endpoints
api.add_resource(User, "/api/user/<int:user_id>")
api.add_resource(Room, "/api/room/<int:room_id>")
api.add_resource(UserList, "/api/users")
api.add_resource(RoomList, "/api/rooms")
api.add_resource(RoomUserList, "/api/room/<room_id:int>/users")
api.add_resource(RoomMessageList, "/api/room/<room_id:int>/messages")
api.add_resource(RoomUserMessageList, "/api/room/<room_id:int>/<user_id:int>/messages")


if __name__ == "__main__":
    app.run(debug=True)
