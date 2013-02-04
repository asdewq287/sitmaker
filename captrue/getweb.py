#!/usr/bin/python
# --*-- coding: utf-8 --*--
'''
Created on 2013-2-4

@author: liuzj
'''
import urllib

if __name__ == '__main__':
    response = urllib.urlopen('http://demo.6888.net/8125_4149/')
    line=response.readline()
    while line!=None and line!='':
        print line,
        line=response.readline()
        
    
    pass