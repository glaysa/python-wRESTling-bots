from flask import Flask, request, render_template, url_for

app = Flask(__name__)

from app import web_views