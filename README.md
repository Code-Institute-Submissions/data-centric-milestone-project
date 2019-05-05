# Game of Thrones Characters

# Your Project's Name

This is my website used to display lists and categorised lists of chatracters from the TV series A Game of Thrones. Users can perform CRUD commands on the app and in essence take 'control' of the data. The data is stored and outputted from a database via MongoDB.

## UX
Use this section to provide insight into your UX process, focusing on who this website is for, what it is that they want to achieve and how your project is the best way to help them achieve these things.

### User Stories:
'As a Game of Thrones fan I would like to see a website that displays a list of all of the main and recurring characters as there are too many to remember by heart and I would like to remember all the names. I would like the list displayed alphabetically so it is easy to look through and digest' - users can find a list of all characters within the database on the app which displays all characters alphabetically.


'As a user I would like to be able to easily discern which character belongs to which house so that it is easier to understand who are allies and distant relatives' - The home page of the app provides the user with an accordion which breaks down houses within regions, and then characters within those houses.


* 'As a Game of Thrones fan I would like to see a website that displays a list of all of the main and recurring characters as there are too many to remember by heart and I would like to remeber names to faces. I would like the list displayed alphabetically so it is easy to look through and digest'



'As a user I would like a 'live' website that will allow myself and others to add character infomation to it as the show still has not finished. It would be great to add any new/old characters and any info that someone else adding character info may have missed for referencing purposes for myself' - users can perform CRUD commands on individual characters through the All Characters page. Once the user clicks on a character, they are given the option to edit and delete. Users can create a new characters by selecting the Add Character link at the top of the page.

'As a Game of Thrones fan I would like to remember which house is in what region. I'd like the ability to visually see which house is where to understand which houses are allies and which house rules which region' - Users can visually find the houses within their retrospective regions through the accordion on the home page.


* Mockups are found within the folder named 'mockups'


## Features

## Existing Features
The Add Characters and Edit character allow the user to add/edit a character by filling out the form on the page they're redirected to. This will input the data on the database, redirect the user back to the characters page, and display the new/edited character input. The Delete link will allow the user to delete the entire character entry from the database


## Features Left to Implement
Another feature I would like to add would be the ability to add an image for each character. I would also like the ability to add a feature that displays how many episodes the character is in, which season they first appear in, and how they die (if relevant).

I would also like to split the list of characters by providing a Dead and Alive page (each) so the user can easily discern which characters are still alive and which are dead.

I would like to add a feature that allows users to perform all CRUD commands on regions and houses.

Another feature left to implement is the ability to add the actor's details that play the character and create a link to their social media/wikipedia pages.

I would like to add a 'best bits' to the page that shows which scenes in the show the characters stood out the most.

I would like the ability to add a 'Characters by Season' category. This would allow users to select a Season and will display the characters that appear in that season.


### Technologies Used

1. HTML - used to create the base of the app. https://html.com/
2. CSS - used to design the app and manipulate Materialize's designs to suit my own creative mind. http://www.css3.info/
3. Python - used to create the functionality of the site. https://www.python.org/
4. Flask - used to connect front end and back end/jinja templating. http://flask.pocoo.org/
5. MongoDB - used to store the data for accessing in a database. https://www.mongodb.com/
6. Materialize - used for creating the accoridons and responsive design. https://materializecss.com/

## Testing
The first user story provides the user with their goal as the All Characters page displays a list of all characters in the database alphabetically. Each character also has a discription and house name associated to them. The character name, description and house name are all editable and can be inputted/created by user themselves. This will create and/or edit the character entry in the database and display them to screen in the All Characters page in alphabetical order.

The second user story is achieved by using an accordion to categorise the characters into their retrospective regions and houses. This works when the user selects the Regions accordion header, this will drop down a body of region names with another body beneath titles 'houses'. Once the user clicks on this it will drop another body down with the regions' house names and each house name will drop another body displaying the character name. This filtering allows the user to find which characters belong to which houses. If this worked in reverse order, the lists would be far too long and far less user friendly and straightforward; the filtering would become messy.

A user can perform CRUD commands on each existing and new character. The third user story is achieved by allowing the user to do this. The user is free to add a description and house name of their choice. This creates a lot more freedom for the user to manipulate the character entry; as all throughout the show characters' journeys often change. e.g the discovery of Jon Snow's real name - ultimately changing the House Name he belongs to. This makes the website 'live' as stated in the user story and provides them with the opportunity to add any missing/irrelevant data. This level of flexibility will allow the user to continue to achieve their goal.

The fourth user story is achieved through the use of the accordion on the home page. The user can see which houses are within which regions. This will allow the user an easy method of finding which house belongs where as it categorises houses into regions; this allows the user to discover which houses are allies. This user story is also achieved as the region names are links to individual pages that the user can navigate to providing them with some infomation regarding that particular region. Within this the user can find which house rules which region with some extra content about that region and house.


All links in the accordion are targeted using Jinja templating (url_for) and target the functions for directing the user to a region page selected. 

To test the responsiveness of the site, the chrome dev tools were used to change the screen size by making the dev tool window wider and by toggling the device tool bar to diplays on the different device options.


##Deployment
This section should describe the process you went through to deploy the project to a hosting platform (e.g. GitHub Pages or Heroku).

In particular, you should provide all details of the differences between the deployed version and the development version, if any, including:

Different values for environment variables (Heroku Config Vars)?
Different configuration files?
Separate git branch?
In addition, if it is not obvious, you should also describe how to run your code locally.


## Credits
## Content
The text for the region html pages was copied from here: https://gameofthrones.fandom.com/wiki/Seven_Kingdoms

The quotation on the home page is from the frst season of the show: https://www.youtube.com/watch?v=RzRbFDWy_lE

The quotations from the region html pages are from the characters of the show


## Media
Background images and sigils are taken from google and edited in PhotoScape X (http://x.photoscape.org/) and CSS

All icons on each region html page are from here: https://www.kisspng.com/png/

With the exception of The North and The Iron Islands: 

The icon of The North page is from here: https://fontawesome.com/icons/wolf-pack-battalion?style=brands

The icon of The Iron Isands page is from here:
https://fontawesome.com/icons/gitkraken?style=brands

All edited using PhotoScape X


## Acknowledgements
I received inspiration for this project from A Game of Thrones and A Song of Ice and Fire

