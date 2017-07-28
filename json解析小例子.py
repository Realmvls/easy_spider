# !/usr/bin/Python
# -*- coding:utf8 -*-
# 打印某ip地址的国家代码
import json
from urllib.request import urlopen
def getCountry(ipaddress):
    response = urlopen("http://freegeoip.net/json/"+ipaddress).read().decode('utf-8')
    responseJson = json.loads(response)
    return responseJson.get("country_code")
print(getCountry("50.78.253.58"))


# Python json解析库处理json字符串中可能出现的数据类型
jsonString = '{"arrayOfNums":[{"number":0},{"number":1},{"number":2}],"arrayOfFruits":[{"fruit":"apple"},{"fruit":"banana"},{"fruit":"pear"}]}'
jsonObj = json.loads(jsonString)

print(jsonObj.get("arrayOfNums"))
print(jsonObj.get("arrayOfNums")[1])
print(jsonObj.get("arrayOfNums")[1].get("number")+
      jsonObj.get("arrayOfNums")[2].get("number"))
print(jsonObj.get("arrayOfNums")[2].get("fruit"))