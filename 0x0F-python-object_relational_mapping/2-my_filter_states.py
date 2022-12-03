#!/usr/bin/python3

'''
script that takes in an argument and displays all values in
the states table of hbtn_0e_0_usa where name matches the argument
'''
import sys
import MySQLdb

if __name__ == "__main__":
    database = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2],
                               database=sys.argv[3], port=3306)

    current = database.cursor()
    current.execute("SELECT * FROM states WHERE CONVERT(`name` USING Latin1) \
                    COLLATE Latin1_General_CS = '{}';".format(sys.argv[4]))
    states = current.fetchall()

    for state in states:
        print("{}".format(state))
