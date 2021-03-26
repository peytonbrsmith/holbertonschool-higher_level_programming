#!/usr/bin/python3
"""cities by state
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

    cur.execute("SELECT cities.id, cities.name, states.name \
                FROM cities, states \
                WHERE states.id = state_id \
                GROUP BY id")
    rows = cur.fetchall()
    for row in rows:
            print(row)

    cur.close()
    db.close()
