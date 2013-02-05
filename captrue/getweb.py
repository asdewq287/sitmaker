#!/usr/bin/python
# --*-- coding: utf-8 --*--
'''
Created on 2013-2-4

@author: liuzj
'''
import os  
import urllib  , httplib  
from bs4 import BeautifulSoup
import re

def use_urllib(url):  
#    httplib.HTTPConnection.debuglevel = 1   
    page = urllib.urlopen(url)  
    bs=BeautifulSoup(page.read())
    #创建网站文件夹
    #处理css文件，如果没有css文件夹就创建
    #处理js文件，如没有js文件夹就创建
    #处理页面中的图片，如果没有img文件夹就创建
    #替换导入文件和图片的路径
    #保存网页



    
    srcs=bs.findAll('script')
    for src in srcs:
        try:
            print src['src']
        except:
            pass
    links=bs.findAll('link')
    for link in links:
        print link['href']
        
    print '========================'
    imgs=bs.findAll(style=re.compile(".*url\\(.*\\).*"))
    for img in imgs:
        print img['style']
    
#    print "status:", page.getcode() #200请求成功,404  
#    print "url:", page.geturl()  
#    print "head_info:\n",  page.info()  
#    print "Content len:", len(page.read())  
    
def  callback_f(downloaded_size, block_size, romote_total_size):  
    per = 100.0 * downloaded_size * block_size / romote_total_size  
    if per > 100:  
        per = 100   
    print "%.2f%%"% per   
  
def use_urllib_retrieve(url):  
    local = os.path.join(os.path.abspath("../sitemaker/download/"), "index.html")  
    print local  
    urllib.urlretrieve(url,local,callback_f) 


if __name__ == '__main__':
    url = "http://demo.6888.net/8125_4149/"  
    use_urllib(url)
    pass