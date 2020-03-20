import cgi
import sqlite3


# print("Content-type: text/html\n")
# print("""<!DOCTYPE HTML>
#         <html>
#         <head>
#             <meta charset="utf-8">
#             <title>Обработка данных форм</title>
#         </head>
#         <body>""")
#
# print("<h1>Обработка данных форм!</h1>")
# print("<p>Имя: {}</p>".format(text1))
# print("<p>Команда: {}</p>".format(crew[0]))
# print("<p>Стиль: {}</p>".format(style[0]))
#
# print("""</body>
#         </html>""")

filename = 'mydb.db'
conn = sqlite3.connect(filename)
# cur = conn.cursor()
# conn.commit()

form = cgi.FieldStorage()
text1 = form.getfirst("TEXT_1", "не задано")
crew = form.getfirst("crewName")
style = form.getfirst("styleName")

cur = conn.cursor()
gen = [(crew[0], style[0], text1)]
cur.executemany("insert into dancers(crew_id, style_id, dancer_name) values (?,?,?)", gen)
conn.commit()

cur.execute("select * from dancers")
rows = cur.fetchall()
for row in rows:
    print(row[0], row[1], row[2])
