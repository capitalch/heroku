from flask import Flask

app = Flask(__name__)

@app.route("/heroku")
def hello_world():
    return "<p>Hello, World!</p>"