from database import db

class Competition(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    country = db.Column(db.String(100), nullable=False)
    season = db.Column(db.String(20), nullable=False)
    logo = db.Column(db.String(255), nullable=False)

class Player(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    position = db.Column(db.String(50), nullable=False)
    team = db.Column(db.String(100), nullable=False)
    image = db.Column(db.String(255), nullable=False)
    stats = db.Column(db.JSON, nullable=False)  # Store stats as JSON
    upcoming_matches = db.relationship("UpcomingMatch", backref="player", lazy=True)

class UpcomingMatch(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    home_team = db.Column(db.String(100), nullable=False)
    away_team = db.Column(db.String(100), nullable=False)
    date = db.Column(db.String(20), nullable=False)  # Store date as string (e.g., "2025-03-01")
    player_id = db.Column(db.Integer, db.ForeignKey("player.id"), nullable=False)

class Team(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    logo = db.Column(db.String(255), nullable=False)
    competition = db.Column(db.String(100), nullable=False)
    founded = db.Column(db.Integer, nullable=False)
    stadium = db.Column(db.String(255), nullable=False)
    manager = db.Column(db.String(100), nullable=False)
    squad = db.Column(db.String(255), nullable=False)  # Comma-separated list

    def __repr__(self):
        return f'<Team {self.name}>'
    
class Match(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    home_team = db.Column(db.String(100), nullable=False)
    away_team = db.Column(db.String(100), nullable=False)
    date = db.Column(db.String(20), nullable=False) 
    time = db.Column(db.String(20), nullable=False) 
    home_score = db.Column(db.Integer, nullable=True)
    away_score = db.Column(db.Integer, nullable=True)
    home_team_logo = db.Column(db.String(255), nullable=False)
    away_team_logo = db.Column(db.String(255), nullable=False)
    competition_id = db.Column(db.Integer, db.ForeignKey("competition.id"), nullable=False)
    competition = db.relationship("Competition", backref="matches")

    def __repr__(self):
        return f"<Match {self.home_team} vs {self.away_team}>"

class FeaturedMatch(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    match_id = db.Column(db.Integer, db.ForeignKey('match.id'), nullable=False)
    is_featured = db.Column(db.Boolean, default=False)

    match = db.relationship('Match', backref=db.backref('featured_matches', lazy=True))


