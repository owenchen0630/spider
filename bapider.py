# -*- coding:utf-8 -*-
import urllib
import urllib2
import re
import thread
import time


pageIndex = 1
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
#初始化headers
headers = { 'User-Agent' : user_agent }
#存放段子的变量，每一个元素是每一页的段子们
stories = []
#存放程序是否继续运行的变量
enable = False
#传入某一页的索引获得页面代码


url = 'http://www.qiushibaike.com/hot/' + str(pageIndex)
 #构建请求的request
request = urllib2.Request(url,headers = headers)
#利用urlopen获取页面代码
response = urllib2.urlopen(request)
#将页面转化为UTF-8编码
pageCode = response.read().decode('utf-8')
print(page.code)
