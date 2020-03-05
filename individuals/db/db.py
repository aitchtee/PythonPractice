import os
import sqlite3
import json

filename = 'mydb.db'
create = not os.path.exists(filename)
db = sqlite3.connect(filename)
if create:
    cursor = db.cursor()
    cursor.execute("CREATE TABLE crews("
                   "id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,"
                   "crew_name TEXT UNIQUE NOT NULL)")
    cursor.execute("CREATE TABLE styles("
                   "id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,"
                   "style_name TEXT UNIQUE NOT NULL)")
    cursor.execute("CREATE TABLE dancers("
                   "id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,"
                   "crew_id INTEGER NOT NULL,"
                   "style_id INTEGER NOT NULL,"
                   "dancer_name TEXT UNIQUE NOT NULL,"
                   "FOREIGN KEY(crew_id) REFERENCES crews(id),"
                   "FOREIGN KEY(style_id) REFERENCES styles(id))")
    db.commit()

cursor = db.cursor()
# cursor.execute("INSERT INTO crews(crew_name) VALUES ('No Team')")
# cursor.execute("INSERT INTO crews(crew_name) VALUES ('Jabbawockeez')")
# cursor.execute("INSERT INTO crews(crew_name) VALUES ('Kinjaz')")

# cursor.execute("INSERT INTO styles(style_name) VALUES('Hip-Hop')")
# cursor.execute("INSERT INTO styles(style_name) VALUES('Popping')")
# cursor.execute("INSERT INTO styles(style_name) VALUES('Breaking')")

# cursor.execute("INSERT INTO dancers(crew_id, style_id, dancer_name) VALUES(2, 3, 'Steven Lor')")
# cursor.execute("INSERT INTO dancers(crew_id, style_id, dancer_name) VALUES(1, 2, 'Dytto')")
# cursor.execute("INSERT INTO dancers(crew_id, style_id, dancer_name) VALUES(1, 1, 'Taylor Hatala')")
# cursor.execute("INSERT INTO dancers(crew_id, style_id, dancer_name) VALUES(2, 3, 'Ben Chung')")
# cursor.execute("INSERT INTO dancers(crew_id, style_id, dancer_name) VALUES(2, 1, 'Phil Tayag')")
db.commit()

cursor2 = db.cursor()
cursor2.execute("SELECT d.id, c.crew_name, s.style_name, d.dancer_name FROM dancers d "
                "INNER JOIN crews c ON d.crew_id = c.id "
                "INNER JOIN styles s ON d.style_id = s.id")
# cursor2.execute("select * from dancers ORDER BY id")

records = cursor2.fetchall()
res = {}
resList = []
for i, record in enumerate(records):
    res["id"] = records[i][0]
    res["crew_name"] = records[i][1]
    res["style_name"] = records[i][2]
    res["dancer_name"] = records[i][3]
    resList.append(res.copy())

with open("data_file.json", "w") as write_file:
    json.dump(resList, write_file, indent=4)
