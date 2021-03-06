from main import Books
from signup import Signup
from login import Login
from getBooks import GetBooks
from addBook import AddBook

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


@app.route("/signup", methods=["POST"])
def signup():
    name = request.form['name']
    email = request.form['email']
    password = request.form['password']
    if len(name) < 3:
        return json({"message": "Name length too short", "status_code": 303})
    if '@' not in email or '.' not in email or len(email) < 9:
        return json({"message": "Email Invalid", "status_code": 303})
    if len(password) < 8:
        return json({"message": "Password too short.", "status_code": 303})
    return json({"data": Signup(name, email, password)})

@app.route("/login", methods=["POST"])
def login():
    email = request.form['email']
    password = request.form['password']
    return json({"data": Login(email, password)})

@app.route("/books", methods=["GET"])
def getBooks():
    Id = request.args.get("id")
    return json({"data": GetBooks(Id)})

@app.route("/addbook", methods=["PATCH"])
def addBook():
    Id = request.args.get("id")
    name = request.form["name"]
    desc = request.form["desc"]
    image = request.form["image"]
    return json({"data": AddBook(Id, name, desc, image)})

if __name__ == "__main__":
    app.run()
