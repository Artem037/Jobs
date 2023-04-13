import sqlite3

filename = input()
con = sqlite3.connect(filename)
cur = con.cursor()
result = cur.execute("""SELECT * FROM films
WHERE films.title LIKE '%?'""").fetchall()

for elem in result:
    print(elem[1])

con.close()
