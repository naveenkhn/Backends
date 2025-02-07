Install MySQL Server
    MySQL is not a Python package, so it needs to be installed outside the virtual environment(venv).

    During installation, you'll see below useful info
        We've installed your MySQL database without a root password. To secure it run:
            mysql_secure_installation

        MySQL is configured to only allow connections from localhost by default

        To connect run:
            mysql -u root

        To start mysql now and restart at login:
            brew services start mysql

Start MySQL in the background
    This ensures MySQL is available system-wide, even after closing the terminal.
        brew services start mysql
    Below command starts mysql only for the current terminal session
        mysql.server start
    verify MySQL is running by checking its status:
        brew services list

Install the MySQL Connector:
    In your virtual environment, run the following command to install the connector:
        pip install mysql-connector-python

Create the MySQL Database and User
    mysql -u root -p (Drop -p if no password is set)
    Create the Database (Schema)
        CREATE DATABASE planets_db;
    Switch to the newly created database:
        USE planets_db;
    Now, create the planets table with two columns:
        CREATE TABLE planets (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(50) UNIQUE NOT NULL,
            gravity FLOAT NOT NULL
        );
    Insert data
        INSERT INTO planets (name, gravity) VALUES
        ('Mercury', 0.38),
        ('Venus', 0.91),
        ('Earth', 1.00),
        ('Mars', 0.38),
        ('Jupiter', 2.34),
        ('Saturn', 1.06),
        ('Uranus', 0.92),
        ('Neptune', 1.19),
        ('Pluto', 0.06);
    Verify data
        SELECT * FROM planets;

Configure backend(app.py) to Connect to MySQL:
    Create a connection to mysql server using host, user, schema_name etc
    prepare query and retrieve data
    return data in json format on the specified route

Where and how exactly does it store table info ?
    To see where MySQL is currently storing your databases, run this in the MySQL prompt:
        SHOW VARIABLES LIKE 'datadir';
    It shows path similar to below
        /opt/homebrew/var/mysql/

Inside /opt/homebrew/var/mysql/, you’ll find a folder named after your schema (database name), and inside that folder, you’ll see .ibd files like planets.ibd.

Explanation:
	•	planets.ibd: This file stores the actual table data and indexes for the planets table.
	•	.ibd stands for InnoDB tablespace file, meaning your MySQL database is using the InnoDB storage engine (default for MySQL).
	•	Unlike SQLite (which stores everything in a single .db file), MySQL organizes data into separate files per table inside the schema directory.