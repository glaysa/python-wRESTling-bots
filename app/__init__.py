from flask import Flask
from flask_login import LoginManager
from flask_restful import Api
from flask_socketio import SocketIO

from api_views.user_resource import UserList, SingleUser
from api_views.room_resource import RoomList, SingleRoom
from api_views.room_object_resource import RoomUserList, RoomMessageList, RoomUserMessageList


app = Flask(__name__)
app.secret_key = '354b9b92b934613f14afe99c94a82415a9a3d49a'
api = Api(app)
login_manager = LoginManager()
login_manager.login_view = 'get_login'
# for the flash()
login_manager.login_message = "Login required to view this page"
login_manager.login_message_category = "warning"
login_manager.init_app(app)
socket = SocketIO(app)

# API endpoints
api.add_resource(UserList, "/api/users")
api.add_resource(RoomList, "/api/rooms")
api.add_resource(SingleUser, "/api/user/<string:user_id>")
api.add_resource(SingleRoom, "/api/room/<string:room_id>")
api.add_resource(RoomUserList, "/api/room/<string:room_id>/users")
api.add_resource(RoomMessageList, "/api/room/<string:room_id>/messages")
api.add_resource(RoomUserMessageList, "/api/room/<string:room_id>/<string:user_id>/messages")

from app import web_views, login, socket_views
