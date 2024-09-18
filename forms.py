from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField
from wtforms.validators import DataRequired
class TeamRegistrationForm(FlaskForm):
    teams_data = TextAreaField('Enter team information', validators=[DataRequired()],
                               render_kw={"placeholder": "firstTeam 17/05 2\nsecondTeam 07/02 2"})
    submit = SubmitField('Register Teams')