import sqlite3


def get_result(name):
    con = sqlite3.connect(name)
    cur = con.cursor()
    req = f"DELETE FROM {name} WHERE genre = (SELECT id FROM genres WHERE title = 'комедия')"
    cur.execute(req).fetchall()
    con.commit()
    con.close()
