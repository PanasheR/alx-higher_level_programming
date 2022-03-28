#!/usr/bin/python3
"""script takes in the name of a state as an argument
and list all cities of the state"""

if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    connection = MySQLdb.connect(host="localhost",
                                 port=3306,
                                 user=argv[1],
                                 passwd=argv[2],
                                 db=argv[3])
    cursor = connection.cursor()
    cursor.execute("SELECT cities.name FROM cities "
                   "JOIN states ON cities.state_id = states.id "
                   "WHERE states.name LIKE %s "
                   "ORDER BY cities.id", (argv[4],))
    rows = cursor.fetchall()
    cities = ""
    for row in rows:
        cities += row[0] + ", "
    print(cities[0: -2:])
    cursor.close()
    connection.close()
