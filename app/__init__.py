from flask import Flask, request, render_template, url_for
from flask_restful import Api

app = Flask(__name__)
api = Api(app)

from app import api_view as resource, web_views

# API endpoints
api.add_resource(resource.User, "/api/user/<int:user_id>")
api.add_resource(resource.Room, "/api/room/<int:room_id>")
api.add_resource(resource.UserList, "/api/users")
api.add_resource(resource.RoomList, "/api/rooms")
api.add_resource(resource.RoomUserList, "/api/room/<int:room_id>/users")
api.add_resource(resource.RoomMessageList, "/api/room/<int:room_id>/messages")
api.add_resource(resource.RoomUserMessageList, "/api/room/<int:room_id>/<int:user_id>/messages")
