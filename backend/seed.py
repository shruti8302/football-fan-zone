from app import app, db
from models import Competition, Player, UpcomingMatch, Team, Match, FeaturedMatch

def seed_database():
    with app.app_context():
        db.create_all()

        # Seed Competitions (if not already seeded)
        if not Competition.query.first():
            dummy_competitions = [
                Competition(name="Premier League", country="England", season="2024-2025",
                            logo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSk717VDVUAAa5prL4G_7r8s75vWsbO6_2JRA&s"),
                Competition(name="La Liga", country="Spain", season="2024-2025",
                            logo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQps-BO5mHEnbvJapQR15SLaTLVsvj2siL-rQ&s"),
                Competition(name="Serie A", country="Italy", season="2024-2025",
                            logo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSfyU_Ubt8hhs-a4Sv6Sj4cZIH4ucqIQn4lV2ZzefRA2sULh9iTtw61Bh2ddhmPu8okSjQ&usqp=CAU"),
                Competition(name="Bundesliga", country="Germany", season="2024-2025",
                            logo="https://upload.wikimedia.org/wikipedia/en/d/df/Bundesliga_logo_%282017%29.svg"),
                Competition(name="Ligue 1", country="France", season="2024-2025",
                            logo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQkJlxJoD9DQphhcmpcVLqT59TOqe7vVErRkI0xja48eOCcZ71iCsOEbD3jNooFQ6Lbjgg&usqp=CAU"),
            ]
            db.session.bulk_save_objects(dummy_competitions)

        # Seed Players (if not already seeded)
        if not Player.query.first():
            players_data = [
                {
                    "name": "Lionel Messi",
                    "position": "Forward",
                    "team": "Inter Miami",
                    "image": "https://assets.goal.com/images/v3/bltd58c4d60ecd9275e/GOAL_-_Blank_WEB_-_Facebook_-_2023-06-13T135350.847.png?auto=webp&format=pjpg&width=1080&quality=60",
                    "stats": {"matches": 25, "goals": 18, "assists": 12, "yellow_cards": 2, "red_cards": 0},
                    "upcoming_matches": [
                        {"home_team": "Inter Miami", "away_team": "LA Galaxy", "date": "2025-03-01"},
                        {"home_team": "New York City FC", "away_team": "Inter Miami", "date": "2025-03-05"},
                    ],
                },
                {
                    "name": "Cristiano Ronaldo",
                    "position": "Forward",
                    "team": "Al Nassr",
                    "image": "https://hips.hearstapps.com/hmg-prod/images/cristiano-ronaldo-of-portugal-reacts-as-he-looks-on-during-news-photo-1725633476.jpg",
                    "stats": {"matches": 22, "goals": 20, "assists": 8, "yellow_cards": 1, "red_cards": 0},
                    "upcoming_matches": [
                        {"home_team": "Al Nassr", "away_team": "Al Hilal", "date": "2025-02-28"},
                    ],
                },
                {
                    "name": "Neymar Jr.",
                    "position": "Forward",
                    "team": "Al Hilal",
                    "image": "https://en.psg.fr/media/251568/123.jpg?quality=60&width=1600&bgcolor=ffffff",
                    "stats": {"matches": 23, "goals": 15, "assists": 5, "yellow_cards": 3, "red_cards": 0},
                    "upcoming_matches": [],
                },
                {
                    "name": "Robert Lewandowski",
                    "position": "Forward",
                    "team": "Barcelona",
                    "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSCycZFEqKaL0HETlnMyLXZI_7fl_chH_OUZI6gfPN0f2pVu4vPV2QJB3ai49XtPYQcYn8&usqp=CAU",
                    "stats": {"matches": 26, "goals": 30, "assists": 10, "yellow_cards": 1, "red_cards": 0},
                    "upcoming_matches": [],
                },
                {
                    "name": "Sergio Ramos",
                    "position": "Defender",
                    "team": "Al Hilal",
                    "image": "https://img.a.transfermarkt.technology/portrait/big/25557-1694502812.jpg?lm=1",
                    "stats": {"matches": 20, "goals": 3, "assists": 1, "yellow_cards": 5, "red_cards": 1},
                    "upcoming_matches": [],
                },
               
            ]

            for data in players_data:
                player = Player(
                    name=data["name"],
                    position=data["position"],
                    team=data["team"],
                    image=data["image"],
                    stats=data["stats"],
                )
                db.session.add(player)
                db.session.flush()  # Ensure player.id is available

                for match_data in data["upcoming_matches"]:
                    competition = Competition.query.first()
                    match = UpcomingMatch(
                        home_team=match_data["home_team"],
                        away_team=match_data["away_team"],
                        date=match_data["date"],
                        player_id=player.id,
                    )
                    db.session.add(match)

        # Seed Teams (if not already seeded)
        if not Team.query.first():
            teams_data = [
                Team(
                    name="Manchester United",
                    logo="https://upload.wikimedia.org/wikipedia/en/7/7a/Manchester_United_FC_crest.svg",
                    competition="Premier League",
                    founded=1878,
                    stadium="Old Trafford",
                    manager="Erik ten Hag",
                    squad="Bruno Fernandes,Marcus Rashford,Casemiro"
                ),
                Team(
                    name="Real Madrid",
                    logo="https://upload.wikimedia.org/wikipedia/en/5/56/Real_Madrid_CF.svg",
                    competition="La Liga",
                    founded=1902,
                    stadium="Santiago Bernabéu",
                    manager="Carlo Ancelotti",
                    squad="Vinicius Jr,Jude Bellingham,Thibaut Courtois"
                ),
                Team(
                    name="AC Milan",
                    logo="https://upload.wikimedia.org/wikipedia/commons/d/d0/Logo_of_AC_Milan.svg",
                    competition="Serie A",
                    founded=1899,
                    stadium="San Siro",
                    manager="Stefano Pioli",
                    squad="Zlatan Ibrahimović,Theo Hernández,Leao"
                ),
                Team(
                    name="Chelsea",
                    logo="https://upload.wikimedia.org/wikipedia/en/c/cc/Chelsea_FC.svg",
                    competition="Premier League",
                    founded=1905,
                    stadium="Stamford Bridge",
                    manager="Graham Potter",
                    squad="Mason Mount,Raheem Sterling,Thiago Silva"
                ),
                Team(
                    name="Barcelona",
                    logo="https://upload.wikimedia.org/wikipedia/en/4/47/FC_Barcelona_%28crest%29.svg",
                    competition="La Liga",
                    founded=1899,
                    stadium="Camp Nou",
                    manager="Xavi Hernández",
                    squad="Robert Lewandowski,Ansu Fati,Pablo Gavi"
                ),
                Team(
                    name="Arsenal",
                    logo="https://upload.wikimedia.org/wikipedia/en/5/53/Arsenal_FC.svg",
                    competition="Premier League",
                    founded=1886,
                    stadium="Emirates Stadium",
                    manager="Mikel Arteta",
                    squad="Bukayo Saka,Martin Ødegaard,Alexandre Lacazette"
                ),
            ]
            
            db.session.add_all(teams_data)  # Add all team instances to the session

        # Seed Matches (if not already seeded)
        if not Match.query.first():
            matches_data = [
                {
                    "home_team": "Manchester United",
                    "away_team": "Liverpool",
                    "date": "2025-02-18",
                    "time": "15:00",  # Add time field
                    "home_score": 2,
                    "away_score": 1,
                    "competition": "Premier League",
                    "home_team_logo": "https://upload.wikimedia.org/wikipedia/en/7/7a/Manchester_United_FC_crest.svg",
                    "away_team_logo": "https://upload.wikimedia.org/wikipedia/en/0/0c/Liverpool_FC.svg",
                },
                {
                    "home_team": "Real Madrid",
                    "away_team": "Barcelona",
                    "date": "2025-02-18",
                    "time": "20:00",  # Add time field
                    "home_score": 3,
                    "away_score": 2,
                    "competition": "La Liga",
                    "home_team_logo": "https://upload.wikimedia.org/wikipedia/en/5/56/Real_Madrid_CF.svg",
                    "away_team_logo": "https://upload.wikimedia.org/wikipedia/en/4/47/FC_Barcelona_%28crest%29.svg",
                },
                {
                    "home_team": "Chelsea",
                    "away_team": "Arsenal",
                    "date": "2025-02-18",
                    "time": "18:30",  # Add time field
                    "home_score": 2,
                    "away_score": 0,
                    "competition": "Premier League",
                    "home_team_logo": "https://upload.wikimedia.org/wikipedia/en/c/cc/Chelsea_FC.svg",
                    "away_team_logo": "https://upload.wikimedia.org/wikipedia/en/5/53/Arsenal_FC.svg",
                },
                {
                    "home_team": "Barcelona",
                    "away_team": "Atletico Madrid",
                    "date": "2025-02-19",
                    "time": "21:00",  # Add time field
                    "home_score": 3,
                    "away_score": 1,
                    "competition": "La Liga",
                    "home_team_logo": "https://upload.wikimedia.org/wikipedia/en/4/47/FC_Barcelona_%28crest%29.svg",
                    "away_team_logo": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQatqY-mSoQFyFNB5xmlWAJeS03_FMgwDxzuQ&s",
                },
                {
                    "home_team": "Liverpool",
                    "away_team": "Manchester City",
                    "date": "2025-02-19",
                    "time": "19:45",  # Add time field
                    "home_score": 2,
                    "away_score": 2,
                    "competition": "Premier League",
                    "home_team_logo": "https://upload.wikimedia.org/wikipedia/en/0/0c/Liverpool_FC.svg",
                    "away_team_logo": "https://upload.wikimedia.org/wikipedia/en/e/eb/Manchester_City_FC_badge.svg",
                }
            ]

            # Add each match data as a Match instance
            for match_data in matches_data:
                competition = Competition.query.filter_by(name=match_data["competition"]).first()
                if competition:
                    match = Match(
                        home_team=match_data["home_team"],
                        away_team=match_data["away_team"],
                        date=match_data["date"],
                        time = match_data["time"],
                        home_score=match_data["home_score"],
                        away_score=match_data["away_score"],
                        home_team_logo=match_data["home_team_logo"],  # Add home team logo
                        away_team_logo=match_data["away_team_logo"],  # Add away team logo
                        competition_id=competition.id
                    )
                    db.session.add(match)

            db.session.commit()

        # Seed FeaturedMatches (if not already seeded)
        if not FeaturedMatch.query.first():
            featured_matches_data = [
                    {"home_team": "Manchester United", "away_team": "Liverpool", "date": "2025-02-18", "competition": "Premier League"},
                    {"home_team": "Real Madrid", "away_team": "Barcelona", "date": "2025-02-18", "competition": "La Liga"},
                    {"home_team": "Chelsea", "away_team": "Arsenal", "date": "2025-02-18", "competition": "Premier League"},
                    {"home_team": "Barcelona", "away_team": "Atletico Madrid", "date": "2025-02-19", "competition": "La Liga"},
                    {"home_team": "Liverpool", "away_team": "Manchester City", "date": "2025-02-19", "competition": "Premier League"},
                ]
      
            for match_data in featured_matches_data:
                match = Match.query.filter_by(
                    home_team=match_data["home_team"],
                    away_team=match_data["away_team"],
                    date=match_data["date"]
                ).first()

                if match:
                    featured_match = FeaturedMatch(
                        match_id=match.id,
                        is_featured=True  
                    )
                    db.session.add(featured_match)

            db.session.commit()

        db.session.commit()
        print("Database seeded successfully!")

if __name__ == "__main__":
    seed_database()
