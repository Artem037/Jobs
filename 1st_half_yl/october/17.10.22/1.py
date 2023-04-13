# Импорт библиотеки
import sqlite3

# Подключение к БД
con = sqlite3.connect("films_db.sqlite")

# Создание курсора
cur = con.cursor()

result = cur.execute("""SELECT * FROM films, genres
    WHERE films.duration >= 60 AND genres.id = films.genre AND 
        genres.title = 'комедия'""").fetchall()

for elem in result:
    print(elem)

con.close()