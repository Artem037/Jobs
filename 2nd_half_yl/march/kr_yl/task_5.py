from flask import Flask
import sqlite3

app = Flask(__name__)

with open('natives.txt', 'r', encoding='utf-8') as f:
    db_name, place = f.readlines()
    db_name = db_name.strip('\n')

sqlite_connection = sqlite3.connect(db_name)
cursor = sqlite_connection.cursor()

sqlite_select_query = f"""SELECT settlement, level, tools, place from inhabitants"""
cursor.execute(sqlite_select_query)
records = cursor.fetchall()

lists = []

for settlement, level, tools, place_got in records:
    if place_got == place:
        lists.append([settlement, level, tools])

lists.sort(key=lambda x: (-x[1], x[2]))
cursor.close()

res_list = []

for i in lists:
    res_list.append({"settlement": i[0], "level": i[1], "tools": i[2]})

@app.route('/level')
def level():
    return res_list


app.run(host='127.0.0.1', port=5000)
