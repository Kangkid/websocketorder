# -*- coding: utf-8 -*-

import sys
import logging
import psycopg2
import os
print('Loading function')

logger = logging.getLogger()
def main_handler():

    logger.info("start main handler")

    Host="postgres-dwj1bc4n.sql.tencentcdb.com"
    User="tencentdb_dwj1bc4n"
    Password="8tpwd[0O32um|^P"
    DB="tencentdb_dwj1bc4n"
    Port="50140"
    #Host = os.getenv('host')
    #Port = os.getenv('port')
    #User = os.getenv('user')
    #Password = os.getenv('password')
    #DB = os.getenv('dbname')
	
    conn = psycopg2.connect(database=DB, user=User, password=Password, host=Host, port=Port)
    print "Opened database successfully"

    cur = conn.cursor() 
    cur.execute("SELECT shop_name, dish, price  from info_shop")

    rows = cur.fetchall()
    shop_info = {}
    
    for row in rows:
        if shop_info.has_key(row[0]) is False:
            shop_info[row[0]] = []
        one = {}
        one["dish"] = row[1]
        one["price"] = row[2]

        print(row[0], row[1], row[2])
        print(one)
        shop_info[row[0]].append(one)


    print(shop_info)
    conn.commit()
    conn.close()

    return shop_info