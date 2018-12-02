# -*- coding: utf-8 -*-
'''requests模块url传值'''
import requests
data = {
    'name': 'gemmey',
    'age': 22
}
resopnse = requests.get('http://httpbin.org/get', params=data)
print(resopnse.text)

#维持会话
import requests
r = requests.Session()
r.get('http://httpbin.org/cookies/set/number/124151')
resopnse = r.get('http://httpbin.org/cookies')
print(resopnse.text)

#证书验证
import requests
resopnse = requests.get('https://www.12306.cn', verify=False)
print(resopnse.status_code)


#认证设置
import requests
from requests.auth import HTTPBasicAuth

r = requests.get('', auth=HTTPBasicAuth('user', '1232'))

r = requests.post('', auth={'user', '123'})

