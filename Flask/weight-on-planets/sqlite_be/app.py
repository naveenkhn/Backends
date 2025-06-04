from flask import Flask, jsonify
from flask_cors import CORS
from models import db, Planet

app = Flask(__name__)
CORS(app)

# SQLite Database Configuration
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///planets.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Initialize DB inside app
db.init_app(app)

# Create tables & insert data if not exists
with app.app_context():
	#	This command checks for the example.db file:
	#	If it does not exist, SQLite creates it automatically.
	#	If it already exists, it just ensures the tables are defined inside.
    db.create_all()
    if not Planet.query.first():
        planets = [
            Planet(name="Mercury", gravity=0.38),
            Planet(name="Venus", gravity=0.91),
            Planet(name="Earth", gravity=1.00),
            Planet(name="Mars", gravity=0.38),
            Planet(name="Jupiter", gravity=2.34),
            Planet(name="Saturn", gravity=1.06),
            Planet(name="Uranus", gravity=0.92),
            Planet(name="Neptune", gravity=1.19),
        ]
        db.session.bulk_save_objects(planets)
        db.session.commit()
        print("Database initialized with planets!")

# API Route
@app.route("/planets", methods=["GET"])
def get_planets():
    planets = Planet.query.all()
    # Convert database objects to a dictionary format
    planet_dict = {p.name: p.gravity for p in planets}
    return jsonify(planet_dict)

# Run Server
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)