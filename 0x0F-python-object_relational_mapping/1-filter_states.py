#!/usr/bin/python3

'''mysql->python: lists all states from the database
hbtn_0e_0_usa with name starting with N'''

import MySQLdb
import sys

if __name__ == '__main__':
    _, user_name, passwd, db_name = sys.argv
    db = MySQLdb.connect(host='localhost', user=user_name,
                         passwd=passwd, db=db_name)
    cur = db.cursor()
    cur.execute(''' SELECT * FROM states
                    WHERE name LIKE BINARY "N%"
                    ORDER BY states.id ASC
                ''')
    query_result = cur.fetchall()

    for item in query_result:
        print(item)

    cur.close()
    db.close()
