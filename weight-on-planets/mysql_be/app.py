from flask import Flask, jsonify
from flask_cors import CORS  # Import CORS
import mysql.connector

app = Flask(__name__)
CORS(app)  # Enable CORS globall

# MySQL Database Configuration
db_config = {
    'host': 'localhost',  # or your MySQL server address
    'user': 'root',       # MySQL username
    'password': '',       # MySQL password (leave empty if none)
    'database': 'planets_db'  # Name of the database
}

# Create a connection to MySQL
def get_db_connection():
    conn = mysql.connector.connect(**db_config)
    return conn

@app.route('/planets', methods=['GET'])
def get_planets():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    
    cursor.execute("SELECT * FROM planets")
    planets = cursor.fetchall()
    
    cursor.close()
    conn.close()

    # Reformat the response as a dictionary of planet names and their gravity values
    planets_data = {planet['name']: planet['gravity'] for planet in planets}

    return jsonify(planets_data)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)