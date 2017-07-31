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

#参考：http://blog.csdn.net/robertchenguangzhi/article/details/49174523   连接
       #http://www.cnblogs.com/hateislove214/archive/2010/11/05/1869889.html   mysql基本指令