from flask import Flask, jsonify
from flask_cors import CORS
from pymongo import MongoClient

app = Flask(__name__)
CORS(app)  # Enable CORS globally

# MongoDB Connection
MONGO_URI = "mongodb://localhost:27017/"
client = MongoClient(MONGO_URI)
db = client["planets_db"]  # Database name
collection = db["planets"]  # Collection name

@app.route('/planets', methods=['GET'])
def get_planets():
    planets = collection.find({}, {"_id": 0, "name": 1, "gravity": 1})  # Exclude '_id' field
    planets_data = {planet["name"]: planet["gravity"] for planet in planets}
    return jsonify(planets_data)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)