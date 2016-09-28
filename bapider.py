# -*- coding:utf-8 -*-
import urllib
import urllib2
import re
import thread
import time


def getStories():
    user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
    headers = { 'User-Agent' : user_agent }
    print(pageIndex)
    print('\n\n')
    url = 'http://www.qiushibaike.com/hot/page/%s/?s=4916034' % str(pageIndex)
    #构建请求的request
    request = urllib2.Request(url,headers = headers)
    #利用urlopen获取页面代码
    response = urllib2.urlopen(request)
    #将页面转化为UTF-8编码
    pageCode = response.read().decode('utf-8')
    #重点在于如何使用正则表达式进行匹配
    pattern = re.compile('<span>.*?</span>', re.S)
    #pattern = re.compile(u"<span>.*?[\u4e00-\u9fa5]</span>", re.S)
    items = re.findall(pattern, pageCode)
    for item in items:
        if not re.search('img src', item):
            print(item)
#it also can use bs4
from bs4 import beautifulsoup
soup = beautifulsoup(html_doc,
                     'html_parser',
                     encoding='utf-8')
links = soup.find_all('span', class_ = '')
# end 
# www.qiushibaike.com 

I = raw_input()
for pageIndex in range(1,int(I)+1):
    getStories()
    raw_input()
print("EXIT !")
