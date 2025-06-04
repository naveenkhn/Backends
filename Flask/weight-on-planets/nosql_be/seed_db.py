from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["planets_db"]
collection = db["planets"]

# Data to insert
planets_data = [
    {"name": "Mercury", "gravity": 0.38},
    {"name": "Venus", "gravity": 0.91},
    {"name": "Earth", "gravity": 1.00},
    {"name": "Mars", "gravity": 0.38},
    {"name": "Jupiter", "gravity": 2.34},
    {"name": "Saturn", "gravity": 1.06},
    {"name": "Uranus", "gravity": 0.92},
    {"name": "Neptune", "gravity": 1.19}
]

# Insert data
collection.insert_many(planets_data)

print("✅ Data inserted successfully!")