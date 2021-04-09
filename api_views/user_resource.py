from flask import request, redirect, url_for, render_template, session
from flask_restful import Resource
from api_views import user_list
from data.json_serializer import asdict
from data.models import User


# Shows a single user
class SingleUser(Resource):

    def get(self, user_id: str):
        for user in user_list:
            if user.usr_id == user_id:
                return asdict(user)
        return {"message": "User not found"}, 404

    def delete(self, user_id: str):
        for user in user_list:
            if user.usr_id == user_id:
                user_list.remove(user)
                return redirect(url_for('get_register', msg=f"{user} is deleted"))
        return {"message": "User not found"}, 404


# Shows a list of users
class UserList(Resource):

    def get(self):
        return [asdict(user) for user in user_list]

    def post(self):
        if request.method == 'POST':
            username = request.form['username']
            personality = request.form['personality']
            user = User(username=username, personality=personality)
            user_list.append(user)
            status_msg = username
            session['user'] = user
            return redirect(url_for('get_home', msg=status_msg))

        status_msg = "Registration failed, please try again!"
        return render_template('register.html', msg=status_msg)
