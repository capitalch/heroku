from flask import Flask
from postgres import getFromHerokuPostgres
app = Flask(__name__)

@app.route("/heroku")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/db")
def resolve_db():
    ret = getFromHerokuPostgres()
    return ret