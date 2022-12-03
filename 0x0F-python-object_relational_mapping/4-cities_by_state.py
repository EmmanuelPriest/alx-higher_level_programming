#!/usr/bin/python3

'''script that lists all cities from the database hbtn_0e_4_usa'''
import sys
import MySQLdb

if __name__ == "__main__":
    database = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2],
                               database=sys.argv[3], port=3306)

    current = database.cursor()
    current.execute("SELECT cities.id, cities.name, states.name FROM cities \
                    JOIN states ON cities.state_id = states.id;")
    states = current.fetchall()

    for state in state:
        print("{}".format(state))
