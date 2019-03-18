import pymongo
import os
from flask import Flask, redirect, request, url_for, render_template
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)


"""
Connects to database
"""

app.config["MONGODB_NAME"] = 'game_of_thrones_characters'
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")

mongo = PyMongo(app)


#Prints all characters to Python console

# def mongo_connect(url):
#     try:
#         conn = pymongo.MongoClient(url)
#         print('Mongo is connected')
#         return conn
#     except pymongo.errors.ConnectionFailure as e:
#         print('Could not connect to MongoDB: %s') % e
        
# conn = mongo_connect(MONGODB_URI)

# coll = conn[DBS_NAME][COLLECTION_NAME]

# documents = coll.find()

# for doc in documents:
#     print(doc)


"""
Returns all characters to Flask app
"""

@app.route('/')
@app.route('/get_all_characters')
def hello():
    return render_template('all_characters.html', character=mongo.db.character.find().sort('name'))
    
    

    


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
