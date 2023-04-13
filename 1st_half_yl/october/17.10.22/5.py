import sqlite3

filename = input()
con = sqlite3.connect(filename)
cur = con.cursor()
result = cur.execute("""SELECT * FROM films, genres
    WHERE films.duration >= 60 AND genres.id = films.genre AND 
        genres.title = 'комедия'""").fetchall()

for elem in result:
    print(elem[1])

con.close()
