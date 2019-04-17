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


"""
Displays home/main page of the web app
"""
@app.route('/')
def home_page():
    return render_template('home_page.html',
                            the_north=mongo.db.region.find({'region_name':'The North'}),
                            the_riverlands=mongo.db.region.find({'region_name':'The Riverlands'}),
                            the_vale=mongo.db.region.find({'region_name':'The Vale'}),
                            the_westerlands=mongo.db.region.find({'region_name':'The Westerlands'}),
                            the_iron_islands=mongo.db.region.find({'region_name':'The Iron Islands'}),
                            the_crownlands=mongo.db.region.find({'region_name':'The Crownlands'}),
                            the_stormlands=mongo.db.region.find({'region_name':'The Stormlands'}),
                            the_reach=mongo.db.region.find({'region_name':'The Reach'}),
                            dorne=mongo.db.region.find({'region_name':'Dorne'}),
                            tully=mongo.db.region.find({'Tully':'Edmure Tully'}),
                            characters = list(mongo.db.character.find())
                            )



"""
All .HTML pages for Regions
"""
@app.route('/north')
def north():
    return render_template('regions_pages/north.html')

@app.route('/vale')
def vale():
    return render_template('regions_pages/vale.html')

@app.route('/riverlands')
def riverlands():
    return render_template('regions_pages/riverlands.html')

@app.route('/westerlands')
def westerlands():
    return render_template('regions_pages/westerlands.html')

@app.route('/iron_islands')
def iron_islands():
    return render_template('regions_pages/iron_islands.html')

@app.route('/crownlands')
def crownlands():
    return render_template('regions_pages/crownlands.html')

@app.route('/dorne')
def dorne():
    return render_template('regions_pages/dorne.html')

@app.route('/reach')
def reach():
    return render_template('regions_pages/reach.html')

@app.route('/stormlands')
def stormlands():
    return render_template('regions_pages/stormlands.html')
                            




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

@app.route('/update_house/<house_id>', methods=['POST'])
def update_house(house_id):
    mongo.db.house.update(
        {'_id':ObjectId(house_id)},
        {'house_name': request.form.get('house_name')})
    return redirect(url_for('get_houses'))
    
"""
Function to Delete a house
"""

@app.route('/delete_house/<house_id>')
def delete_house(house_id):
    mongo.db.house.remove({'_id':ObjectId(house_id)})
    return redirect(url_for('get_houses'))


"""
Function for Adding a house
"""
@app.route('/insert_house', methods=["POST"])
def insert_house():
    house_doc={'house_name': request.form.get('house_name')}
    mongo.db.house.insert_one(house_doc)
    return redirect(url_for('get_houses'))
    
@app.route('/add_house')
def add_house():
    return render_template('add_house.html')






"""ALL FUNCTIONS BELOW RELATING TO REGIONS"""


"""
Function for retrieving and displaying all Regions
"""
@app.route('/get_regions')
def get_regions():
    return render_template('get_regions.html',
                            region=mongo.db.region.find())


"""
Function for editing a Region
"""
@app.route('/edit_region/<region_id>')
def edit_region(region_id):
    return render_template('edit_region.html',
                            region=mongo.db.region.find_one({'_id': ObjectId(region_id)}))

@app.route('/update_region/<region_id>', methods=['POST'])
def update_region(region_id):
    mongo.db.region.update(
        {'_id':ObjectId(region_id)},
        {'region_name': request.form.get('region_name')})
    return redirect(url_for('get_regions'))
    
"""
Function to Delete a Region
"""

@app.route('/delete_region/<region_id>')
def delete_region(region_id):
    mongo.db.region.remove({'_id':ObjectId(region_id)})
    return redirect(url_for('get_regions'))


"""
Function for Adding a Region
"""
@app.route('/insert_region', methods=["POST"])
def insert_region():
    region_doc={'region_name': request.form.get('region_name')}
    mongo.db.region.insert_one(region_doc)
    return redirect(url_for('get_regions'))
    
@app.route('/add_region')
def add_region():
    return render_template('add_region.html')







@app.route('/the_north/region_id')
def the_north(region_id):
    return render_template('the_north.html',
                            house_name=mongo.db.region.find_one({'_id': ObjectId(
                                                                '5c7bc9d11c9d440000b78303')}))





"""
ALL FUNCTIONS BELOW RELATING TO DEAD ALIVE CHARACTERS
"""

"""Function for returning all dead characters"""
@app.route('/deceased_characters')
def deceased_characters():
    return render_template('deceased_characters.html',
                            deceased=mongo.db.deceased.find().sort('name'),
                            characters = list(mongo.db.character.find()))
                            
"""Function for returning all alive characters"""
@app.route('/alive_characters')
def alive_characters():
    return render_template('alive_characters.html',
                            alive=mongo.db.deceased.find().sort('name'),
                            characters = list(mongo.db.character.find()))
                            






if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
