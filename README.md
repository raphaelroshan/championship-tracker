
This is Raphael Joseph's submission for Govtech take home assignment for software engineer

This is meant to be a simple python + flask based app that can handle the basic requirements, with the bonus requirements being added later.

Directory structure:
- Templates : for HTML templates for flask
- static : for any static CSS/ JS files I add
- logs : for any recorded logs

Main files:
- app.py : load the flask app and routes
- models.py : load the database model
- forms.py : for input forms (wtflask)
- views.py : handle routing
- database.py : handle the db connection

## Setup Instructions
1. Clone the repository.
2. Install dependencies:
    python -m venv venv
    source venv/bin/activate for Mac, venv\Scripts\activate for Windows
    pip install -r requirements.txt
3. run app with run flask

## How have I met the objectives?
# Basic tasks

Update methods:
1. re-registering a team - done by default in the register team page
2. updating the match scores - done by using the update results page

# Bonus tasks


# Design decisions

# assumptions
teams must first be registered to play
Teams are unique, team A can play against team B any number of times

# future improvements:
inefficient writing of data (should write in bulk preferably, currently single line)
inefficient update of data (should re-read single value preferably, currently reads all data)
unclear logging (logging should be more granular, not just button based)

Bonus item:
5. I would use a library like fuzzywuzzy to do similarity searches, eg. when a team is added to the register matches and its not an existing team,
I could do a suggest_similar that finds the nearest existing name to the name being added
6. Authentication - I would use sqlalchemy, or a cloud hosted db to store logins and users, and also allow people to register new accounts. 

Note: my git history features many gitignore updates due to a misconfiguration of my gitignore and vscode settings, has been fixed