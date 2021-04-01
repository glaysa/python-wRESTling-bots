from app import app
from flask import render_template


@app.route("/")
@app.route("/login")
def get_login():
    return render_template("login.html")


@app.route("/home")
def get_home():
    return render_template("home.html")


@app.route("/chatroom")
def get_room():
    return render_template("chatroom.html")
