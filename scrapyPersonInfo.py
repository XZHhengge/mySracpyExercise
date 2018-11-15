#coding=utf-8
import urllib.request
import http.cookiejar
import json
from bs4 import  BeautifulSoup

#修改为自己的学号和密码
username = input('请输入学号: ')
password = input('请输入密码: ')
date = input('请输入你要查看课表的周数')

if( username == "学号" or  password == "密码" ):
   exit("*** 请修改必要资料 ***")

print("*** 开始执行 ***\n")
#第一次进入首页，获取cookie
url = 'http://210.38.250.43/login!doLogin.action'
htmlObj = urllib.request.urlopen(url)
cookie = http.cookiejar.LWPCookieJar("cookies.txt")
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
urllib.request.install_opener(opener)
urllib.request.urlopen(url)
cookie.save(ignore_discard=True, ignore_expires=True)


#进行登陆操作
url = 'http://210.38.250.43/login!doLogin.action'
postData = {
   "account": username,
   "pwd": password
}

postDataEncode = urllib.parse.urlencode(postData).encode(encoding="UTF8")
request = urllib.request.Request(url,data = postDataEncode,method="POST")
htmlObj = urllib.request.urlopen(request)
html = htmlObj.read().decode("UTF-8")
resultJson = json.loads(html)

if resultJson['status'] == 'y':
   print("*** 登陆成功 ***\n")
else:
   print("登陆失败:" + resultJson['msg'] )
   exit("*** 执行结束 ***")

print("*** 获取用户信息 ***")
url = 'http://210.38.250.43/xjkpxx!xjkpList.action'
htmlObj = urllib.request.urlopen(url)
html = htmlObj.read().decode("UTF-8")
soup = BeautifulSoup(html, "lxml")
info = soup.select("label")
print('学籍信息')
for i in info:
    print(i.parent.previous_element.previous_element + i.getText())




posturl = 'http://210.38.250.43/xsgrkbcx!getKbRq.action?xnxqdm=201801&zc='+date

htmlobj3 = urllib.request.urlopen(posturl)
html3 = htmlobj3.read().decode("UTF-8")
soup3 = BeautifulSoup(html3, 'lxml')
jsons = json.dumps(soup3.get_text(), ensure_ascii=False)
js = json.loads(jsons)
print('这是第'+date+'周的课表')
print(js)


exit("\n*** 爬取结束 ***")
