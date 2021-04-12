from pymongo import MongoClient
import urllib
from flask import jsonify as json

def Login(email, pwd):

    username = urllib.parse.quote_plus('adarsh')
    password = urllib.parse.quote_plus('adarsh123')

    URI = f'mongodb+srv://{username}:{password}@cluster0.dsmi2.mongodb.net/adarsh?retryWrites=true&w=majority'

    client = MongoClient(URI)

    db = client.adarsh
    userCollection = db.user

    userExists = userCollection.find_one({"email": email})

    if not userExists:
        return {"message": "User doesn't exist, try again later.", "status_code": 404}

    if userExists["password"] != pwd:
        return {"message": "Invalid Credentials!!", "status_code": 401}

    return {"id": str(userExists["_id"]), "name": userExists["name"]}