# Inspiré de https://www.digitalocean.com/community/tutorials/how-to-use-the-sqlite3-module-in-python-3

import sqlite3
import os

database_name = 'database.db'
# Ouverture de la DB, création si elle n'existe pas
connection = sqlite3.connect(database_name)
cursor = connection.cursor()


# On regarde si la DB est vierge et on crée la table et les insert
if os.path.getsize(f'./{database_name}') == 0:
    cursor.execute("CREATE TABLE fish (name TEXT, species TEXT, tank_number INTEGER)")
    cursor.execute("INSERT INTO fish VALUES ('Sammy', 'shark', 1)")
    cursor.execute("INSERT INTO fish VALUES ('Jamie', 'cuttlefish', 7)")

# Last insert ID
cursor.execute("INSERT INTO fish VALUES ('Sammy', 'shark', 1)")
print(cursor.lastrowid)

# SELECT
rows = cursor.execute("SELECT name, species, tank_number FROM fish").fetchall()
for row in rows:
    print(row[0], row[1])


# UPDATE
qry = "UPDATE fish SET name = 'JB' WHERE tank_number = 7"
cursor.execute(qry)

# Affected rows
print(cursor.rowcount)

connection.commit()
connection.close()