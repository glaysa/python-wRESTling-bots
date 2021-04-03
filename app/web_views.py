from app import app
from flask import render_template
from validation.form_validations import EnterAppForm, CreateRoomForm

app.config['SECRET_KEY'] = '354b9b92b934613f14afe99c94a82415a9a3d49a'  # Not Necessary


@app.route("/", methods=['GET', 'POST'])
def get_login():
    form = EnterAppForm()
    return render_template("login.html", form=form)


@app.route("/home", methods=['GET', 'POST'])
def get_home():
    form = CreateRoomForm()
    return render_template("home.html", form=form)


@app.route("/chatroom", methods=['GET', 'POST'])
def get_room():
    return render_template("chatroom.html")
