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
                   "FOREIGN KEY(crew_id) REFERENCE crews(id),"
                   "FOREIGN KEY(style_id) REFERENCE styles(id))")
    db.commit()

cursor = db.cursor()
# cursor.execute("INSERT INTO styles(style_name) VALUES('Hip-Hop')")
# cursor.execute("INSERT INTO styles(style_name) VALUES('Popping')")
# cursor.execute("INSERT INTO styles(style_name) VALUES('Breaking')")
cursor.execute("INSERT INTO dancers(crew_id, style_id, dancer_name) VALUES(2, 3, 'Steven Lor')")
db.commit()

cursor2 = db.cursor()
cursor2.execute("SELECT * FROM crews")

records = cursor2.fetchall()
dictRecord = dict(records)
for i, record in enumerate(records):
    print("{0} : {1}".format(record[0], record[1]))

with open("data_file.json", "w") as write_file:
    json.dump(dictRecord, write_file, indent=4)

print("===============================")

cursor3 = db.cursor()
cursor3.execute("SELECT * FROM styles")

records = cursor3.fetchall()
dictRecord = dict(records)

for i, record in enumerate(records):
    print("{0} : {1}".format(record[0], record[1]))

