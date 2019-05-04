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
    return render_template('regions_pages/north.html',
                            the_north=mongo.db.region.find({'region_name':'The North'}),
                            characters = list(mongo.db.character.find()))

@app.route('/vale')
def vale():
    return render_template('regions_pages/vale.html',
                            the_vale=mongo.db.region.find({'region_name':'The Vale'}),
                            characters = list(mongo.db.character.find()))

@app.route('/riverlands')
def riverlands():
    return render_template('regions_pages/riverlands.html',
                            the_riverlands=mongo.db.region.find({'region_name':'The Riverlands'}),
                            characters = list(mongo.db.character.find()))

@app.route('/westerlands')
def westerlands():
    return render_template('regions_pages/westerlands.html',
                            the_westerlands=mongo.db.region.find({'region_name':'The Westerlands'}),
                            characters = list(mongo.db.character.find()))

@app.route('/iron_islands')
def iron_islands():
    return render_template('regions_pages/iron_islands.html',
                            the_iron_islands=mongo.db.region.find({'region_name':'The Iron Islands'}),
                            characters = list(mongo.db.character.find()))

@app.route('/crownlands')
def crownlands():
    return render_template('regions_pages/crownlands.html',
                            the_crownlands=mongo.db.region.find({'region_name':'The Crownlands'}),
                            characters = list(mongo.db.character.find()))


@app.route('/dorne')
def dorne():
    return render_template('regions_pages/dorne.html',
                            dorne=mongo.db.region.find({'region_name':'Dorne'}),
                            characters = list(mongo.db.character.find()))

@app.route('/reach')
def reach():
    return render_template('regions_pages/reach.html',
                            the_reach=mongo.db.region.find({'region_name':'The Reach'}),
                            characters = list(mongo.db.character.find()))

@app.route('/stormlands')
def stormlands():
    return render_template('regions_pages/stormlands.html',
                            the_stormlands=mongo.db.region.find({'region_name':'The Stormlands'}),
                            characters = list(mongo.db.character.find()))
                            




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
                            the_north=mongo.db.region.find({'region_name':'The North'}).sort('name'),
                            the_riverlands=mongo.db.region.find({'region_name':'The Riverlands'}).sort('name'),
                            the_vale=mongo.db.region.find({'region_name':'The Vale'}).sort('name'),
                            the_westerlands=mongo.db.region.find({'region_name':'The Westerlands'}).sort('name'),
                            the_iron_islands=mongo.db.region.find({'region_name':'The Iron Islands'}).sort('name'),
                            the_crownlands=mongo.db.region.find({'region_name':'The Crownlands'}).sort('name'),
                            the_stormlands=mongo.db.region.find({'region_name':'The Stormlands'}).sort('name'),
                            the_reach=mongo.db.region.find({'region_name':'The Reach'}).sort('name'),
                            dorne=mongo.db.region.find({'region_name':'Dorne'}).sort('name'),
                            character=mongo.db.character.find().sort('name'),)

    
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
                            the_north=mongo.db.region.find({'region_name':'The North'}).sort('name'),
                            the_riverlands=mongo.db.region.find({'region_name':'The Riverlands'}).sort('name'),
                            the_vale=mongo.db.region.find({'region_name':'The Vale'}).sort('name'),
                            the_westerlands=mongo.db.region.find({'region_name':'The Westerlands'}).sort('name'),
                            the_iron_islands=mongo.db.region.find({'region_name':'The Iron Islands'}).sort('name'),
                            the_crownlands=mongo.db.region.find({'region_name':'The Crownlands'}).sort('name'),
                            the_stormlands=mongo.db.region.find({'region_name':'The Stormlands'}).sort('name'),
                            the_reach=mongo.db.region.find({'region_name':'The Reach'}).sort('name'),
                            dorne=mongo.db.region.find({'region_name':'Dorne'}).sort('name'),)
                            
@app.route('/update_character/<character_id>', methods=["POST"])
def update_character(character_id):
    character = mongo.db.character
    character.update({'_id': ObjectId(character_id)},
    {
        'name':request.form.get('name'),
        'description':request.form.get('description'),
        'house_name':request.form.get('house_name'),
    })
    print(request.form.get('house_name'))
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



if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
