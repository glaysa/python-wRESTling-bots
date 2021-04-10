from flask import request, redirect, url_for, render_template, session, flash
from flask_restful import Resource
from api_views import user_list
from dataclasses import asdict
from data.models import User


# Shows a single user
class SingleUser(Resource):

    def get(self, user_id: str):
        for user in user_list:
            if user.usr_id == user_id:
                return asdict(user)
        return {"message": "User not found"}, 404

    # Deletes a user
    def post(self, user_id: str):
        for user in user_list:
            if user.usr_id == user_id:
                user_list.remove(user)
                flash(f"The user '{user.username}' has been deleted")
                return redirect(url_for('get_register'))
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

            flash(f"User '{user.username}' has been successfully registered!")
            return redirect(url_for('get_login'))

        flash("Registration failed, please try again!")
        return render_template('register.html')
