from flask_restful import Resource, reqparse
from resources import validate
from requests import get, post, put, delete

users = {}
rooms = {}
BASE = "http://127.0.0.1:5000/api"

users_post_args = reqparse.RequestParser()
users_post_args.add_argument("user_name", type=str, help="Missing argument: user_name", required=True)
users_post_args.add_argument("user_rooms", type=list, help="Missing argument: user_rooms")
users_post_args.add_argument("user_messages", type=dict, help="Missing argument: user_messages")

users_put_args = reqparse.RequestParser()
users_put_args.add_argument("user_name", type=str, help="Missing argument: user_name", store_missing=False)
users_put_args.add_argument("user_rooms", type=list, help="Missing argument: user_rooms", store_missing=False)
users_put_args.add_argument("user_messages", type=dict, help="Missing argument: user_messages", store_missing=False)


class UsersResource(Resource):

    def get(self, user_id: int = None):
        if user_id:
            validate.abort_if_not_exists(user_id, users, "User does not exist")
            return {user_id: users[user_id]}
        return users

    def put(self, user_id: int = None):
        validate.abort_if_not_exists(user_id, users, "User does not exist")
        args = users_put_args.parse_args()
        if "user_name" in args:
            users[user_id]["user_name"] = args["user_name"]
        if "user_rooms" in args:
            users[user_id]["user_rooms"] = args["user_rooms"]
        return {user_id: users[user_id]}

    def post(self):
        user_id = (len(users) - 1) + 1
        args = users_post_args.parse_args()
        added_user = {user_id: args}
        users.update(added_user)
        return added_user

    def delete(self, user_id: int = None):
        validate.abort_if_not_exists(user_id, users, "User does not exist")
        deleted_user = {user_id: users.pop(user_id)}
        return deleted_user


class Users:

    @staticmethod
    def get_all_users():
        url = BASE + "/users/"
        response = get(url)
        return response.json()

    @staticmethod
    def get_user(user_id: int):
        url = BASE + f"/users/{user_id}"
        response = get(url)
        return response.json()

    @staticmethod
    def add_user(user_name: str, user_rooms: list, user_messages: dict):
        url = BASE + "/users/"
        response = post(url, {"user_name": user_name, "user_rooms": user_rooms, "user_messages": user_messages})
        return response.json()

    @staticmethod
    def update_user(user_id: int, user_name: str, user_rooms: list, user_messages: dict):
        url = BASE + f"/users/{user_id}"
        response = put(url, {user_id: {"user_name": user_name, "user_rooms": user_rooms, "user_messages": user_messages}})
        return response.json()

    @staticmethod
    def delete_user(user_id: int):
        url = BASE + f"/users/{user_id}"
        response = delete(url)
        return response.json()
