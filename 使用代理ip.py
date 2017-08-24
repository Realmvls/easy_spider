#!/usr/bin/Python
# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
# import socket
a=0   #用来统计一共多少个ip
Headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36'}
base_url = 'http://www.xicidaili.com/nn/'         #国内免费高匿ip
for u in range(113,2337):
    print('第%d页'%(u))
    html = requests.get(base_url+str(u),headers=Headers).content
    soup = BeautifulSoup(html,'html.parser')
    data = soup.find_all('tr')
    # print(len(data))
    proxys = []
    for x in range(1,len(data)):                       #ip地址以及端口信息是从第二个tr标签开始的
        ip = data[x]
        tds = ip.find_all('td')
        # print(tds)
        proxys.append(tds[1].text)
        proxys.append(tds[2].text)
        # d = tds[1].text+'\t'+tds[2].text
        # print(d)

    #并不是所有的代理都能用，原因有很多，可能是我们所处的网络连不到这个代理，也有可能是这个代理，连不到我们的目标网址，所以，我们要验证一下。以http://ip.chinaz.com/getip.aspx作为目标网址为例（这个是测试ip地址的网址）代码如下：
    # socket.setdefaulttimeout(2)                       #socket.setdefaulttimeout(3)设置全局超时时间为3s，也就是说，如果一个请求3s内还没有响应，就结束访问，并返回timeout（超时）
    z = []
    num = len(proxys)//2                                #因为ip地址和端口号一共为两行，所以总个数要除2
    h = 0
    for i in range(0,num):
        proxy_host = 'http://'+proxys[h]+':'+proxys[h+1]
        proxy_temp = {"http":proxy_host}               #proxy_temp = {"http":proxy_host}其中http代表代理的类型，除了http之外还有https，socket等，这里就以http为例
        z.append(proxy_temp)                           #此处为代理ip的固定格式
        h = h+1
    finallyip = []
    url = "http://ip.chinaz.com/getip.aspx"        #这个是测试ip地址的网址
    p = 1
    for proxy in z:
        print('正在处理第%d个'%(p))
        p = p+1
        try:
            response = requests.get(url,proxies=proxy,timeout = 1)           #此处可传递proxies参数，urlopen不可以传递proxies参数。以代理模式访问目标网址
            finallyip.append(proxy)
            # print(response.text)
        except Exception as e:           # Exception 为所有异常的基类。此句为捕捉多个异常并将异常对象输出
            # print(proxy)
            # print(e)
            continue

    file = open('F:/spider_data/ip.txt', 'a')        #a的意思是接着写入，改成w则为替换写入
    for e in finallyip:
        file.write(str(e))          #此处finallyip为列表，里面的所有的元素为字典对象，file.write的对象必须是字符串所以用str转换一下
        file.write('\n')
    file.close()
    u = u+len(finallyip)            #共有多少个可用ip
print(u)



############################################################################################################################
#验证代理ip是否存活的一种方法，讲真也就前100页存活率高一点点。。。
# import requests
# try:
#     requests.get('http://www.baidu.com/', proxies={"http":"http://113.241.248.198:80"},timeout = 1)
# except:
#     print( 'connect failed')
# else:
#     print('success')
############################################################################################################################
# for u in finallyip:
#     print(u)

# 随机或按顺序获取finallyip并把它直接传入requests的get方法中便可切换代理访问网址
# web_data = requests.get(url, headers=headers, proxies=proxies)

# split()通过指定分隔符对字符串进行切片，如果参数num 有指定值，则仅分隔 num 个子字符串
#split()方法语法：
#str.split(str="", num=string.count(str)).
#str -- 分隔符，默认为所有的空字符，包括空格、换行(\n)、制表符(\t)等。num -- 分割次数。
#返回分割后的字符串列表返回值

#示例
    # str = "this is string example....wow!!!"
    # print(str.split())
    # print(str.split('i', 1))
    # print(str.split('w'))
#结果
    # ['this', 'is', 'string', 'example....wow!!!']
    # ['th', 's is string example....wow!!!']
    # ['this is string example....', 'o', '!!!']



