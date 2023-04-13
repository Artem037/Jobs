import sqlite3


def get_result(name):
    con = sqlite3.connect(name)
    cur = con.cursor()
    req = f"UPDATE {name} SET duration = '42' WHERE not duration"
    cur.execute(req).fetchall()
    con.commit()
    con.close()
