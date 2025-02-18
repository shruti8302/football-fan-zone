from flask import Blueprint, request, jsonify
from flask_restx import Api, Resource, fields
from models import Competition, Player, UpcomingMatch, Match, Team, FeaturedMatch
from database import db

api_blueprint = Blueprint("api", __name__)
api = Api(api_blueprint, title="Football API", version="1.0")

# Namespaces
competition_ns = api.namespace("competitions", description="Football Competitions API")

player_ns = api.namespace("players", description="Football Players API")

team_ns = api.namespace("teams", description="Football Teams API")

match_ns = api.namespace("matches", description="Football Matches API")

# Match Model for Swagger Documentation
match_model = api.model("Match", {
    "id": fields.Integer,
    "home_team": fields.String,
    "away_team": fields.String,
    "date": fields.String,
    "home_score": fields.Integer,
    "away_score": fields.Integer,
    "competition": fields.String,
})


# Player Model for Swagger Documentation
player_model = api.model("Player", {
    "id": fields.Integer,
    "name": fields.String,
    "position": fields.String,
    "team": fields.String,
    "image": fields.String,
})

player_detail_model = api.model("PlayerDetail", {
    "id": fields.Integer,
    "name": fields.String,
    "position": fields.String,
    "team": fields.String,
    "image": fields.String,
    "stats": fields.Raw,
    "upcoming_matches": fields.List(fields.Raw),
})


# Competition Routes (Existing)
@competition_ns.route("/")
class CompetitionList(Resource):
    def get(self):
        """Get all competitions (with optional search)"""
        search_query = request.args.get("search", "").lower()
        query = Competition.query
        if search_query:
            query = query.filter(Competition.name.ilike(f"%{search_query}%"))

        competitions = query.all()
        return jsonify([
            {"id": c.id, "name": c.name, "country": c.country, "season": c.season, "logo": c.logo}
            for c in competitions
        ])

# Player Routes
@player_ns.route("/")
class PlayerList(Resource):
    @player_ns.doc(params={
        "search": "Search by player name",
        "team": "Filter by team",
        "position": "Filter by position",
    })
    def get(self):
        """Get all players (with optional search and filters)"""
        search_query = request.args.get("search", "").lower()
        team_filter = request.args.get("team")
        position_filter = request.args.get("position")

        query = Player.query

        if search_query:
            query = query.filter(Player.name.ilike(f"%{search_query}%"))
        if team_filter:
            query = query.filter(Player.team == team_filter)
        if position_filter:
            query = query.filter(Player.position == position_filter)

        players = query.all()
        return jsonify([
            {"id": p.id, "name": p.name, "position": p.position, "team": p.team, "image": p.image}
            for p in players
        ])

@player_ns.route("/<int:player_id>")
class PlayerDetail(Resource):
    @player_ns.marshal_with(player_detail_model)
    def get(self, player_id):
        """Get details of a specific player"""
        player = Player.query.get_or_404(player_id)
        upcoming_matches = UpcomingMatch.query.filter_by(player_id=player_id).all()

        return {
            "id": player.id,
            "name": player.name,
            "position": player.position,
            "team": player.team,
            "image": player.image,
            "stats": player.stats,
            "upcoming_matches": [
                {"id": m.id, "home_team": m.home_team, "away_team": m.away_team, "date": m.date}
                for m in upcoming_matches
            ],
        }
    
# Team Model for Swagger Documentation
team_model = api.model("Team", {
    "id": fields.Integer,
    "name": fields.String,
    "logo": fields.String,
    "competition": fields.String,
    "founded": fields.Integer,
    "stadium": fields.String,
    "manager": fields.String,
    "squad": fields.List(fields.String),
})

@team_ns.route("/")
class TeamList(Resource):
    @team_ns.doc(params={
        "search": "Search teams by name",
    })
    def get(self):
        """Get all teams with optional search"""
        search_query = request.args.get("search", "").lower()
        
        # Create query
        query = Team.query
        if search_query:
            query = query.filter(Team.name.ilike(f"%{search_query}%"))
        
        teams = query.all()

        return jsonify([
            {
                "id": t.id,
                "name": t.name,
                "logo": t.logo,
                "competition": t.competition,
                "founded": t.founded,
                "stadium": t.stadium,
                "manager": t.manager,
                "squad": t.squad.split(",")  # Convert squad string to list
            }
            for t in teams
        ])

@match_ns.route("/")
class MatchList(Resource):
    @match_ns.doc(params={
        "search": "Search by match (home/away team)",
        "competition": "Filter by competition name",
        "date": "Filter by date",
        "area": "Filter by competition country (area)"
    })
    def get(self):
        """Get all matches (with optional search and filters)"""
        search_query = request.args.get("search", "").lower()
        competition_filter = request.args.get("competition")
        date_filter = request.args.get("date")
        area_filter = request.args.get("area")

        # Start with a base query
        query = Match.query.join(Competition)  # Join with the Competition table

        # Apply search filter (home_team or away_team)
        if search_query:
            query = query.filter(
                (Match.home_team.ilike(f"%{search_query}%")) |
                (Match.away_team.ilike(f"%{search_query}%"))
            )

        # Apply competition filter (competition name)
        if competition_filter:
            query = query.filter(Competition.name.ilike(f"%{competition_filter}%"))

        # Apply date filter
        if date_filter:
            query = query.filter(Match.date == date_filter)

        # Apply area filter (competition country)
        if area_filter:
            query = query.filter(Competition.country.ilike(f"%{area_filter}%"))

        # Execute the query and fetch matches
        matches = query.all()

        # Format the response
        return jsonify([
            {
                "id": m.id,
                "home_team": m.home_team,
                "away_team": m.away_team,
                "date": m.date,
                "time": m.time,
                "home_score": m.home_score,
                "away_score": m.away_score,
                "home_logo": m.home_team_logo,
                "away_logo": m.away_team_logo,
                "competition": m.competition.name,
                "competition_logo": m.competition.logo,
                "area": m.competition.country  # Use the country field from Competition
            }
            for m in matches
        ])
    
@match_ns.route("/featured")
class FeaturedMatchList(Resource):
    def get(self):
        """Get all featured matches"""
        featured_matches = (
            db.session.query(FeaturedMatch, Match)
            .join(Match, FeaturedMatch.match_id == Match.id)
            .filter(FeaturedMatch.is_featured == True)
            .all()
        )

        # Format the response
        matches = [
            {
                "id": fm[1].id,  # Match ID
                "home_team": fm[1].home_team,
                "away_team": fm[1].away_team,
                "date": fm[1].date,
                "home_score": fm[1].home_score,
                "away_score": fm[1].away_score,
                "home_team_logo": fm[1].home_team_logo,
                "away_team_logo": fm[1].away_team_logo,
                "competition": fm[1].competition.name if fm[1].competition else None
            }
            for fm in featured_matches
        ]

        return jsonify(matches)



