Step 1: Install SQLite and Required Packages
    QLite is built into Python, but we need Flask-SQLAlchemy to interact with the database.
    pip install Flask-SQLAlchemy
    Add this to requirements.txt for future reference:
        Flask-SQLAlchemy==3.1.1

Step 2: Set Up the SQLite Database
    Inside your sqlite_backend/ folder, create a new file called models.py

Step 3: Modify app.py to Use SQLite

Step 4: Run the Flask App
    python sqlite_backend/app.py
    It should now serve data from SQLite at http://127.0.0.1:5000/planets.
    Test with Postman or curl

When Should You Use SQLite?

✅ Good for:
	•	Small apps, prototypes, or local storage.
	•	Single-user or low-concurrency applications.
	•	Applications that don’t need authentication at the database level.

❌ Not Ideal for:
	•	Multi-user, high-concurrency web apps. (Multiple users can read concurrently but not write)
	•	Applications needing user roles and access control.
	•	Large datasets with complex queries.