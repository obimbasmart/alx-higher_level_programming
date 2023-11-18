#!/usr/bin/python3

'''mysql->python: filter states by name'''

import MySQLdb
import sys

if __name__ == '__main__':
    _, user_name, passwd, db_name = sys.argv
    db = MySQLdb.connect(host='localhost', user=user_name,
                         passwd=passwd, db=db_name)
    cur = db.cursor()
    cur.execute("""SELECT cities.id, cities.name, states.name
                FROM cities
                INNER JOIN states ON cities.state_id = states.id""")

    query_result = cur.fetchall()
    for item in query_result:
        print(item)

    cur.close()
    db.close()
