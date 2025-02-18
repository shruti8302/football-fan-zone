from flask import Flask
from flask_cors import CORS
from flask_restx import Api
from database import db
from routes import api_blueprint

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}}, supports_credentials=True)

# SQLite Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///football.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize Database
db.init_app(app)

# Register Blueprint
app.register_blueprint(api_blueprint)

# API Documentation
api = Api(app, doc="/swagger")

if __name__ == "__main__":
    with app.app_context():
        # db.drop_all()
        db.create_all()  # Ensure tables are created
    app.run(debug=True)
