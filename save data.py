#!/usr/bin/Python
# -*- coding: utf-8 -*-
from urllib.request import urlretrieve
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.pythonscraping.com")
bsObj = BeautifulSoup(html,"html.parser")
imageLocation = bsObj.find("a",attrs={'title':'Home'}).find("img")["src"]
urlretrieve(imageLocation,"logo.jpg")

