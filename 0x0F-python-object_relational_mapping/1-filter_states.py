#!/usr/bin/python3
"""filter states
"""
if __name__ == '__main__':
    import MySQLdb
    import sys

    USER = sys.argv[1]
    PASS = sys.argv[2]
    DATABASE = sys.argv[3]

    db = MySQLdb.connect(
        host="localhost",
        user=USER,
        passwd=PASS,
        db=DATABASE,
        port=3306)

    cur = db.cursor()

    cur.execute("SELECT * FROM states ORDER BY states.id")
    rows = cur.fetchall()
    for row in rows:
        if row[1].startswith("N"):
            print(row)

    cur.close()
    db.close()
