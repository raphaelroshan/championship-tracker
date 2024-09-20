
This is Raphael Joseph's submission for Govtech take home assignment for software engineer

This is meant to be a simple python + flask based app that can handle the basic requirements, with the bonus requirements being added later.

Directory structure:
- Templates : for HTML templates for flask

Main files:
- app.py : load the flask app and routes
- models.py : load the database model
- forms.py : for input forms (wtflask)

# To run repo
2 commands to run: Install dependencies with `pip install -r requirements.txt`, and run flask app with `flask run`

Note: I used a venv when running locally, can be done with
    create venv: `python -m venv venv`
    enter venv: `source venv/bin/activate` for Mac, `venv\Scripts\activate` for Windows

# How have I implemented the objectives?
## Basic tasks
1. Register teams: Done by accessing the register teams button
2. Register match results: Done by accessing the register match results button
3. Display rankings: Displayed by default on the home page
4. Retrieve details: Done by using the search team button
5. Edit previous data: there are two update methods
    1. updating a team registration - done by default in the register team page when you provide new details for a given team
    2. updating the match scores - done by using the update results page
6. Clear all previously entered data: Done by using the clear data button
7. Ensure application is secured: The application is secured by using csrf validation with flask and strong os.urandom key, secures against cross site request forgery,
    Additionally no input is able to influence internal working so injection attacks will not work
8. Record down logs: Logs are created to record data level actions, accessed with view logs button

## Bonus tasks achieved
3. Database persistence: Txt files act as db, allow flask to reload data as needed across multiple restarts
4. Handle invalid input sensibly: Done by raising errors when data is incorrectly processed, and notifying user. Also input is required to avoid empty submissions
7. Static code analysis: Used pylint for static code analysis, with .pylintrc settings and pylint_report.txt artifact
note: the remaining bonus tasks are detailed below with future plans

## Design decisions
**Input**:
Registration of teams and match results using text area fields allows the bulk entry following the given format, and can be easily converted into data of the format i want
I can then perform any validation as required. Search also works similarly, with the exception that the input is considered a single string

**Output**:
I use flask's jinjja for loops and such to iterate through the data and to print it with minimal overhead. It also allows me to structure and organise the placement of text,
and even to generate rankings

**Storage**:
TXT files are the most lightweight method to both store and persist data, although the true form of data in the app memory is stored more similar to a document DB, where the data
is read and updated to allow for very quick retrieval. This could be upgraded to use either NOSQL or SQL databases, but at the scale of the app is sufficient

**Logging**:
The reduced granularity allows me to attach a log action to the basic functions that interact with data. While this reduces the meaningfulness of the logs, it still
provides a clear view of which actions were taken

**Editing data**:
The user is given access to directly update all prior data input, partially for ease of access but also because the expected use case for this app would be an organiser
who would know the correct data and format to input. In case they have forgotten, existing data is prepopulated for easy editing.

**Overall structure**:
Flask is used because it creates web applications, especially when hosted locally, very quickly and is very lightweight. Jinjja is excellent for formatting, and core features
such as notices, buttons and redirects are easily implemented. 

WTForms allows users to easily interact with the forms and are convenient for collecting data in the format required

Python is the language of choice due to ease of picking up and modularity of adding new libraries and functionality

## assumptions
teams must first be registered to play
Teams are unique, team A can play against team B any number of times

## future improvements:
inefficient writing of data (should write in bulk preferably, currently single line)
inefficient update of data (should re-read single value preferably, currently reads all data)
unclear logging (logging should be more granular, not just button based)

Bonus items:
1. I would use a provider like GCP with the $300 credits to host, and the txt files could be stored on 
2. A static checker like bandit + authentication would help secure the site
5. I would use a library like fuzzywuzzy to do similarity searches, eg. when a team is added to the register matches and its not an existing team,
    I could do a suggest_similar that finds the nearest existing name to the name being added
6. Authentication - I would use sqlalchemy, or a cloud hosted db to store logins and users, and also allow people to register new accounts. 

Noted bugs to fix:
1. view teams shows all changes made due to reference being change history and not storage
2. Date entry is not sanity checked
3. log clutter when editing results

Note: my git history features many gitignore updates due to a misconfiguration of my gitignore and vscode settings, has been fixed