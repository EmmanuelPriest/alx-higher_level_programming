#!/usr/bin/python3

'''script that lists all states from the database hbtn_0e_0_usa'''
import sys
import MySQLdb


f __name__ == "__main__":
    database MySQLdb.connect(user=sys.argv1[1], passwd=sys.argv[2],
                             database=sys.argv[3], port=3306)

    current = database.cursor()
    current.execute("SELECT * FROM states;")
    selected_states = current.fetchall()

    for state in selected_states:
        print("{}".format(state))
