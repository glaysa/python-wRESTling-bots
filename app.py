from flask import Flask, request, render_template, url_for


app = Flask(__name__)

@app.route("/")
@app.route("/login")
def get_login():
    return render_template("login.html")


@app.route("/home")
def get_home():
    return render_template("home.html")


if __name__ == "__main__":
    app.run(debug=False)
