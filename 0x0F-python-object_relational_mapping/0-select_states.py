#!/usr/bin/python3

'''script that lists all states from the database hbtn_0e_0_usa'''
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv1[1], passwd=sys.argv[2],
                         db=sys.argv[3], port=3306)

    current = db.cursor()
    current.execute("SELECT * FROM states;")
    states = current.fetchall()

    for state in states:
        print(state)
