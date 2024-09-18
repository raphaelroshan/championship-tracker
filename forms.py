from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField
from wtforms.validators import DataRequired
class TeamRegistrationForm(FlaskForm):
    teams_data = TextAreaField('Enter team information', validators=[DataRequired()],
                               render_kw={"placeholder": "firstTeam 17/05 2\nsecondTeam 07/02 2"})
    submit = SubmitField('Register Teams')

class MatchResultsForm(FlaskForm):
    teams_data = TextAreaField('Enter result information', validators=[DataRequired()],
                               render_kw={"placeholder": "firstTeam secondTeam 0 3\nthirdTeam fourthTeam 1 1"})
    submit = SubmitField('Submit Results')
