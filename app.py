import pymongo
import os
from flask import Flask, redirect, request, url_for, render_template
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)


"""
Connects to database in Mongo DB Atlas
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
Displays home/main page of the web app
"""
@app.route('/')
def home_page():
    return render_template('home_page.html')



"""ALL BELOW FUNCTIONS RELATING TO CHARACTERS"""


"""
Returns all characters to Flask app/Displays all of the characters in the DB
"""

@app.route('/get_all_characters')
def get_all_characters():
    return render_template('all_characters.html', character=mongo.db.character.find().sort('name'))
    
    
"""
Function for adding a character to the database, then returns user to get_all_characters function page
"""
@app.route('/add_character')
def add_character():
    return render_template('add_character.html',
                            house_name=mongo.db.house.find(),
                            region_name=mongo.db.region.find())
    
    
@app.route('/insert_character', methods=["POST"])
def insert_character():
    character = mongo.db.character
    character.insert_one(request.form.to_dict())
    return redirect(url_for('get_all_characters'))


"""
Edits character info, then returns user to get_all_characters function page
"""
    
@app.route('/edit_character/<character_id>')
def edit_character(character_id):
    character = mongo.db.character.find_one({"_id": ObjectId(character_id)})
    return render_template('edit_character.html', character=character,
                            house_name=mongo.db.house.find(), 
                            region_name=mongo.db.region.find())
                            
@app.route('/update_character/<character_id>', methods=["POST"])
def update_character(character_id):
    character = mongo.db.character
    character.update({'_id': ObjectId(character_id)},
    {
        'name':request.form.get('name'),
        'description':request.form.get('description'),
        'region_name':request.form.get('region_name'),
        'house_name':request.form.get('house_name'),
        'episodes':request.form.get('episodes'),
        'deceased':request.form.get('deceased')
    })
    return redirect(url_for('get_all_characters'))
    
    
    
"""
Function for deleting an entire character's info/entry and returning to all_characters page
"""

@app.route('/delete_character/<character_id>')
def delete_character(character_id):
    mongo.db.character.remove({'_id': ObjectId(character_id)})
    return redirect(url_for('get_all_characters'))
    



"""ALL FUNCTIONS BELOW RELATING TO HOUSES"""


"""
Function for retrieving and displaying all Houses
"""
@app.route('/get_houses')
def get_houses():
    return render_template('houses.html',
                            house=mongo.db.house.find())


"""
Function for editing a House
"""
@app.route('/edit_house/<house_id>')
def edit_house(house_id):
    return render_template('edit_house.html',
                            house=mongo.db.house.find_one({'_id': ObjectId(house_id)}))









if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
