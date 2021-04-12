from pymongo import MongoClient
from bson.objectid import ObjectId
import urllib

def AddBook(id, name, desc, image):
    
    username = urllib.parse.quote_plus('adarsh')
    password = urllib.parse.quote_plus('adarsh123')

    URI = f'mongodb+srv://{username}:{password}@cluster0.dsmi2.mongodb.net/adarsh?retryWrites=true&w=majority'

    client = MongoClient(URI)

    db = client.adarsh
    userCollection = db.user

    userExists = userCollection.find_one({"_id": ObjectId(id)})

    if not userExists:
        return {"message": "User doesn't exist, try again later.", "status_code": 404}

    userExists["books"].append({
        "name": name,
        "desc": desc,
        "image": image
    })

    r = userCollection.insert_one(userExists)

    print(r)