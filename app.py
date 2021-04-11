from main import Books
import flask
import os
from flask import request
from flask_cors import CORS
from flask import jsonify as json

app = flask.Flask(__name__)
app_setting = os.getenv("APP_SETTINGS")
app.config.from_object(app_setting)
CORS(app)
app.config["DEBUG"] = True


@app.route("/", methods=["GET"])
def home():
    return json({"data": "This is the Home Page designed by Adarsh Srivastava. Follow Github www.github.com/adarshSrivastava01 for more."})

@app.route("/data", methods=["GET"])
def info():
    book = request.args.get("book")
    return json(Books(book).getBooks())

@app.route("/bye", methods=["GET"])
def bye():
    return json({"bye": 404})

@app.route("/signup", methods=["GET"])
def login():
    return "Hello"

if __name__ == "__main__":
    app.run()