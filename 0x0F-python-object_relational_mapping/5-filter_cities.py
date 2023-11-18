#!/usr/bin/python3

'''mysql->python: filter cities by state name'''

import MySQLdb
import sys

if __name__ == '__main__':
    _, user_name, passwd, db_name, state_name = sys.argv
    db = MySQLdb.connect(host='localhost', user=user_name,
                         passwd=passwd, db=db_name)
    cur = db.cursor()
    cur.execute("""SELECT cities.name
                FROM cities
                INNER JOIN states ON cities.state_id = states.id
                WHERE BINARY states.name = %s""", (state_name,))

    query_result = cur.fetchall()
    output = ', '.join([item[0] for item in query_result])
    print(output)
    cur.close()
    db.close()
