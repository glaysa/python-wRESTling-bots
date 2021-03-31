from flask import Flask
from flask_restful import Api
from resources.resource_users import UsersResource

app = Flask(__name__)
api = Api(app)

api.add_resource(UsersResource, "/api/users/", "/api/users/<int:user_id>")

if __name__ == "__main__":
    app.run(debug=True)
