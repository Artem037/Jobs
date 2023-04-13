import sqlite3

filename = input()
con = sqlite3.connect(filename)
cur = con.cursor()
result = cur.execute("""SELECT DISTINCT year FROM films
WHERE films.title LIKE 'Х%'""").fetchall()

for elem in result:
    print(elem[1])

con.close()
