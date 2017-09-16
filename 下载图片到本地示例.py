# -* - coding: UTF-8 -* -
# !/usr/bin/python
# 下载网页图片到本地文件夹
#python 2.7
# import os, urllib2, urllib
# # 设置下载后存放的本地路径"E:\img\1.jpg"
# path = r'E:\img'
# file_name = r'1.jpg'
# dest_dir = os.path.join(path, file_name)
# # 设置链接的路径
# url = "http://pic3.nipic.com/20090518/2662644_083611033_2.jpg"
# # 定义下载函数downLoadPicFromURL（本地文件夹，网页URL）
# def downLoadPicFromURL(dest_dir, URL):
#     try:
#         urllib.urlretrieve(url, dest_dir)
#     except:
#         print '\tError retrieving the URL:', dest_dir
# downLoadPicFromURL(dest_dir, url)