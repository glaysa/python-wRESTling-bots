from flask_login import login_user, login_required, logout_user, current_user
from flask import render_template, request, redirect, url_for, session, flash

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
    if 'user' not in session:
        user = request.args.get('user')

    return render_template("home.html", rooms=room_list, user=user)


@app.route("/profile")
@login_required
def get_profile_page():
    user = current_user
    if 'user' not in session:
        return redirect(url_for('get_login'))

    return render_template("profile.html", user=user)


@app.route("/chatroom")  # for now we should use the route below.
@app.route("/chatroom/<room_id>")
@login_required
def get_room(room_id):
    active_room = None
    active_user = session['user']

    for room in room_list:
        if room.room_id == room_id:
            active_room = room
    return render_template(f"chatroom.html", room=active_room, user=active_user)


@app.route("/", methods=['GET', 'POST'])
@app.route("/login", methods=['GET', 'POST'])
def get_login():
    if 'user' in session:
        the_current_user = session['user']
        return render_template('home.html', user=the_current_user, rooms=room_list)

    if request.method == "POST":
        username = request.form.get('username')
        user = get_user(username)
        if user and user.check_username(username):
            login_user(user)
            session['user'] = user
            # flash() Not needed
            return render_template('home.html', user=user, rooms=room_list)
        flash(message="Wrong username, please try again or create a new user", category="warning")

    return render_template('login.html')


@app.route("/logout")
@login_required
def logout():
    logout_user()
    session.pop('user', None)
    return redirect(url_for('get_login'))
