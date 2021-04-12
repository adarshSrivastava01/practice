from pymongo import MongoClient
import urllib
from flask import jsonify as json
import bcrypt


def signup(name, email, password):

    username = urllib.parse.quote_plus('adarsh')
    password = urllib.parse.quote_plus('adarsh123')

    URI = f'mongodb+srv://{username}:{password}@cluster0.dsmi2.mongodb.net/adarsh?retryWrites=true&w=majority'

    client = MongoClient(URI)

    db = client.adarsh
    userCollection = db.user

    userExists = userCollection.find_one({"email": email})
    print("-----------")
    print(userExists)
    print("-----------")
    if userExists:
        return json({"message": "User with this email exists already!", "status_code": 301})

    # try:
    # print("Bcrypt Started")
    # hashedPassword = bcrypt.hashpw(password, bcrypt.gensalt(12))
    # print("Bcrypt Ended")
    # print(hashedPassword, type(hashedPassword))
    # except:
    #     return json({"message": "Encryption Failed!!", "status_code": 401})




    newUser = {
        "name": name,
        "email": email,
        "password": password
    }
    print(newUser)
    print("------", "Reached Here", "----------")
    try:
        response = userCollection.insert_one(newUser)
        print("----------", response, "---------")
        return {"id": str(response.inserted_id), "message": "User Created Succesfully.", "status_code": 200}
    except:
        return {"message": "Uploading to Database failed.", "status_code": 401}
