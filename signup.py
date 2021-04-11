from pymongo import MongoClient
import urllib

username = urllib.parse.quote_plus('adarsh')
password = urllib.parse.quote_plus('adarsh123')

URI = f'mongodb+srv://{username}:{password}@cluster0.dsmi2.mongodb.net/adarsh?retryWrites=true&w=majority'

client = MongoClient(URI)

db = client.adarsh
userCollection = db.user

def signup(name, email, password):
    pass

# userData = {
#     "name": "Hello",
#     "password": 1234,
#     "email": "adarshsrivastava.tech@gmail.com"
# }

# response = userCollection.insert_one(userData)

# print(response.inserted_id)