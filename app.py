from flask import Flask, render_template, redirect, url_for, flash
from forms import TeamRegistrationForm, MatchResultsForm, TeamSearchForm
from models import update_registration, update_results, clear_stored_data, calculate_rankings_grouped, search
import os
from datetime import datetime

app = Flask(__name__)
# secret key for csrf validation, could be generated with os.urandom(24) for a more secure key
# csrf validation is included in FlaskForm
app.config['SECRET_KEY'] = 'tempsecretkey' 

# Store team data locally
DATA_FILE = 'teams_data.txt'
RESULT_FILE = 'results_data.txt'
LOG_FILE = 'log.txt'

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
        log_action("register teams")
        teams_data = form.teams_data.data
        teams_list = teams_data.split('\n')
        for team_info in teams_list:
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
        log_action("register results")
        results_data = form.teams_data.data
        results_list = results_data.split('\n')
        for result_info in results_list:
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
@app.route('/clear_data')
def clear_data():
    log_action("clear data")
    if os.path.exists(DATA_FILE):
        os.remove(DATA_FILE)
    if os.path.exists(RESULT_FILE):
        os.remove(RESULT_FILE)
    clear_stored_data()
    return redirect(url_for('index'))

@app.route('/search_team', methods=['GET', 'POST'])
def search_team():
    form = TeamSearchForm()
    team_data = None
    if form.validate_on_submit():
        team_name = form.team_name.data
        team_data = search(team_name)
        if not team_data:
            flash(f"No results found for team: {team_name}", 'error')

    return render_template('search_team.html', form=form, team_data=team_data)

def log_action(action):
    with open(LOG_FILE, 'a') as file:
        timestamp = datetime.now().strftime('%d/%m %H:%M:%S')
        file.write(f"{timestamp} - {action}\n")

@app.route('/clear_log')
def clear_log():
    if os.path.exists(LOG_FILE):
        os.remove(LOG_FILE)
    return redirect(url_for('index'))

@app.route('/view_log')
def view_log():
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, 'r') as file:
            logs = file.readlines()
    else:
        logs = ["No logs available"]

    return render_template('view_log.html', logs=logs)

def reload_data():
    # used on start, and on edit
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as file:
            teams = file.readlines()
        for team_info in teams:
            team_name, reg_date, group_number = team_info.split()
            update_registration(team_name, reg_date, group_number)

    if os.path.exists(RESULT_FILE):
        with open(RESULT_FILE, 'r') as file:
            results = file.readlines()
        for result_info in results:
            team_a_name, team_b_name, team_a_goals, team_b_goals = result_info.split()
            update_results(team_a_name, team_b_name, team_a_goals, team_b_goals)

@app.route('/')
def index():
    reload_data()
    ranked_groups = calculate_rankings_grouped()
    return render_template('index.html', ranked_groups=ranked_groups)

if __name__ == '__main__':
    app.run(debug=True)