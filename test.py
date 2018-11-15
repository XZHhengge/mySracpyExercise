import requests
from bs4 import BeautifulSoup

account = input('请输入你的学号：')
pwd = input('请输入你的密码：')
data = {'account': account, 'pwd': pwd, 'verifycode': ''}

r = requests.post('http://210.38.250.43/login!doLogin.action', data=data)
cookies = r.cookies.get_dict()
e = requests.post('http://210.38.250.43/login!doLogin.action', data=data,cookies=cookies)

x = requests.get('http://210.38.250.43/xjkpxx!xjkpList.action', cookies=cookies)

soup = BeautifulSoup(x.text, "lxml")
info = soup.select("label")
print('学籍信息')
for i in info:
    print(i.parent.previous_element.previous_element + i.getText())
