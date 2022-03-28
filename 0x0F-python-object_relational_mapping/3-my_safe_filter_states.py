#!/usr/bin/python3
"""takes in an argument and displays all values
and keeps query safe from sql injection."""

if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    conn = MySQLdb.connect(host="localhost",
                           port=3306,
                           user=argv[1],
                           passwd=argv[2],
                           db=argv[3])
    cur = conn.cursor()
    cur.execute("SELECT * FROM states WHERE BINARY name='{}' ORDER BY id ASC"
                .format(argv[4]))
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
