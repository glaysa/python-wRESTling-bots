from app import app
from flask import render_template
from validation.form_validations import EnterAppForm, CreateRoomForm

app.config['SECRET_KEY'] = '354b9b92b934613f14afe99c94a82415a9a3d49a'  # Not Necessary


@app.route("/")
@app.route("/login")
def get_login_page():
    return render_template("login.html", msg="Username not found in our users list")


@app.route("/register")
def get_register():
    return render_template("register.html",msg="will send a message here from the /api/users (post)")


@app.route("/home")
def get_home():
    # msg = request.args.get('msg')
    return render_template("home.html")


@app.route("/chatroom")
def get_room():
    return render_template("chatroom.html")
