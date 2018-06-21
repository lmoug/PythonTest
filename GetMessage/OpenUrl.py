#coding=gbk
'''
Created on 2017

@author: mgliu
'''


import sys, urllib,urllib2
from bs4 import BeautifulSoup
import re,os,string
import gzip
import StringIO

first_url="http://detail.zol.com.cn/cell_phone_advSearch/subcate57_1_s1398-s7074-s6500-s6502-s6106_1_1_0_1.html?#showc"
#later_url = "http://detail.zol.com.cn/cell_phone_advSearch/subcate57_1_s1398-s7074-s6500-s6502-s6106_1_1__"

req = urllib2.Request(first_url,headers={'User-Agent':"Magic Browser"})
page = urllib2.urlopen(req)
data = page.read()

soup = BeautifulSoup(data,from_encoding="gbk")

page_result=soup.find("div",attrs={"class":"page_total"})

#print (page_result)

for child in page_result:
    name = unicode(str(child),"utf-8")
    if str(name).find(u"ÿҳ") !=-1:
        print (str(child))



for link in soup.find_all('a'):
    if str(link).find("param.shtml") != -1:
        print (str(link))
