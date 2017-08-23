#!/usr/bin/Python
# -*- coding: utf-8 -*-
#使用selenium打开chrome时要先安装与chrome版本对应的chrom浏览器驱动（chromedriver）并将其保存在所使用的python路径下的scripts目录下
# chromedriver所有版本在这个：http://chromedriver.storage.googleapis.com/index.html
# chromedriver2.31 支持chrome58-60
# 这里看chromedriver对应的版本：http://blog.csdn.net/huilan_same/article/details/51896672
#cmd中用pip list 查看所有安装过的包（路径：python/scripts）

# 新建项目的时候命名为selenium，则会自动在easy_spider下生成要给selenium.py的文件，此时在项目里import selenium，pycharm会先在当前目录下
# 也就是easy_spider中寻找selenium.py的文件，找到后然而里面并没有东西，真正的selenium模块并不在这里啊啊啊。。。。真正需要导入的应该是标准库里面的selenium.py所以会报错webdriver找不到。心累。。。
# 只需要将项目名称换个名字就好了，具体理由如下：
#python在import的时候是怎么找到他要import的模块or文件的？是从syspath(系统环境变量)找，大概长下面这个样子
# Windows:['', 'C:\\WINDOWS\\system32\\python24.zip', 'C:\\Documents and Settings\\weizhong', 'C:\\Python24\\DLLs', 'C:\\Python24\\lib', 'C:\\Python24\\lib\\plat-win', 'C:\\Python24\\lib\\lib-tk', 'C:\\Python24\\Lib\\site-packages\\pythonwin', 'C:\\Python24', 'C:\\Python24\\lib\\site-packages', 'C:\\Python24\\lib\\site-packages\\win32', 'C:\\Python24\\lib\\site-packages\\win32\\lib', 'C:\\Python24\\lib\\site-packages\\wx-2.6-msw-unicode']
# 空字符串 代表当前目录. 要加入新的搜索路径,只需要将这个路径加入到这个列表.
# 所以题主做这样一个实验，在任意目录下建一个文件架a，在里面建test.py 写一句import b运行，会报错找不到b，然后新建b.py啥也不写，再运行test就不报错了。
# 然后在test写一句from a import c，会报错找不到a，因为a是test的上层目录，test的当前目录没有a，建一个a.py，再运行会报错找不到c，因为他找到的当前目录下的a(是个py文件而不是文件夹)下面没有c。



from selenium import webdriver
driver = webdriver.Chrome()
driver.get("http://www.baidu.com")
driver.find_element_by_id('kw').send_keys("selenium基础总结")
driver.find_element_by_id('su').submit()