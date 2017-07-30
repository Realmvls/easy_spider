#!/usr/bin/Python
# -*- coding: utf-8 -*-
import csv
csvFile = open("F:/github/easy_spider/test.csv",'w+')
try:
    writer = csv.writer(csvFile)
    writer.writerow(('number','number plus 2','number time 2'))
    for i in range(10):
        writer.writerow((i,i+2,i*2))
finally:
    csvFile.close