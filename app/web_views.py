from app import app
from flask import render_template
from validation.form_validations import EnterAppForm, CreateRoomForm

app.config['SECRET_KEY'] = '354b9b92b934613f14afe99c94a82415a9a3d49a'  # Not Necessary


@app.route("/register")
def get_login():
    return render_template("register.html")


@app.route("/")
@app.route("/home")
def get_home():
    return render_template("home.html",)


'''
@app.route("/chatroom")
def get_room():
    return render_template("chatroom.html")
'''