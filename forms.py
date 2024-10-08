from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField
from wtforms.validators import DataRequired

class TeamRegistrationForm(FlaskForm):
    teams_data = TextAreaField('Enter team information with format: <Team Name> <DD/MM> <Group Number>', validators=[DataRequired()],
                               render_kw={"placeholder": "firstTeam 17/05 2\nsecondTeam 07/02 2\n\nNote: team registrations can be updated with new input"})
    submit = SubmitField('Register Teams')

class MatchResultsForm(FlaskForm):
    teams_data = TextAreaField('Enter result information with format: <Team A name> <Team B name> <Team A goals scored> <Team B goals scored>', validators=[DataRequired()],
                               render_kw={"placeholder": "firstTeam secondTeam 0 3\nthirdTeam fourthTeam 1 1"})
    submit = SubmitField('Submit Results')

class TeamSearchForm(FlaskForm):
    team_name = TextAreaField('Enter team name', validators=[DataRequired()],
                              render_kw={"placeholder": "firstTeam"})
    submit = SubmitField('Search Team')

class EditResultsForm(FlaskForm):
    results_data = TextAreaField('Edit Match Results', validators=[DataRequired()])
    submit = SubmitField('Update Results')
