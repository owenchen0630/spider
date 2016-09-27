#-*-coding:utf-8-*-
import urllib2
import cookielib
from bs4 import BeautifulSoup
url = "http://www.baidu.com"

re = urllib2.urlopen(url)
print(re.getcode())


request = urllib2.Request(url)
request.add_header("user-agent", "Mozilla/5.0")
response2 = urllib2.urlopen(request)
print(response2.getcode())
html_doc = response2.read()
print(html_doc)
# cj = cookielib.CookieJar()
# opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
# urllib2.install_opener(opener)
# response3 = urllib2.urlopen(url)
# print(response3.getcode())
# print(cj)
# print(response3.read())

soup = BeautifulSoup(html_doc,
                     'html.parser',
                     from_encoding='utf-8')
soup.find_all('a', herf='')