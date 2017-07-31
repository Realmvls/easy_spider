#!/usr/bin/Python
# -*- coding: utf-8 -*-
import pymysql
conn = pymysql.connect(host='127.0.0.1',port = 3306,user='root',passwd=None,db='mysql')

cur = conn.cursor()
cur.execute("USE scraping")

cur.execute("select * from pages ")
print(cur.fetchone())
cur.close()
conn.close()