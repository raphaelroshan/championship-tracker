from app import db
class Team(db.Model):
    name = db.Column(db.String(50), nullable=False, primary_key=True)
    registration_date = db.Column(db.String(10), nullable=False)
    group_number = db.Column(db.Integer, nullable=False)

class MatchResult(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    team_a_name = db.Column(db.String(50), nullable=False)
    team_b_name = db.Column(db.String(50), nullable=False)
    team_a_goals = db.Column(db.Integer, nullable=False)
    team_b_goals = db.Column(db.Integer, nullable=False)