from flask import Flask, render_template, redirect, url_for, flash
from forms import TeamRegistrationForm, MatchResultsForm
from models import update_registration, update_results, clear_data
import os

app = Flask(__name__)
# secret key for csrf validation, could be generated with os.urandom(24) for a more secure key
# csrf validation is included in FlaskForm
app.config['SECRET_KEY'] = 'tempsecretkey' 

# Store team data locally
DATA_FILE = 'teams_data.txt'
RESULT_FILE = 'results_data.txt'

def store_team_data(data):
    with open(DATA_FILE, 'a') as file:
        file.write(data + '\n')

def store_result_data(data):
    with open(RESULT_FILE, 'a') as file:
        file.write(data + '\n')

@app.route('/view_teams')
def view_teams():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as file:
            teams = file.readlines()
    else:
        teams = []
    return render_template('view_teams.html', teams=teams)

@app.route('/view_results')
def view_results():
    if os.path.exists(RESULT_FILE):
        with open(RESULT_FILE, 'r') as file:
            results = file.readlines()
    else:
        results = []

    return render_template('view_results.html', results=results)

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
                update_registration(team_name, reg_date, group_number)
                store_team_data(f"{team_name} {reg_date} {group_number}")
            except ValueError:
                flash('Invalid input format. Make sure each line follows the format: <Team Name> <DD/MM> <Group Number>', 'error')
                return redirect(url_for('register_teams'))

        return redirect(url_for('register_teams'))

    return render_template('register_teams.html', form=form)

@app.route('/register_results', methods=['GET', 'POST'])
def register_results():
    form = MatchResultsForm()

    if form.validate_on_submit():
        results_data = form.teams_data.data
        results_list = results_data.split('\n')
        for result_info in results_list:
            # Ensure each result line has team names and goals scored, all stored as strings
            try:
                team_a_name, team_b_name, team_a_goals, team_b_goals = result_info.split()
                update_results(team_a_name, team_b_name, team_a_goals, team_b_goals)
                store_result_data(f"{team_a_name} {team_b_name} {team_a_goals} {team_b_goals}")
            except ValueError:
                flash('Invalid input format. Make sure each line follows the format: <Team A name> <Team B name> <Team A goals scored> <Team B goals scored>', 'error')
                return redirect(url_for('register_results'))

        return redirect(url_for('register_results'))

    return render_template('register_results.html', form=form)

# clear ALL data
@app.route('/clear_data', methods=['GET','POST'])
def clear_data():
    if os.path.exists(DATA_FILE):
        os.remove(DATA_FILE)
    if os.path.exists(RESULT_FILE):
        os.remove(RESULT_FILE)
    return redirect(url_for('index'))

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)