import csv
import sqlite3

con = sqlite3.connect(input())
side, damage = input().split()
damage = int(damage)

cur = con.cursor()

ids = [i[0] for i in cur.execute("SELECT id FROM Sides WHERE title=?", (side,)).fetchall()]
res = []
for i in ids:
    result = cur.execute("SELECT id, owner, size FROM Rooms WHERE side_id = ?", (i,)).fetchall()
    res.append(result)
itog_1 = []
for i in res:
    for j in i:
        id_it = j[0]
        itog = cur.execute("SELECT broken_thing, damage, can_be_repaired FROM Protocol WHERE room_id = ?", (id_it,)).fetchall()
        itog_1.append(itog)

a = []
for i in range(len(itog_1)):
    for j in itog_1[i]:
        if int(j[1]) > damage:
            a.append([j[0], str(j[1]), str(j[2]), str(res[0][i][2]), res[0][i][1]])

with open('damage.csv', 'w', newline='\n', encoding="utf8") as csvfile:
    writer = csv.writer(csvfile, delimiter=';', quotechar='"')
    for row in a:
        writer.writerow(row)
