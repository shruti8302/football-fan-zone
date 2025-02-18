import unittest
import json
from app import app, db
from models import Competition, Player, UpcomingMatch, Match, Team, FeaturedMatch

class TestAPI(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Configure the app for testing
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        cls.app = app.test_client()

        # Push the application context
        cls.app_context = app.app_context()
        cls.app_context.push()

        # Create the database and seed test data
        with app.app_context():
            db.drop_all()  # Clear the database first
            db.create_all()
            print("Database created.")  # Debug statement
            cls.seed_test_data()

    @classmethod
    def tearDownClass(cls):
        # Clean up the database after all tests
        with app.app_context():
            db.session.remove()  # Close the session
            db.drop_all()
        # Pop the application context
        cls.app_context.pop()

    @classmethod
    def seed_test_data(cls):
        # Add test data to the database
        print("Seeding test data...")
        competition = Competition(id=1, name="Premier League", country="England", season="2023/24", logo="logo.png")
        team = Team(id=1, name="Team A", logo="team_a.png", competition="Premier League", founded=1900, stadium="Stadium A", manager="Manager A", squad="Player1,Player2")
        player = Player(id=1, name="Player 1", position="Forward", team="Team A", image="player1.png", stats={"goals": 10})
        match = Match(id=1, home_team="Team A", away_team="Team B", date="2023-10-01", time="15:00", home_score=2, away_score=1, home_team_logo="team_a.png", away_team_logo="team_b.png", competition_id=1)
        featured_match = FeaturedMatch(id=1, match_id=1, is_featured=True)
        upcoming_match = UpcomingMatch(id=1, player_id=1, home_team="Team A", away_team="Team B", date="2023-10-01")

        db.session.add(competition)
        db.session.add(team)
        db.session.add(player)
        db.session.add(match)
        db.session.add(featured_match)
        db.session.add(upcoming_match)
        db.session.commit()
        print("Test data seeded successfully.")

    # Test Competitions Endpoint
    def test_get_competitions(self):
        # Test without search query
        response = self.app.get('/competitions/')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(type(data), list)
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]["name"], "Premier League")

        # Test with search query
        response = self.app.get('/competitions/?search=premier')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]["name"], "Premier League")

        # Test with no results
        response = self.app.get('/competitions/?search=nonexistent')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(len(data), 0)

    # Test Players Endpoint
    def test_get_players(self):
        # Test without filters
        response = self.app.get('/players/')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(type(data), list)
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]["name"], "Player 1")

        # Test with search query
        response = self.app.get('/players/?search=player')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]["name"], "Player 1")

        # Test with team filter
        response = self.app.get('/players/?team=Team A')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]["team"], "Team A")

        # Test with position filter
        response = self.app.get('/players/?position=Forward')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]["position"], "Forward")

        # Test with no results
        response = self.app.get('/players/?search=nonexistent')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(len(data), 0)

    # Test Player Detail Endpoint
    def test_get_player_detail(self):
        # Test valid player ID
        response = self.app.get('/players/1')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data["name"], "Player 1")
        self.assertEqual(len(data["upcoming_matches"]), 1)
        self.assertEqual(data["upcoming_matches"][0]["home_team"], "Team A")

        # Test invalid player ID
        response = self.app.get('/players/999')
        self.assertEqual(response.status_code, 404)

    # Test Teams Endpoint
    def test_get_teams(self):
        # Test without search query
        response = self.app.get('/teams/')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(type(data), list)
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]["name"], "Team A")

        # Test with search query
        response = self.app.get('/teams/?search=team')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]["name"], "Team A")

        # Test with no results
        response = self.app.get('/teams/?search=nonexistent')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(len(data), 0)

    # Test Matches Endpoint
    def test_get_matches(self):
        # Test without filters
        response = self.app.get('/matches/')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(type(data), list)
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]["home_team"], "Team A")

        # Test with search query
        response = self.app.get('/matches/?search=team')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]["home_team"], "Team A")

        # Test with competition filter
        response = self.app.get('/matches/?competition=Premier League')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]["competition"], "Premier League")

        # Test with date filter
        response = self.app.get('/matches/?date=2023-10-01')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]["date"], "2023-10-01")

        # Test with area filter
        response = self.app.get('/matches/?area=England')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]["area"], "England")

        # Test with no results
        response = self.app.get('/matches/?search=nonexistent')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(len(data), 0)

    # Test Featured Matches Endpoint
    def test_get_featured_matches(self):
        response = self.app.get('/matches/featured')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(type(data), list)
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]["home_team"], "Team A")
    
if __name__ == '__main__':
    unittest.main()