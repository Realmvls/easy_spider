#!/usr/bin/Python
# -*- coding: utf-8 -*-
#!/usr/bin/Python
# -*- coding: utf-8 -*-

import csv
# csvfile = open('F:/spider_data/csvtext.csv','w',newline='')     #此处为w而非wb
# writer = csv.writer(csvfile)
# writer.writerow(['姓名','年龄','电话'])
# data = [
#     ('小李','21','2626565'),
#     ('小留','21','87989565'),
#     ('小刘','23','848445')
#
# ]
# writer.writerows(data)
# csvfile.close()

csvfile = open('F:/spider_data/csvtext.csv','r')           #此处为r 而非rb
reader = csv.reader(csvfile)
for line in reader:
    print(line)
csvfile.close()