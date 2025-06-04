from flask import Flask, jsonify
from flask_cors import CORS  # Import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS globall

# Static JSON data for weight multipliers on planets
PLANET_DATA = {
    "Mercury": 0.38,
    "Venus": 0.91,
    "Earth": 1.0,
    "Mars": 0.38,
    "Jupiter": 2.34,
    "Saturn": 1.06,
    "Uranus": 0.92,
    "Neptune": 1.19,
    "Pluto": 0.06
}

@app.route('/planets', methods=['GET'])
def get_planets():
    """Endpoint to get weight multipliers for all planets."""
    return jsonify(PLANET_DATA)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)