#-*-coding:utf-8-*-
import urllib2
from urllib2 import Request, urlopen
import cookielib
from logging.handlers import HTTPHandler
from pip._vendor.distlib.util import HTTPSHandler

url = 'http://www.baidu.com'
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = { 'User-Agent' : user_agent }

se = urllib2.Request(url, headers = headers)
req = urllib2.urlopen(se)
pagecode = req.read()
print(pagecode)


res = Request(url)
response = urlopen(res)
# print(url)
# print(response.geturl())
# print('INFO')
# print(response.info())

cookie  = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
res = opener.open(url)
#for item in cookie:
#     print 'Name = ' + item.name
#     print 'Value = ' + item.value


#Debug log
httpHandler = urllib2.HTTPHandler(debuglevel=1)
httpsHandler = urllib2.HTTPSHandler(debuglevel=1)
opener = urllib2.build_opener(httpHandler, httpsHandler)
urllib2.install_opener(opener)
res = urllib2.urlopen(url)

