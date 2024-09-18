from flask import Flask, render_template, redirect, url_for, flash
from forms import TeamRegistrationForm
import os
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# secret key for csrf validation, could be generated with os.urandom(24) for a more secure key
# csrf validation is included in FlaskForm
app.config['SECRET_KEY'] = 'tempsecretkey' 

# Store team data locally
DATA_FILE = 'teams_data.txt'

db = SQLAlchemy()
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///championship-tracker.db"
db.init_app(app)

def init_db(app):
    db.init_app(app)
    with app.app_context():
        db.create_all()

def store_team_data(data):
    with open(DATA_FILE, 'a') as file:
        file.write(data + '\n')

@app.route('/view_teams')
def view_teams():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as file:
            teams = file.readlines()
    else:
        teams = []

    return render_template('view_teams.html', teams=teams)

@app.route('/register_teams', methods=['GET', 'POST'])
def register_teams():
    form = TeamRegistrationForm()

    if form.validate_on_submit():
        teams_data = form.teams_data.data
        teams_list = teams_data.split('\n')
        for team_info in teams_list:
            # Ensure each team line has name, date, group, all stored as strings
            try:
                team_name, reg_date, group_number = team_info.split()
                store_team_data(f"{team_name} {reg_date} {group_number}")
            except ValueError:
                flash('Invalid input format. Make sure each line follows the format: <Team Name> <DD/MM> <Group Number>', 'error')
                return redirect(url_for('register_teams'))

        flash('Teams registered successfully!', 'success')
        return redirect(url_for('register_teams'))

    return render_template('register_teams.html', form=form)

@app.route('/clear_data', methods=['GET','POST'])
def clear_data():
    if os.path.exists(DATA_FILE):
        os.remove(DATA_FILE)
    return redirect(url_for('index'))

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)