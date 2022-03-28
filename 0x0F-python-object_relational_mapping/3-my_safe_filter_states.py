#!/usr/bin/python3
"""takes arguments and displays all values safe from injection"""

if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    connection = MySQLdb.connect(host="localhost",
                                 port=3306,
                                 user=argv[1],
                                 passwd=argv[2],
                                 db=argv[3])
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM states WHERE BINARY name='{}'ORDER BY id ASC"
                   .format(argv[4]))
    query_rows = cursor.fetchall()
    for row in query_rows:
        print(row)
    cursor.close()
    connection.close()
