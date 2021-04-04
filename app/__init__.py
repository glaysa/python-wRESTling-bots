from flask import Flask, request, render_template, url_for
from flask_restful import Api

app = Flask(__name__)
api = Api(app)

from app import api_view as resource, web_views
