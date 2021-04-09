from flask_restful import Resource


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

