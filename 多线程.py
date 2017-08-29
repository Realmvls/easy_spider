#!/usr/bin/Python
# -*- coding: utf-8 -*-
#例一

import requests
import threading
import time
Headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36'}
class GetUrl(threading.Thread):
    def __init__(self,url):
        threading.Thread.__init__(self)
        self.url = url
    def run(self):
        response = requests.get(self.url,headers = Headers)                          #requests.get才能传headers，urlopen则不能。。
        print(self.url)
def get_response():
    urls =[
        'http://www.baidu.com',
        'http://www.taobao.com',
        'http://www.youku.com',
        'http://www.ctrip.com'
    ]
    global start
    start = time.time()
    threads = []
    for url in urls:
        t = GetUrl(url)
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    print("end time is:", time.time() - start)
get_response()





##对比
# def get_response():
#     urls =[
#         'http://www.baidu.com',
#         'http://www.taobao.com',
#         'http://www.youku.com',
#         'http://www.ctrip.com',
#         'http://www.github.com'
#
#     ]
#     start = time.time()
#     for url in urls:
#         print(url)
#         response = requests.get(url,headers = Headers)
#     print('end time is:',time.time()-start)
# get_response()




# #例二
# import threading
# import requests
# import queue
# import time
#
# hosts = ['http://www.baidu.com',
#          'http://www.taobao.com',
#          'http://www.youku.com',
#          'http://www.ctrip.com',
#          'http://www.github.com']
# class MyThread(threading.Thread):
#     def __init__(self,queue):
#         threading.Thread.__init__(self)
#         self.queue = queue
#     def run(self):
#         host = self.queue.get()
#         url = requests.get(host)
#         print(url)
#         self.queue.task_done()
# def main():
#     q = queue.Queue()
#     for i in range(len(hosts)):
#         t = MyThread(q)
#         t.setDaemon(True)
#         t.start()
#     for host in hosts:
#         q.put(host)
#     q.join()
# if __name__=='__main__':
#     start = time.time()
#     main()
#     end = time.time()-start
#     print('%f'%end)


