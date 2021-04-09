from app import app
from flask import render_template, request, session, redirect, url_for, get_flashed_messages
from api_views import room_list
from validation.form_validations import EnterAppForm, CreateRoomForm

app.config['SECRET_KEY'] = '354b9b92b934613f14afe99c94a82415a9a3d49a'  # Not Necessary


def flash_message(custom_msg: str):
    msg = get_flashed_messages()
    if len(msg) > 0:
        return msg.__getitem__(0)
    else:
        return custom_msg


@app.route("/")
@app.route("/login")
def get_login_page():
    return render_template("login.html", msg="Username not found in our users list")


@app.route("/register")
def get_register():
    msg = flash_message("You must be a registered user to use the web app")
    return render_template("register.html", msg=msg)


@app.route("/home")
def get_home():
    if 'user_id' in session:
        user = session['user']
        msg = flash_message('')
        return render_template("home.html", user=user, rooms=room_list, msg=msg)
    return render_template("login.html")


@app.route("/profile")
def get_profile_page():
    if 'user' in session:
        user = session['user']
        return render_template("profile.html", user=user)
    return render_template("register.html")


@app.route("/chatroom")      # for now we should use the route below.
@app.route("/chatroom/<room_id>")
def get_room():
    return render_template("chatroom.html")


@app.route("/logout")
def logout():
    session.pop('user')
    return redirect(url_for('get_login_page'))
