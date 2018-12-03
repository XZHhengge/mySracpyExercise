# -*- coding: utf-8 -*-

#exercise1
import urllib.request
resopnse = urllib.request.urlopen('http://www.baidu.com')
print(resopnse.read().decode('utf-8'))

#exercise2_post
import urllib.parse
import urllib.request

data = bytes(urllib.parse.urlencode({'world':'hello'}), encoding='utf-8')
resopnse = urllib.request.urlopen('http://httpbin.org/post',data=data)
print(resopnse.read())

#exercise3
import socket
import urllib.request
import urllib.error
try:
    resopnse = urllib.request.urlopen('http://httpbin.org/get',timeout=0.1)
except urllib.error.URLError as e:
    if isinstance(e.reason, socket.timeout):
        print("TIME OUT")


#exercise4
import urllib.request
resopnse = urllib.request.urlopen('http://www.python.org')
print(resopnse.status)
print(resopnse.getheaders())
print(resopnse.getheaders('Server'))

#exericse5_
'''请求头加上headers'''
from urllib import request,parse

url = 'http://httpbin.org/post'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0) Gecko/20100101 Firefox/61.0',
    'Host': 'httpbin.org'
}
dict = {
    'name': 'Germey'
}
data = bytes(parse.urlencode(dict), encoding='utf-8')
req = request.Request(url=url, data=data, headers=headers, method='POST')
resopnse = request.urlopen(req)
print(resopnse.read().decode('utf-8'))


from urllib import request,parse
url = 'http://www.xicidaili.com'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0) Gecko/20100101 Firefox/61.0',
    'Host': 'www.xicidaili.com'
}
req = urllib.request.Request(url=url, headers=headers)
resopnse = request.urlopen(req)
print(resopnse.read().decode('utf-8'))


# Handler  代理
import urllib.request
proxy_handler = urllib.request.ProxyHandler({
    'http': 'http://',
    'https': 'https://'
})
opener = urllib.request.urlopen(proxy_handler)
resopnse = opener.open('http://')

# Cookies
import http.cookiejar
from urllib import request
cookie = http.cookiejar.CookieJar()
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
resopnse = opener.open('http://www.baidu.com')
for item in  cookie:
    print(item)

#保存cookies_1
import http.cookiejar, urllib.request
filename = 'cookie.txt'
cookie = http.cookiejar.MozillaCookieJar(filename)
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
resopnse = opener.open('http://www.baidu.com')
cookie.save(ignore_discard=True, ignore_expires=True)

#保存cookies2.0
import http.cookiejar, urllib.request
filename = 'cookie.txt'
cookie = http.cookiejar.LWPCookieJar(filename)
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
resopnse = opener.open('http://www.baidu.com')
cookie.save(ignore_discard=True, ignore_expires=True)

#使用cookie
import http.cookiejar,urllib.request
cookie = http.cookiejar.LWPCookieJar()
cookie.load('cookie.txt', ignore_expires=True, ignore_discard=True)
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
resopnse = opener.open('http://www.baidu.com')
print(resopnse.read().decode('utf-8'))

#urlencode  url传值
from urllib.parse import urlencode
params = {
    'name': 'gemmey',
    'age': 22
}
base_url = 'http://www.baudi.com?'
url = base_url + urlencode(params)
print(url)