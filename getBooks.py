from pymongo import MongoClient
from bson.objectid import ObjectId
import urllib

def GetBooks(id):
    
    username = urllib.parse.quote_plus('adarsh')
    password = urllib.parse.quote_plus('adarsh123')

    URI = f'mongodb+srv://{username}:{password}@cluster0.dsmi2.mongodb.net/adarsh?retryWrites=true&w=majority'

    client = MongoClient(URI)

    db = client.adarsh
    userCollection = db.user

    userExists = userCollection.find_one({"_id": ObjectId(id)})

    if not userExists:
        return {"message": "User doesn't exist, try again later.", "status_code": 404}

    return userExists["books"]