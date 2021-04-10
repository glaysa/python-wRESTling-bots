from flask_login import login_user, login_required, logout_user, current_user
from flask import render_template, request, redirect, url_for, session

from api_views.login import get_user
from app import app
from api_views import room_list


@app.route("/register")
def get_register():
    if 'user' in session:
        return redirect(url_for("get_home"))

    return render_template("register.html", msg="will send a message here from the /api/users (post)")


@app.route("/home")
@login_required
def get_home():
    user = current_user
    if not user:
        user = request.args.get('user')

    return render_template("home.html", rooms=room_list, user=user)


@app.route("/profile")
@login_required
def get_profile_page():
    return render_template("profile.html")


@app.route("/chatroom")  # for now we should use the route below.
@app.route("/chatroom/<room_id>")
@login_required
def get_room():
    return render_template("chatroom.html")


@app.route("/", methods=['GET', 'POST'])
@app.route("/login", methods=['GET', 'POST'])
def get_login():
    if 'user' in session:
        return redirect(url_for('get_home'))

    if request.method == "POST":
        username = request.form.get('username')
        user = get_user(username)
        if user and user.check_username(username):
            login_user(user)
            session['user'] = user
            # flash()
            return render_template('home.html', user=user, rooms=room_list)
    # flash()
    return render_template('login.html')


@app.route("/logout")
@login_required
def logout():
    logout_user()
    session.pop('user', None)
    return redirect(url_for('get_login'))
