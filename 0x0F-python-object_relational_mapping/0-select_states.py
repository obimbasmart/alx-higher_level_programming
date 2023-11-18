#!/usr/bin/python3

import MySQLdb
import sys

if __name__ == '__main__':
    _, user_name, passwd, db_name = sys.argv
    db = MySQLdb.connect(host='localhost', user=user_name,
                         passwd=passwd, db=db_name)
    cur = db.cursor()
    cur.execute('SELECT * FROM states')
    query_result = cur.fetchall()

    for item in query_result:
        print(item)

    cur.close()
    db.close()
