import pymongo
import os

MONGODB_URI = os.getenv("MONGODB_URI")
DBS_NAME = 'game_of_thrones_characters'
COLLECTION_NAME = 'house'

def mongo_connect(url):
    try:
        conn = pymongo.MongoClient(url)
        print('Mongo is connected')
        return conn
    except pymongo.errors.ConnectionFailure as e:
        print('Could not connect: %s') % e
        
    
conn = mongo_connect(MONGODB_URI)

coll = conn[DBS_NAME][COLLECTION_NAME]

documents = coll.find()

for doc in documents:
    print (doc)
        