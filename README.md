# Game of Thrones Characters

This is my website used to display lists and categorised lists of chatracters from the TV series A Game of Thrones. Users can perform CRUD commands on the app and in essence take 'control' of the data. The data is stored and outputted from a database via MongoDB.

## UX

### User Stories:
'As a Game of Thrones fan I would like to see a website that displays a list of all of the main and recurring characters as there are too many to remember by heart and I would like to remember names to faces. I would like the list displayed alphabetically so it is easy to look through and digest' - users can find a list of all characters within the database on the app which displays all characters alphabetically.

'As a user I would like to be able to easily discern which character belongs to which house so that it is easier to understand who are allies and distant relatives' - The home page of the app provides the user with an accordion which breaks down houses within regions, and then characters within those houses.


'As a user I would like a 'live' website that will allow myself and others to add character infomation to it as the show still has not finished. It would be great to add any new/old characters and any info that someone else adding character info may have missed for referencing purposes for myself' - users can perform CRUD commands on individual characters through the All Characters page. Once the user clicks on a character, they are given the option to edit and delete. Users can create a new characters by selecting the Add Character link at the top of the page.

'As a Game of Thrones fan I would like to remember which house is in what region. I'd like the ability to visually see which house is where to understand which houses are allies' - Users can visually find the houses within their retrospective regions through the accordion on the home page.


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
In this section, you need to convince the assessor that you have conducted enough testing to legitimately believe that the site works well. Essentially, in this part you will want to go over all of your user stories from the UX section and ensure that they all work as intended, with the project providing an easy and straightforward way for the users to achieve their goals.

Whenever it is feasible, prefer to automate your tests, and if you've done so, provide a brief explanation of your approach, link to the test file(s) and explain how to run them.

For any scenarios that have not been automated, test the user stories manually and provide as much detail as is relevant. A particularly useful form for describing your testing process is via scenarios, such as:

## Contact form:
Go to the "Contact Us" page
Try to submit the empty form and verify that an error message about the required fields appears
Try to submit the form with an invalid email address and verify that a relevant error message appears
Try to submit the form with all inputs valid and verify that a success message appears.
In addition, you should mention in this section how your project looks and works on different browsers and screen sizes.

You should also mention in this section any interesting bugs or problems you discovered during your testing, even if you haven't addressed them yet.

If this section grows too long, you may want to split it off into a separate file and link to it from here.

## Deployment
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