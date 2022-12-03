#!/usr/bin/python3

'''
script that lists all states with a name starting with N (upper N) from the database hbtn_0e_0_usa
'''
import sys
import MySQLdb

if __name__ == "__main__":
    database = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2],
                               database=sys.argv[3], port=3306)

    current = database.cursor()
    current.execute("SELECT * FROM states WHERE CONVERT(`name` USING Latin1) \
                    COLLATE Latin1_General_CS LIKE 'N%';")
    states = current.fetchall()

    for state in states:
        print("{}".format(state))
