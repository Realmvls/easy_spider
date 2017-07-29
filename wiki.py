#!/usr/bin/Python
# -*- coding: utf-8 -*-

'''采集wiki百科python词条的历史编辑页面，并通过freegeoip.net提供的
API把采集到的历史编辑页面中的ip地址对应成地理位置并输出'''
from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import datetime
import random
import re
import json

random.seed(datetime.datetime.now())                         #生成一个以当前系统时间为随机种子的随机系统参数
def getLinks(articleUrl):                                   #建立一个getLinks函数。作用：把以en.wikipedia.org域名开头的域名用beaurifulsoup解析，并通过正则表达式等条件筛选并返回该页面中所有指向其他词条的链接。
    html = urlopen("http://en.wikipedia.org"+articleUrl)     #当前python词条历史编辑页面含有词条链接和其他链接（ps：维基百科的每个页面都充满了侧边栏、页眉、页脚链接，以及连接到分类页面、对话页面和其他不包含词条的页面的链接）
    bsObj = BeautifulSoup(html, "html.parser")               #要过滤指向其他页面的其他链接，观察可得词条链接的三个共同点：1它们都在id是bodyContent的div标签里。2URL链接不包含冒号。3URL链接都以/wiki/开头
    return bsObj.find("div",{"id":"bodyContent"}).findAll("a",href=re.compile("^(/wiki/)((?!:).)*$"))

def getHistoryIPs(pageUrl):   #编辑历史页面URL链接格式:  https://en.wikipedia.org/w/index.php?title=Title_in_URL&action=history
    pageUrl = pageUrl.replace("/wiki/", "")
    historyUrl = "http://en.wikipedia.org/w/index.php?title=" + pageUrl + "&action=history"
    print ("history url is:"+historyUrl)
    html = urlopen(historyUrl)
    bsObj = BeautifulSoup(html,"html.parser")
    #找出class属性是“mw——anonuserlink”的链接
    #它们用IP地址代替用户名
    ipAddresses = bsObj.findAll("a",{"class":"mw-anonuserlink"})         #以后mw后面一定要看清楚是下划线还是减号啊啊啊啊啊啊！！！！！！！
    addressList = set()
    for ipAddress in ipAddresses:
        addressList.add(ipAddress.get_text())
    return addressList

def getCountry(ipAddress):       #调用API，获取ip地址对应的地理位置
    try:
        response = urlopen("http://freegeoip.net/json/"+ipAddress).read().decode('utf_8')
    except HTTPError:
        return None
    responseJson = json.loads(response)
    return responseJson.get("country_code")

links = getLinks("/wiki/Python_(programming_language)")

while(len(links) > 0):
    for link in links:
        print("-----------------------")
        historyIPs = getHistoryIPs(link.attrs["href"])
        for historyIP in historyIPs:
            country = getCountry(historyIP)
            if country is not None:
                print(historyIP+"is from"+country)
    newLink = links[random.randit(0,len(links)-1)].attrs["href"]   #random.randit(a,b)  a到b之前产生一个随机数（包含a，）
    links = getLinks(newLink)                                      #tag.attrs  取tag全部属性

'''#!/usr/bin/Python       #这段代码为验证这个函数getHistoryIPs(pageUrl)的输结果
# -*- coding: utf-8 -*-
from urllib.request import urlopen
from bs4 import BeautifulSoup
historyUrl = "https://en.wikipedia.org/w/index.php?title=Python_(programming_language)&action=history"
html = urlopen(historyUrl)
bsObj = BeautifulSoup(html, "html.parser")
ipAddresses = bsObj.findAll("a", {"class": "mw-anonuserlink"})
for ipAddress in ipAddresses:
    print(ipAddress.get_text())'''