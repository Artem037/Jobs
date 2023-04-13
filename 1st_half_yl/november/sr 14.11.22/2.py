import sqlite3

con = sqlite3.connect(input())

first = input()
second = input()
third = input()
cur = con.cursor()
result = cur.execute("SELECT team_id, leader FROM towage WHERE " + first + ' AND ' + second + ' OR ' + third).fetchall()
for i in sorted(result, key=lambda x: x[1]):
    print(f'{i[0]} ({i[1]})')
